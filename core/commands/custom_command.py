import json
import os
import sys
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from core.src.settings import (
    MSG_ON_SAME_CHAT
)
from core.src.static_modules import db


class CustomCommand(object):

    def __init__(self, bot, language, command, arg, params):

        self.bot = bot
        self.language = language
        self.command = command

        self.arg = arg

        self.stored_ppl_data = []
        self.file_path = "data_global/ppl.json"
        self.url = 'http://users.dimi.uniud.it/~alberto.policriti/home/?q=node/42'
        self.num_max_scores = 6  # Number of scores shown as results
        self.bot_last_check = None
        self.check_every_t_min = 10  # time in min between a check and another
        self.time_between_last_check = 0

    def web_scrapper(self):

        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')

        outer_table = soup.find('tbody')
        table = outer_table.find_next('tbody')
        table_entries = table.find_all_next('tr')

        scores = []
        for el in table_entries:
            font = el.find_all('font')
            name = font[0].find('b').get_text()
            score = font[1].get_text()
            scores.append((name, score))

        return scores

    def check_differences(self):

        def str_to_datetime(a): return datetime.strptime(a, '%y-%m-%d %H:%M:%S')
        def datetime_to_str(a): return str(a.strftime("%y-%m-%d %H:%M:%S"))

        with open(os.path.join(sys.path[0], self.file_path), "r") as infile:
            stored_ppl_json = json.load(infile)

        self.bot_last_check = str_to_datetime(stored_ppl_json.get('bot_last_check'))
        self.time_between_last_check = (datetime.now() - self.bot_last_check).seconds // 60 % 60

        del stored_ppl_json['bot_last_check']  # remove control value

        stored_ppl_json_keys = stored_ppl_json.keys()

        # load and convert to tuple existing data from json
        for name in stored_ppl_json_keys:
            score = stored_ppl_json[name].get('score')
            timestamp = str_to_datetime(stored_ppl_json[name].get('timestamp'))
            self.stored_ppl_data.append((name, score, timestamp))

        # if is time, check for new entries and add them
        new_entries_json = {}
        new_entries_tuple = []

        if self.time_between_last_check >= self.check_every_t_min:
            new_ppl_data = self.web_scrapper()
            self.bot_last_check = datetime.now()
            self.time_between_last_check = 0

            new_timestamp = datetime_to_str(datetime.now())
            for name, score in new_ppl_data:
                if name not in stored_ppl_json_keys:
                    new_entries_json[name] = {
                        'score': score,
                        'timestamp': new_timestamp,
                    }
                    new_entries_tuple.append((name, score, datetime.now()))

            self.stored_ppl_data.extend(new_entries_tuple)
            stored_ppl_json = {
                    'bot_last_check': datetime_to_str(self.bot_last_check),
                    **stored_ppl_json,
                    **new_entries_json,
                }

            with open(os.path.join(sys.path[0], self.file_path), "w") as outfile:
                json.dump(stored_ppl_json, outfile, indent=2)

        return new_entries_tuple

    @staticmethod
    def build_person_string(name, score, timestamp):

        dt = '{}'.format(timestamp.strftime('alle %H:%M il %d %b'))
        return '**{}: {}** -- {}\n'.format(name, score, dt)

    def void_arg(self):

        self.check_differences()

        self.stored_ppl_data.sort(key=lambda tup: tup[2], reverse=True)

        latest_publication_time = (datetime.now() - self.stored_ppl_data[0][2]).days
        out = 'L\'ultimo voto è uscito {}'
        if latest_publication_time is 0:
            out = out.format('**oggi**.\n')
        elif latest_publication_time is 1:
            out = out.format('**ieri**.\n')
        elif latest_publication_time > 1:
            out = out.format('**' + str(latest_publication_time) + ' giorni fa**\n')

        if self.time_between_last_check <= 1:
            out += 'Ultimo controllo un istante fa.\n'
        else:
            out += 'Ultimo controllo {} minuti fa, alle {}.\n'.format(
                self.time_between_last_check,
                self.bot_last_check.strftime('%H:%M')
            )

        out += '\nHai utilizzato *{}* volte il comando.\n'.format(db.get_command_interactions(self.command))

        today_ppl_data = []
        yesterday_ppl_data = []
        other_ppl_data = []

        counter = 0
        for el in self.stored_ppl_data:
            publication_time = (datetime.now() - el[2]).days
            if publication_time is 0:
                today_ppl_data.append(el)
                counter += 1
            elif publication_time is 1:
                yesterday_ppl_data.append(el)
                counter += 1
            elif publication_time > 1:
                other_ppl_data.append(el)
                counter += 1
                if counter >= self.num_max_scores:
                    break

        if today_ppl_data:
            out += '\nVOTI USCITI OGGI:\n'
            for name, score, timestamp in today_ppl_data:
                out += self.build_person_string(name, score, timestamp)
        if yesterday_ppl_data:
            out += '\nVOTI USCITI IERI:\n'
            for name, score, timestamp in yesterday_ppl_data:
                out += self.build_person_string(name, score, timestamp)
        if other_ppl_data:
            out += '\nVOTI USCITI DI RECENTE:\n'
            for name, score, timestamp in other_ppl_data:
                out += self.build_person_string(name, score, timestamp)

        self.bot.send_message(out, MSG_ON_SAME_CHAT, parse_mode_en=True)

    def all_scores(self):

        out = ''
        self.check_differences()

        for name, score, timestamp in self.stored_ppl_data:
            out += self.build_person_string(name, score, timestamp)
            if len(out) > 1900:
                self.bot.send_message(out, MSG_ON_SAME_CHAT, parse_mode_en=True)
                out = ''

        out += '\nLISTA COMPLETA VOTI\nIN ORDINE ALFABETICO\n\n'
        self.bot.send_message(out, MSG_ON_SAME_CHAT, parse_mode_en=True)

    def custom_command(self):

        chose = {
            '': self.void_arg,
            'all': self.all_scores,
        }

        chose[self.arg]()

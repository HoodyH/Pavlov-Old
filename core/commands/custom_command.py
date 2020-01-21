import json
import os
import sys
import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from core.src.settings import (
    MSG_ON_SAME_CHAT
)


class CustomCommand(object):

    def __init__(self, bot, language, command, arg, params):

        self.bot = bot
        self.language = language
        self.command = command

        self.arg = arg

        # parameter handed
        self._filter = None
        self._set = None

        self.file_path = "data_global/ppl.json"

        _vars = ['filter', 'set']
        for param in params:
            name = '_{}'.format(param[0])
            setattr(self, name, param[1])

    @staticmethod
    def web_scrapper():
        url = 'http://users.dimi.uniud.it/~alberto.policriti/home/?q=node/42'

        page = requests.get(url)
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

    @staticmethod
    def save_ppl(file_path, data):

        with open(os.path.join(sys.path[0], file_path), "w") as outfile:
            json.dump(data, outfile)

    @staticmethod
    def load_ppl(file_path):
        with open(os.path.join(sys.path[0], file_path), "r") as json_file:
            data = json.load(json_file)
        return data

    def check_differences(self):

        new_entries = {}
        stored_ppl_data = self.load_ppl(self.file_path)
        new_ppl_data = self.web_scrapper()
        stored_ppl_data_keys = stored_ppl_data.keys()

        for el in new_ppl_data:
            if el[0] not in stored_ppl_data_keys:
                new_entries[el[0]] = {
                    'score': el[1],
                    'timestamp': str(datetime.now().strftime("%y-%m-%d %H:%M:%S")),
                }
        merged = {**stored_ppl_data, **new_entries}
        self.save_ppl(self.file_path, merged)

        return new_entries

    def custom_command(self):

        def void_arg():

            out = ''
            new_entries = self.check_differences()

            if new_entries:
                out = '**Il poli ha caricato voti nuovi!**'
                for el in new_entries.keys():
                    name = el
                    score = new_entries[el].get('score')
                    out += '{}: {}\n'.format(name, score)
                out = '\n'
            else:
                out = 'Il poli non ha aggiunto nulla di nuovo dall\' ultimo aggiornamento... '
                out += 'ritenta e sarai più fortunato\n\n'

            stored_ppl_data = self.load_ppl(self.file_path)

            data = []
            for el in stored_ppl_data.keys():
                name = el
                score = stored_ppl_data[el].get('score')
                timestamp = datetime.strptime(stored_ppl_data[el].get('timestamp'), '%y-%m-%d %H:%M:%S')
                data.append((name, score, timestamp))

            data.sort(key=lambda tup: tup[2], reverse=True)

            latest_publication = (datetime.now() - data[0][2]).days
            out += 'L\'ultimo voto è uscito {} giorni fa\n\n'.format(latest_publication)

            out += 'LISTA ULTIMI 6 VOTI:\n'
            count = 0
            for el in data:
                out += '**{}: {}** - uscito il: {}\n'.format(el[0], el[1], str(el[2]))

                count += 1
                if count >= 6:
                    break

            self.bot.send_message(out, MSG_ON_SAME_CHAT, parse_mode_en=True)

        def all_scores():

            out = 'LISTA COMPLETA VOTI:\n'
            self.check_differences()
            stored_ppl_data = self.load_ppl(self.file_path)

            for el in stored_ppl_data.keys():
                name = el
                score = stored_ppl_data[el].get('score')
                timestamp_str = stored_ppl_data[el].get('timestamp')
                out += '**{}: {}** - uscito il: {}\n'.format(name, score, timestamp_str)
                if len(out) > 1900:
                    self.bot.send_message(out, MSG_ON_SAME_CHAT, parse_mode_en=True)
                    out = ''

            self.bot.send_message(out, MSG_ON_SAME_CHAT, parse_mode_en=True)

        chose = {
            '': void_arg,
            'all': all_scores,
        }

        chose[self.arg]()

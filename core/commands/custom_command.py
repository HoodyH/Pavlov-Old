import json
import os
import sys
import requests
from bs4 import BeautifulSoup
from core.src.settings import (
    MSG_ON_SAME_CHAT
)
from core.src.utils.select_handler import random_between


class CustomCommand(object):

    def __init__(self, bot, language, command, arg, params):

        self.bot = bot
        self.language = language
        self.command = command

        self.arg = arg

        # parameter handed
        self._filter = None
        self._set = None

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

        scores = {}
        for el in table_entries:
            font = el.find_all('font')
            name = font[0].find('b').get_text()
            score = font[1].get_text()
            scores[name] = score

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

    @staticmethod
    def check_differences(stored_ppl_data, new_ppl_data):
        differences = {}
        stored_ppl_data_keys = stored_ppl_data.keys()

        for el in new_ppl_data.keys():
            if el not in stored_ppl_data_keys:
                differences[el] = new_ppl_data.get(el)

        return differences

    def custom_command(self):

        def void_arg():

            out = ''

            file_path = "ppl.json"
            stored_ppl_data = self.load_ppl(file_path)
            new_ppl_data = self.web_scrapper()
            differences = self.check_differences(stored_ppl_data, new_ppl_data)
            if differences:
                for el in differences.keys():
                    name = el
                    score = differences.get(el)
                    out += '{} Voto: {}\n'.format(name, score)
            else:
                out = 'Il poli non ha aggiunto nulla di nuovo... ritenta e sarai più fortunato'

            self.save_ppl(file_path, new_ppl_data)
            self.bot.send_message(out, MSG_ON_SAME_CHAT)

        chose = {
            '': void_arg,
        }

        chose[self.arg]()

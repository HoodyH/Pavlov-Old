import requests
from bs4 import BeautifulSoup
"""from old_core.src.utils.select_handler import random_between"""


class Chatrubate(object):

    def __init__(self, bot, language, command, arg, params, *args, **kwargs):

        self.bot = bot
        self.language = language

        self.arg = arg

        self._first = None
        self._idx = None
        self._n = None
        self._girls = None

        _vars = ['first', 'idx', 'n', 'girls']
        for param in params:
            name = '_{}'.format(param[0])
            setattr(self, name, param[1])

        self.url = 'https://it.chaturbate.com'

        self.girls_list = []

    def web_scrapper(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')

        for vid in soup.findAll(attrs={'class': 'room_list_room'}):
            self.girls_list.append(vid.find('a')['href'])

    def chatrubate(self):

        self.web_scrapper()
        len_vl = len(self.girls_list) - 1
        print(len_vl)

        # Send the first o the query
        if self._first is not None:
            self.bot.send_message(self.url + self.girls_list[0], MSG_ON_SAME_CHAT)
            return

        if self._girls is not None:
            out = ''
            girls = self.girls_list[:20]
            for girl in girls:
                out += '{}\n'.format(girl.replace('/', ''))
            self.bot.send_message(out, MSG_ON_SAME_CHAT)
            return

        # send in chat a stack of videos
        if self._n:
            n = int(self._n)
            for girl in self.girls_list:
                self.bot.send_message(self.url + girl, MSG_ON_SAME_CHAT)
                n -= 1
                if n is 0:
                    break
            return

        # Send a specific video in the query array
        if self._idx:
            idx = int(self._idx) - 1

            if idx > len_vl:
                idx = len_vl
            if idx < 0:
                idx = 0

        else:
            idx = random_between(0, len_vl)

        out = self.url + self.girls_list[idx]
        self.bot.send_message(out, MSG_ON_SAME_CHAT)

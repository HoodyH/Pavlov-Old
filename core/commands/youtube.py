import requests
from random import randrange
from bs4 import BeautifulSoup
from pvlv.settings import (
    MSG_ON_SAME_CHAT
)
from core.src.utils.select_handler import random_between


class Youtube(object):

    def __init__(self, bot, language, command, arg, params, *args, **kwargs):

        self.bot = bot
        self.language = language

        self.arg = arg

        self._first = None
        self._idx = None
        self._n = None

        _vars = ['first', 'idx', 'n']
        for param in params:
            name = '_{}'.format(param[0])
            setattr(self, name, param[1])

        self.url_search = 'https://www.youtube.com/results?search_query={}'
        self.url_video = 'https://www.youtube.com{}'

        self.no_entry = [
            'japanese cooking',
            'cat videos',
            'asmr',
            'memes',
            'funny videos',
            'music'
        ]

    def compose_url(self, entry):
        if not entry:
            entry = self.no_entry[randrange(0, len(self.no_entry) - 1)]
            url = self.url_search.format(entry)
        else:
            url = self.url_search.format(entry)

        return url

    def web_scrapper(self, url):

        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        video_list = []
        for vid in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
            vid_pointer = vid['href']
            # if not vid_pointer.startswith('/channel'):
            video_list.append(self.url_video.format(vid_pointer))

        return video_list

    def youtube(self):

        url = self.compose_url(self.arg)
        video_list = self.web_scrapper(url)
        len_vl = len(video_list) - 1
        print(len_vl)

        # Send the first o the query
        if self._first is not None:
            self.bot.send_message(video_list[0], MSG_ON_SAME_CHAT)
            return

        # send in chat a stack of videos
        if self._n:
            n = int(self._n)
            for video in video_list:
                self.bot.send_message(video, MSG_ON_SAME_CHAT)
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

        out = video_list[idx]
        self.bot.send_message(out, MSG_ON_SAME_CHAT)

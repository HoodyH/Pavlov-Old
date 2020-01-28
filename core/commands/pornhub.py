import requests
from bs4 import BeautifulSoup
from pvlv.settings import (
    MSG_ON_SAME_CHAT
)
from core.src.utils.select_handler import random_between


class Pornhub(object):

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

        self.url_search = 'https://it.pornhub.com/video/search?search={}'
        self.url_video = 'https://it.pornhub.com/view_video.php?viewkey={}'

    def compose_url(self, entry):
        if not entry:
            url = self.url_search.format('video')
        else:
            url = self.url_search.format(entry)

        return url

    def web_scrapper(self, url):

        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        body = soup.body
        video_search_result = body.find(id='videoSearchResult')
        video_boxes = video_search_result.find_all('li', class_='js-pop videoblock videoBox')

        video_list = []
        for el in video_boxes:
            video_key = el.get('_vkey')
            video_list.append(self.url_video.format(video_key))

        return video_list

    def pornhub(self):

        url = self.compose_url(self.arg)
        video_list = self.web_scrapper(url)
        len_vl = len(video_list) - 1

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

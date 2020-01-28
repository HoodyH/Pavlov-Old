import requests
import json
from pvlv.settings import (
    MSG_ON_SAME_CHAT
)
from core.src.utils.select_handler import random_between


class HanimeTv(object):

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

        self.url = 'https://hanime.tv'
        self.url_search = 'https://search.hanimetv.club/'
        self.url_video = 'https://hanime.tv/videos/hentai/{}'

        self.video_list = []

    def __search(self, tags, query=""):

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'it,it-IT;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'content-type': 'application/json',
            'Origin': self.url,
            'Connection': 'keep-alive',
            'TE': 'Trailers'
        }
        data = {
            "search_text": query,
            "tags": tags,
            "tags_mode": "OR",
            "brands": [],
            "blacklist": [],
            "order_by": "released_at_unix",
            "ordering": "desc",
            "page": 0
        }
        req = requests.post(self.url_search, headers=headers, json=data)
        response = json.loads(req.text)

        for video_data in json.loads(response.get('hits')):
            self.video_list.append(video_data)

    def __send_hanime_video(self, video_data):

        slug = video_data.get('slug')
        description = video_data.get('description')
        tags = video_data.get('tags')
        is_censored = video_data.get('is_censored')
        views = video_data.get('views')

        out = 'Description:\n{}\n\nTags:\n{}\n\nCensored: {}\n\nViews: {}\n\n{}'.format(
            description.replace('<p>', '').replace('</p>', ''),
            tags,
            is_censored,
            views,
            self.url_video.format(slug),
        )

        self.bot.send_message(out, MSG_ON_SAME_CHAT)

    def hanime_tv(self):

        self.__search([])
        len_vl = len(self.video_list) - 1
        print(len_vl)

        # Send the first o the query
        if self._first is not None:
            self.__send_hanime_video(self.video_list[0])
            return

        # send in chat a stack of videos
        if self._n:
            n = int(self._n)
            for video in self.video_list:
                self.__send_hanime_video(video)
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

        self.__send_hanime_video(self.video_list[idx])

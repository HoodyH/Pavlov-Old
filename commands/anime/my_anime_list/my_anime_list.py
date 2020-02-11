import requests
import json


class MyAnimeList(object):

    def __init__(self, bot, language, command, arg, params, *args, **kwargs):

        self.bot = bot
        self.language = language

        self.arg = arg

        self._res = None
        self._idx = None
        self._all = None

        _vars = ['res', 'idx', 'all']
        for param in params:
            name = '_{}'.format(param[0])
            setattr(self, name, param[1])

        self.url_search = 'https://api.jikan.moe/v3/search/anime?q={}'
        self.url_item = 'https://api.jikan.moe/v3/anime/{}'

        self.title = None
        self.title_english = None
        self.image_url = None
        self.synopsis = None
        self.airing = None
        self.premiered = None
        self.broadcast = None
        self.episodes = None
        self.duration = None
        self.genres = []
        self.rank = None
        self.trailer_url = None
        self.mal_url = None

    @staticmethod
    def __make_search(url):
        page = requests.get(url)
        json_data = json.loads(page.content)

        json_results = json_data.get('results')

        results = []
        for result in json_results:
            title = result.get('title')
            mal_id = result.get('mal_id')
            results.append((title, mal_id))

        return results

    def __get_anime_info(self, mai_id):
        page = requests.get(self.url_item.format(mai_id))
        data = json.loads(page.content)

        self.title = data.get('title')
        self.title_english = data.get('title_english')
        self.image_url = data.get('image_url')
        self.synopsis = data.get('synopsis')
        self.airing = data.get('airing')
        self.premiered = data.get('premiered')
        self.broadcast = data.get('broadcast')
        self.episodes = data.get('episodes')
        self.duration = data.get('duration')

        data_genres = data.get('genres')
        for genre in data_genres:
            self.genres.append(genre.get('name'))

        self.rank = data.get('rank')
        self.score = data.get('score')
        self.trailer_url = data.get('trailer_url')
        self.mal_url = data.get('url')

    def my_anime_list(self):

        if not self.arg:
            out = no_arg_error(self.language)
            self.bot.send_message(out, MSG_ON_SAME_CHAT)
            return

        url = self.url_search.format(self.arg)
        results = self.__make_search(url)[:10]

        out = ''
        count = 1
        if self._res is not None:
            for title, mal_id in results:
                out += '{}) {}\n'.format(count, title)
                count += 1
            self.bot.send_message(out, MSG_ON_SAME_CHAT)
            return

        idx = 0
        if self._idx is not None:
            idx = int(self._idx) - 1

        self.__get_anime_info(results[idx][1])

        # Print MAL url and TRAILER
        if self._all is not None:
            if self.trailer_url:
                self.bot.send_message(self.trailer_url, MSG_ON_SAME_CHAT)
            self.bot.send_message(self.mal_url, MSG_ON_SAME_CHAT)

        # Build Details Message
        if self.title == self.title_english:
            out += '**{}**\n\n'.format(self.title)
        else:
            out += '**{}**\n**{}**\n\n'.format(self.title, self.title_english)

        out += airing(self.language, self.airing, self.broadcast, self.premiered)
        out += genres(self.language, self.genres)
        out += details(
            self.language,
            self.episodes,
            self.duration,
            self.rank,
            self.score,
        )
        self.bot.send_message(out, MSG_ON_SAME_CHAT, parse_mode_en=True)

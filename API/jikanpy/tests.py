from API.jikanpy.jikanpy import Jikan
from pprint import pprint

jikan = Jikan()

anime = jikan.anime(34134)

title = anime.get('title')
broadcast_time = anime.get('broadcast')
airing = anime.get('airing')
status = anime.get('status')
episodes = anime.get('episodes')
print(broadcast_time, airing, episodes)
if airing is True:
    print(title)
    print(broadcast_time)
    print(status)

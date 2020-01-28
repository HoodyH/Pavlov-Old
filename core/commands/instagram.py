import json
import requests
from bs4 import BeautifulSoup
from pvlv.settings import (
    MSG_ON_SAME_CHAT
)


class Instagram(object):

    def __init__(self, bot, language, command, arg, params, *args, **kwargs):

        self.bot = bot
        self.language = language

        self.arg = arg

        # parameter handed
        self._n = None

        _vars = ['n']
        for param in params:
            name = '_{}'.format(param[0])
            setattr(self, name, param[1])

        # internal var
        self.is_private = None
        self.username = None
        self.full_name = None
        self.profile_pic_url_hd = None
        self.is_verified = None
        self.is_business_account = None
        self.business_category_name = None
        self.is_joined_recently = None
        self.connected_fb_page = None
        self.biography = None
        self.external_url = None
        self.followers = None
        self.following = None

        self.media_count = None  # number of total post in the profile
        self.img_list = []  # tuple (text, url_image)

        self.file_path = 'data_global/university/file'

    @staticmethod
    def compose_url(entry):
        if entry.startswith('http'):
            return entry
        else:
            username = entry.replace('@', '')
            url = 'https://www.instagram.com/{}/'.format(username)
            return url

    def web_scrapper(self, url):

        try:
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            script = soup.body.script.text
            start_of_json = str(script).find('{')
            script = script[start_of_json:-1]
            data = json.loads(script)

            entry_data = data.get('entry_data')
            profile_page = entry_data.get('ProfilePage')[0]
            user = profile_page.get('graphql').get('user')

            self.is_private = user.get('is_private')
            self.username = user.get('username')
            self.full_name = user.get('full_name')
            self.profile_pic_url_hd = user.get('profile_pic_url_hd')
            self.is_verified = user.get('is_verified')
            self.is_business_account = user.get('is_business_account')
            self.business_category_name = user.get('business_category_name')
            self.is_joined_recently = user.get('is_joined_recently')
            self.connected_fb_page = user.get('connected_fb_page')
            self.biography = user.get('biography')
            self.external_url = user.get('external_url')
            self.followers = user.get('edge_followed_by').get('count')
            self.following = user.get('edge_follow').get('count')

            # get pics
            edge_media = user.get('edge_owner_to_timeline_media')

            self.media_count = edge_media.get('count')

            self.img_list = []
            media = edge_media.get('edges')
            for el in media:
                node = el.get('node')
                edge_like = node.get('edge_media_preview_like')
                if edge_like:
                    likes = edge_like.get('count')
                else:
                    likes = None
                edges_text = node.get('edge_media_to_caption').get('edges')
                text = ''
                if edges_text:
                    text = edges_text[0].get('node').get('text')

                img = node.get('thumbnail_resources')[-1].get('src')
                self.img_list.append((likes, text, img))

        except Exception as exc:
            print(exc)

    def instagram(self):

        if not self.arg:
            out = 'Devi dare come arg un url o un nome utente (username o @username)'
            self.bot.send_message(out, MSG_ON_SAME_CHAT)
            return

        url = self.compose_url(self.arg)
        self.web_scrapper(url)

        if self.img_list:

            if self._n:
                count = int(self._n)
            else:
                count = 2

            for el in self.img_list:
                if count is 0:
                    break
                count -= 1
                msg_post = 'Likes: {}\n\n{}'.format(
                    el[0],  # likes
                    el[1],  # text
                )

                img = requests.get(el[2])
                open(self.file_path, 'wb').write(img.content)
                self.bot.send_image(open(self.file_path, 'rb'), MSG_ON_SAME_CHAT, caption=msg_post)
        else:
            msg_link = 'Non posso accedere alle immagini!'
            self.bot.send_message(msg_link, MSG_ON_SAME_CHAT)

        msg_profile_pic = 'FOTO PROFILO'
        img = requests.get(self.profile_pic_url_hd)
        open(self.file_path, 'wb').write(img.content)
        self.bot.send_image(open(self.file_path, 'rb'), MSG_ON_SAME_CHAT, caption=msg_profile_pic)

        out = '**Nome Completo:** {}\n\n'.format(self.full_name)
        if self.is_private:
            out += '**Questo utente ha il profilo privato**\n\n'

        out += '**Biografia:** {}\n'.format(self.biography)
        out += '**Folloers:** {}\n'.format(self.followers)
        out += '**Following:** {}\n'.format(self.following)
        if self.connected_fb_page:
            out += '**Facebook:** {}\n'.format(self.connected_fb_page)
        if self.external_url:
            out += '**Sito o link:** {}\n'.format(self.external_url)
        out += '**Account verificato:** {}\n'.format(self.is_verified)
        out += '**Account buisness:** {}\n'.format(self.is_business_account)
        if self.is_business_account:
            out += '**Categoria buisness:** {}\n'.format(self.business_category_name)
        if self.is_joined_recently:
            out += '**Questo profilo è stato creato di recente**'

        self.bot.send_message(out, MSG_ON_SAME_CHAT, parse_mode_en=True)
        self.bot.send_message(url, MSG_ON_SAME_CHAT)

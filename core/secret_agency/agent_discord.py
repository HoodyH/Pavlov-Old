import discord
from core.src.internal_log import Log
from core.src.static_modules import telegram_bot_abstraction
from core.src.url_downloader import download_file_on_disc
from core.secret_agency.wrapper_targets import Targets

sending_point = '-1001440557381'
_sending_point = '-1001444141366'


class MyDiscordAgent(discord.Client):

    def __init__(self, targets, log_en=True, human=False):
        super(MyDiscordAgent, self).__init__()
        self.targets = Targets(targets)
        self.log_en = log_en
        self.human = human
        self.print_log = Log()

        self.user_id = None

    async def _send_message(self, element, sending_function, *args, **kwargs):

        for commissioner in self.targets.commissioners:
            sending_function(element, commissioner.channel_id, *args, **kwargs)

    async def _send_action_message(self, action):
        if action is not None:
            await self._send_message(action, telegram_bot_abstraction.send_message)

    async def _send_img_message(self, url, path, file_name, file_type):

        full_file_path = await download_file_on_disc(url, path, file_name, file_type)

        caption = 'Undercover agent find this on discord.\n{}'
        caption = caption.format(file_name)
        with open(full_file_path, 'rb') as f:
            await self._send_message(f, telegram_bot_abstraction.send_image, caption=caption)

    async def on_ready(self):
        await self.change_presence(afk=False)
        self.print_log.console_login_as('Me', '436515529692545044')

    async def on_message(self, message):

        user_id = message.author.id
        if self.targets.is_under_monitoring_user(user_id):

            self.print_log.console_user_action_log(message.author, message.author.id, message.content)

            if message.attachments:
                user_folder_name = 'users/{}_{}'.format(str(message.author.id), str(message.author))
                for pic in message.attachments:
                    full_url = str(pic['url'])
                    file_name = str('{}_{}'.format(message.timestamp, message.author))
                    file_type = str(full_url.split('/')[-1].split('.')[-1])
                    try:
                        await self._send_img_message(
                            full_url,
                            user_folder_name,
                            file_name,
                            file_type
                        )
                    except Exception as e:
                        print(e)
                        pass

    async def on_member_update(self, before, after):
        user_id = str(after.id)
        if self.targets.is_under_monitoring_user(user_id):

            if str(before.status) != "offline" and str(after.status) == "offline":
                action = '{} has gone {}.'.format(after.name, after.status)
            elif str(before.status) != str(after.status):
                action = '{} has gone {}.'.format(after.name, after.status)
            else:
                action = None

            await self._send_action_message(action)

    async def on_voice_state_update(self, before, after):
        user_id = before.id
        if self.targets.is_under_monitoring_user(user_id):

            if after.voice.voice_channel is not None:
                action = '{} è appena entrato nel calale vocale {} nella gilda {}.'
                action = action.format(after.name, after.voice.voice_channel, after.server)
            elif before.voice.voice_channel != after.voice.voice_channel:
                action = '{} si è appena disconnesso dal calale vocale {} nella gilda {}.'
                action = action.format(before.name, before.voice.voice_channel, after.server)
            else:
                action = None

            await self._send_action_message(action)

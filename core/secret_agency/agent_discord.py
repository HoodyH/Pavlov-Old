import discord
from copy import deepcopy
from core.src.internal_log import Log
from core.src.static_modules import telegram_bot_abstraction
from core.src.url_downloader import download_file_on_disc
from core.secret_agency.wrapper_targets import Targets
from core.src.settings import (
    VOICE_STATUS_UPDATED, MEMBER_UPDATE, MESSAGE_UPDATE
)


class MyDiscordAgent(discord.Client):

    def __init__(self, targets, log_en=True, human=False):
        super(MyDiscordAgent, self).__init__()
        self.target = Targets(targets)
        self.log_en = log_en
        self.human = human
        self.print_log = Log()

        self.user_id = None

    async def _send_message(
        self, element, sending_function, observers=MESSAGE_UPDATE, message_type=MESSAGE_UPDATE,  *args, **kwargs
    ):
        for commissioner in self.target.commissioners:
            _element = deepcopy(element)
            if commissioner.data_to_collect:
                for el in commissioner.data_to_collect:
                    if el == observers:
                        sending_function(_element, commissioner.channel_id, *args, **kwargs)
            else:
                sending_function(_element, commissioner.channel_id, *args, **kwargs)

    async def _send_action_message(self, action, *args, **kwargs):
        if action is not None:
            await self._send_message(action, telegram_bot_abstraction.send_message, *args, **kwargs)

    async def _send_img_message(self, url, path, file_name, file_type, *args, **kwargs):

        buffer_reader = await download_file_on_disc(url, path, file_name, file_type)

        caption = 'Undercover agent find this on discord.\n{}'
        caption = caption.format(file_name)
        await self._send_message(buffer_reader, telegram_bot_abstraction.send_image, caption=caption, *args, **kwargs)

    async def on_ready(self):
        await self.change_presence(afk=False)
        self.print_log.console_login_as('Me', '436515529692545044')

    async def on_message(self, message):

        if self.target.is_under_monitoring(message.author.id):

            if message.attachments:

                for attachment in message.attachments:
                    try:
                        await self._send_img_message(
                            attachment.proxy_url,
                            'users/{}_{}'.format(str(message.author.id), str(message.author)),  # user folder name
                            str('{}_{}'.format(message.created_at, message.author)),  # file name
                            str(attachment.proxy_url.split('/')[-1].split('.')[-1]),  # file extension
                            observers=MESSAGE_UPDATE
                        )
                    except Exception as e:
                        print(e)
                        pass

    async def on_member_update(self, before, after):
        if self.target.is_under_monitoring(after.id):

            if str(before.status) != "offline" and str(after.status) == "offline":
                if not self.target.changes_in_last_member_update(after.status):
                    return
                action = '{} has gone {}.'.format(after.name, after.status)
            elif str(before.status) != str(after.status):
                if not self.target.changes_in_last_member_update(after.status):
                    return
                action = '{} has gone {}.'.format(after.name, after.status)
            else:
                return

            await self._send_action_message(action, observers=MEMBER_UPDATE)

    async def on_voice_state_update(self, member, before, after):

        if self.target.is_under_monitoring(member.id):
            if after.channel is not None:
                if not self.target.changes_in_last_voice_state_update(after.channel):
                    return
                action = '{} è appena entrato nel calale vocale {} nella gilda {}.'\
                    .format(member.name, after.channel, member.guild)
            elif before.channel != after.channel:
                if not self.target.changes_in_last_voice_state_update(after.channel):
                    return
                action = '{} si è appena disconnesso dal calale vocale {} nella gilda {}.'\
                    .format(member.name, before.channel, member.guild)
            else:
                return

            await self._send_action_message(action, observers=VOICE_STATUS_UPDATED)

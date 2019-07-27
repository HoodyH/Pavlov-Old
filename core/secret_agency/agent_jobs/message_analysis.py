import asyncio

class MessageAnalysis(object):

    async def _send_img_message(self, url, path, file_name, file_type, *args, **kwargs):

        buffer_reader = await download_file_on_disc(url, path, file_name, file_type)

        caption = 'Undercover agent find this on discord.\n{}'
        caption = caption.format(file_name)
        await self._send_message(buffer_reader, telegram_bot_abstraction.send_image, caption=caption, *args, **kwargs)

    async def is_attachments_from_target(self, message):

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
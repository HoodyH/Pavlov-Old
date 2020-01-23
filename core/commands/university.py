import os
import sys
import io
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

from core.src.settings import (
    MSG_ON_SAME_CHAT
)


class University:

    def __init__(self, bot, language, command, arg, params, *args, **kwargs):

        self.bot = bot
        self.language = language

        self.arg = arg

        # parameter handed
        self._f = None
        self._exam_mode = None

        _vars = ['el', 'exam_mode']
        for param in params:
            name = '_{}'.format(param[0])
            setattr(self, name, param[1])

        # class data
        google_auth = GoogleAuth()
        google_auth.LocalWebserverAuth()
        self.drive = GoogleDrive(google_auth)

        self.file_list = None

        self.file_path = 'data_global/university/file'
        self.exam_mode_name = 'exam_mode.txt'
        self.folder_drive_type = 'drive#file'
        self.query_str = "'{}' in parents and trashed=false"

    def __get_file_list(self, query_set):

        query = {'q': self.query_str.format('root')}
        files = self.drive.ListFile(query).GetList()

        while query_set:
            next_file_name = query_set.pop(0)
            for file in files:
                file_name = file.get('title')
                if file_name == next_file_name:
                    query = {'q': self.query_str.format(file.get('id'))}

            files = self.drive.ListFile(query).GetList()

        self.file_list = files

    def __download_file(self):
        for file in self.file_list:
            file_name = file['title']
            file.GetContentFile(self.file_path)
            self.bot.send_file(open(self.file_path, 'rb'), MSG_ON_SAME_CHAT, filename=file_name)

    def __get_exam_mode(self):
        for file in self.file_list:
            file_name = file['title']
            if file_name == self.exam_mode_name:
                out = '**Modalità D\'esame:**\n\n'
                out += file.GetContentString(self.file_path)
                self.bot.send_message(out, MSG_ON_SAME_CHAT)

    def __get_dir_names(self):
        out = ''
        for file in self.file_list:
            if file['kind'] == self.folder_drive_type and file['title'] != self.exam_mode_name:
                out += '{}\n'.format(file['title'])
        return out

    def university(self):

        if not self.arg:
            self.__get_file_list([])
            out = 'Devi specificare come argomento un **CORSO** tra i seguenti.\n\n'
            out += self.__get_dir_names()
            out += '\n**.uni CORSO**\nPer accedere ai contenuti.\n\n'.format(self.arg)

            self.bot.send_message(out, MSG_ON_SAME_CHAT, parse_mode_en=True)
            return

        if self._exam_mode is not None:
            self.__get_file_list([self.arg])
            self.__get_exam_mode()
            return

        if not self._f:
            self.__get_file_list([self.arg])
            dir_names = self.__get_dir_names()

            if dir_names:
                out = 'Devi scegliere una delle seguenti **sottocartelle** di {} a cui accedere.\n\n'.format(self.arg)
                out += dir_names
                out += '\n**.uni {} -f sottocartela**\nPer accedere ai suoi contenuti.\n\n'.format(self.arg)
            else:
                out = 'La cartella {} non ha contenuti\n'.format(self.arg)
                out += '\n**.uni**\nPer vedere l\'elenco dei corsi.'.format(self.arg)

            self.bot.send_message(out, MSG_ON_SAME_CHAT, parse_mode_en=True)
            return

        query_set = [self.arg, self._f]
        self.__get_file_list(query_set)
        self.__download_file()

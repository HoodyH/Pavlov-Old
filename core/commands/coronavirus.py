from datetime import datetime, timedelta
from io import BytesIO
import requests
from bs4 import BeautifulSoup
from core.src.settings import (
    MSG_ON_SAME_CHAT
)
import matplotlib.pyplot as plt
from pvlv_database import DataCommands


class Coronavirus(object):

    def __init__(self, bot, language, command, arg, params):

        self.bot = bot
        self.language = language
        self.command = command

        self.arg = arg

        self._sort = None
        self._plot = None

        for param in params:
            name = '_{}'.format(param[0])
            setattr(self, name, param[1])

        # Counters for total data
        self.total_cases = 0
        self.total_new_cases = 0
        self.total_deaths = 0
        self.total_new_deaths = 0
        self.total_recovered = 0
        self.total_critical_cases = 0

        self.data = {}

        self.db = DataCommands()
        self.data_db = self.db.get_command_data('coronavirus')

    def __add_data(self, data, rank):

        if len(data) < 8:
            return

        county = data[0].lower()
        date = datetime.utcnow()
        cases = data[1]
        new_cases = data[2]
        deaths = data[3]
        new_deaths = data[4]
        recovered = data[5]
        critical_cases = data[6]
        continent = data[7]

        self.data[county] = {
            'rank': rank,
            'date': date,
            'cases': cases,
            'new_cases': new_cases,
            'deaths': deaths,
            'new_deaths': new_deaths,
            'recovered': recovered,
            'critical_cases': critical_cases,
            'continent': continent,
        }

        self.total_cases += cases
        self.total_new_cases += new_cases
        self.total_deaths += deaths
        self.total_new_deaths += new_deaths
        self.total_recovered += recovered
        self.total_critical_cases += critical_cases

    def __web_scrapper(self):

        url = 'https://www.worldometers.info/coronavirus/'

        res = requests.get(url)
        page = BeautifulSoup(res.content, 'html.parser')

        row_counter = 0
        for row in page.find(id='main_table_countries').find_all_next('tr'):
            row_data = []
            elements = row.find_all('td')
            for el in elements:
                try:
                    row_data.append(int(el.text.replace(',', '')))
                except ValueError:
                    text = el.text.replace(' ', '')
                    row_data.append(text if text != '' else 0)
            self.__add_data(row_data, row_counter)
            row_counter += 1

    @staticmethod
    def __calculate_death_percentage(confirmed, deaths):
        if confirmed is 0:
            deathly_percentage = 0
        else:
            deathly_percentage = deaths / confirmed * 100 if deaths is not 0 else 0

        return str(deathly_percentage)[:4]

    def __build_country(self, country):
        d = self.data.get(country)

        rank = d.get('rank')
        # date = d.get('date')
        cases = d.get('cases')
        new_cases = d.get('new_cases')
        deaths = d.get('deaths')
        new_deaths = d.get('new_deaths')
        recovered = d.get('recovered')
        critical_cases = d.get('critical_cases')
        continent = d.get('continent')

        out = '**#{} {} - {}**\n'.format(rank, country.upper(), continent)

        # out += 'Ultimo aggiornamento: {}\n'.format(date)
        out += 'Infetti: **{}** - nuovi: **{}**\n'.format(cases, new_cases)
        out += 'Morti: **{}** - nuovi: **{}**\n'.format(deaths, new_deaths)
        out += 'Guariti: **{}**\n'.format(recovered)
        out += 'Casi Critici: **{}**\n'.format(critical_cases)

        deathly_percentage = self.__calculate_death_percentage(cases, deaths)
        out += 'Mortalità attuale: **{}%**\n\n'.format(str(deathly_percentage)[:5])
        return out

    def __build_country_list(self, sort_key, show_data=True):
        _sorted = sorted(self.data.items(), key=lambda x: x[1][sort_key], reverse=True)

        if show_data:
            out_str = '**#{} {}**, {}: {}\n'
        else:
            out_str = '**#{} {}**\n'

        out = ''
        for i, el in enumerate(_sorted):
            out += out_str.format(
                i+1,
                el[0].upper(),
                sort_key,
                self.data[el[0]][sort_key],
            )

        return out

    @staticmethod
    def __timestamp_conversion(timestamp):
        return datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S')

    def __format_data(self, country):
        try:
            data = self.data_db[country]

            formatted_data = [[], [], []]

            timestamps = list(data.keys())

            prev_timestamp = timestamps.pop(0)
            first_timestamp = self.__timestamp_conversion(prev_timestamp)
            timestamp_cursor = first_timestamp

            for timestamp_str in timestamps:

                while timestamp_cursor < self.__timestamp_conversion(timestamp_str):

                    timestamp_cursor += timedelta(days=1)
                    formatted_data[0].append(int(data[prev_timestamp].get('cases')))
                    formatted_data[1].append(int(data[prev_timestamp].get('deaths')))
                    formatted_data[2].append(int(data[prev_timestamp].get('recovered')))

                prev_timestamp = timestamp_str

            # load the last timestamp data
            formatted_data[0].append(int(data[timestamps[-1]].get('cases')))
            formatted_data[1].append(int(data[timestamps[-1]].get('deaths')))
            formatted_data[2].append(int(data[timestamps[-1]].get('recovered')))

            # return: [start - end], formatted data
            start = first_timestamp.strftime('%d-%m-%Y')
            stop = self.__timestamp_conversion(timestamps[-1]).strftime('%d-%m-%Y')
            return [start, stop], formatted_data

        except Exception as exc:
            print(exc)
            return '', []

    def __build_plot(self, country):

        data_range, formatted_data = self.__format_data(country)

        fig, ax = plt.subplots()
        ax.plot(formatted_data[0], '.-', color='#aa0504', alpha=0.7, label='Infected')
        ax.plot(formatted_data[1], '.-', color='#110000', alpha=0.7, label='Deaths')
        ax.plot(formatted_data[2], '.-', color='#087800', alpha=0.7, label='Recovered')
        plt.grid(axis='y', alpha=0.75)

        legend = ax.legend(loc='upper center', shadow=True, fontsize='x-large')
        legend.get_frame()

        plt.title('Number of Infected People in {}'.format(country))
        plt.ylabel('Infected / Death / Recovered value'.format(country))
        plt.xlabel('Day Zero: {} - Last update: {}'.format(data_range[0], data_range[1]))

        img_bytes = BytesIO()
        plt.savefig(img_bytes)
        img_bytes.seek(0)

        self.bot.send_image(img_bytes, MSG_ON_SAME_CHAT)

    def void_arg(self):

        out = '**Coronavirus Update**\n\n'
        out += 'Da dove vengono presi i dati:\n'
        out += 'https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6\n'
        out += 'https://www.worldometers.info/coronavirus/\n\n'
        out += 'Totale Infetti: **{}**\n'.format(self.total_cases)
        out += 'Nuovi Infetti: **{}**\n'.format(self.total_new_cases)
        out += 'Totale Morti: **{}**\n'.format(self.total_deaths)
        out += 'Nuovi Morti: **{}**\n'.format(self.total_new_deaths)
        out += 'Totale Guariti: **{}**\n'.format(self.total_recovered)
        out += 'Casi Critici: **{}**\n'.format(self.total_critical_cases)

        deathly_percentage = self.__calculate_death_percentage(self.total_cases, self.total_deaths)
        out += 'La mortalità attuale è del **{}%**'.format(str(deathly_percentage)[:5])

        self.bot.send_message(out, MSG_ON_SAME_CHAT, parse_mode_en=True)

        # countries to stamp data
        my_country = ['italy']
        out = ''
        for country in my_country:
            self.__build_plot(country)
            out += self.__build_country(country)

        self.bot.send_message(out, MSG_ON_SAME_CHAT, parse_mode_en=True)

    def custom_country(self, country):
        try:
            out = self.__build_country(country)
            self.bot.send_message(out, MSG_ON_SAME_CHAT, parse_mode_en=True)
        except Exception as exc:
            print(exc)
            out = 'Nome della nazione non trovato. Usa uno tra questi:\n'
            out += self.__build_country_list('cases', show_data=False)
            self.bot.send_message(out, MSG_ON_SAME_CHAT, parse_mode_en=True)
        try:
            self.__build_plot(country)
        except Exception as exc:
            print(exc)
            out = 'Non c\'è lo storico di questa nazione a database per costruire il grafico,' \
                  'o è salvata sotto altro nome.\nProva con .conv -plot NomeNazione per avere più informazioni'
            self.bot.send_message(out, MSG_ON_SAME_CHAT, parse_mode_en=True)

    def run(self):

        self.__web_scrapper()

        if self._plot:
            try:
                self.__build_plot(self._plot.lower())
            except Exception as exc:
                print(exc)
                out = 'Scegli uno di questi continenti e riprova:\n'
                data_db = list(self.data_db.keys())
                data_db.pop(0)
                for i, el in enumerate(data_db):
                    out += '**#{} {}**\n'.format(
                        i + 1,
                        el.upper(),
                    )
                self.bot.send_message(out, MSG_ON_SAME_CHAT, parse_mode_en=True)
            return

        try:
            if self._sort.lower() == ('c' or 'confirmed' or 'infetti'):
                self.bot.send_message(self.__build_country_list('cases'), MSG_ON_SAME_CHAT, parse_mode_en=True)
                return

            if self._sort.lower() == ('r' or 'recovered' or 'guariti'):
                self.bot.send_message(self.__build_country_list('recovered'), MSG_ON_SAME_CHAT, parse_mode_en=True)
                return

            if self._sort.lower() == ('d' or 'deaths' or 'morti'):
                self.bot.send_message(self.__build_country_list('deaths'), MSG_ON_SAME_CHAT, parse_mode_en=True)
                return

        except AttributeError:
            pass

        chose = {
            '': self.void_arg,
        }
        try:
            chose[self.arg]()
        except KeyError:
            self.custom_country(self.arg.lower())

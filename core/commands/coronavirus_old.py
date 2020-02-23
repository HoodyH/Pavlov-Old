import json
import requests
from datetime import datetime
from core.src.settings import (
    MSG_ON_SAME_CHAT
)


class Coronavirus(object):

    def __init__(self, bot, language, command, arg, params):

        self.bot = bot
        self.language = language
        self.command = command

        self.arg = arg

        self._sort = None
        _vars = ['_sort']
        for param in params:
            name = '_{}'.format(param[0])
            setattr(self, name, param[1])

        self.total_confirmed = 0
        self.total_recovered = 0
        self.total_deaths = 0

        self.country_data = {}

    def __sort_by_rank(self, rank_name, sort_key):

        _sorted = sorted(self.country_data.items(), key=lambda x: x[1][sort_key], reverse=True)
        for i, el in enumerate(_sorted):
            self.country_data[el[0]][rank_name] = i

    def __web_scrapper(self):

        section = 'services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/ncov_cases/FeatureServer/1/'
        query = 'where=Confirmed%20%3E%200&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*'
        order_by = 'orderByFields=Confirmed%20desc%2CCountry_Region%20asc%2CProvince_State%20asc&outSR=102100'
        url = 'https://{}query?f=json&{}&{}'.format(
            section,
            query,
            order_by,
        )

        content = requests.get(url).content
        json_data = json.loads(content)

        # get the main object
        data_list = json_data.get('features')

        for data in data_list:
            report = data.get('attributes')

            county = report.get('Country_Region').lower()
            date = datetime.fromtimestamp(report.get('Last_Update') / 1e3)
            confirmed = report.get('Confirmed')
            recovered = report.get('Recovered')
            deaths = report.get('Deaths')

            self.total_confirmed += confirmed
            self.total_recovered += recovered
            self.total_deaths += deaths

            # create or update for sub zones
            try:
                d = self.country_data[county]
                d['date'] = date
                d['confirmed'] += confirmed
                d['recovered'] += recovered
                d['deaths'] += deaths
                self.country_data[county] = d

            except KeyError:
                self.country_data[county] = {
                    'date': date,
                    'confirmed': confirmed,
                    'recovered': recovered,
                    'deaths': deaths,
                }

        self.__sort_by_rank('rank_by_confirmed', 'confirmed')

    @staticmethod
    def __calculate_death_percentage(confirmed, deaths):
        if confirmed is 0:
            deathly_percentage = 0
        else:
            deathly_percentage = deaths / confirmed * 100 if deaths is not 0 else 0

        return str(deathly_percentage)[:4]

    def __build_country(self, country):
        try:
            d = self.country_data.get(country)
            if d:
                date = d.get('date').strftime("%H:%M %d-%m-%Y")
                confirmed = d.get('confirmed')
                rank_by_confirmed = d.get('rank_by_confirmed')
                recovered = d.get('recovered')
                deaths = d.get('deaths')

                out = '**#{} {}**\n'.format(rank_by_confirmed+1, country.upper())

                out += 'Ultimo aggiornamento: {}\n'.format(date)
                out += 'Infetti: {}\n'.format(confirmed)
                out += 'Morti: {}\n'.format(deaths)
                out += 'Guariti: {}\n'.format(recovered)

                deathly_percentage = self.__calculate_death_percentage(confirmed, deaths)
                out += 'Mortalità attuale: {}%\n\n'.format(str(deathly_percentage)[:5])
                return out
            else:
                return ''
        except Exception as e:
            print(e)
            return ''

    def __build_country_list(self, sort_key):
        print(self.country_data.items())
        _sorted = sorted(self.country_data.items(), key=lambda x: x[1][sort_key], reverse=True)

        out = ''
        for i, el in enumerate(_sorted):
            print(el)
            out += '**#{} {}**, {}: {}\n'.format(
                i+1,
                el[0].upper(),
                sort_key,
                self.country_data[el[0]][sort_key],
            )

        return out

    def void_arg(self):

        out = '**Coronavirus Update**\n\n'
        out += 'Da dove vengono presi i dati:\n'
        out += 'https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6\n\n'
        out += 'Totale Infetti: {}\n'.format(self.total_confirmed)
        out += 'Totale Morti: {}\n'.format(self.total_deaths)
        out += 'Totale Guariti: {}\n'.format(self.total_recovered)

        deathly_percentage = self.__calculate_death_percentage(self.total_confirmed, self.total_deaths)
        out += 'La mortalità attuale è del {}%'.format(str(deathly_percentage)[:5])

        self.bot.send_message(out, MSG_ON_SAME_CHAT, parse_mode_en=True)

        # countries to stamp data
        my_country = ['italy', 'japan']
        out = ''
        for country in my_country:
            out += self.__build_country(country)
        self.bot.send_message(out, MSG_ON_SAME_CHAT, parse_mode_en=True)

    def custom_country(self, country):
        out = self.__build_country(country)
        self.bot.send_message(out, MSG_ON_SAME_CHAT, parse_mode_en=True)

    def run(self):

        self.__web_scrapper()

        try:
            if self._sort.lower() == ('c' or 'confirmed' or 'infetti'):
                self.bot.send_message(self.__build_country_list('confirmed'), MSG_ON_SAME_CHAT, parse_mode_en=True)
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



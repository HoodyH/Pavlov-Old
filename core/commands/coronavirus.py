import json
import os
import sys
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from core.src.settings import (
    MSG_ON_SAME_CHAT
)
from core.src.static_modules import db


class Coronavirus(object):

    def __init__(self, bot, language, command, arg, params):

        self.bot = bot
        self.language = language
        self.command = command

        self.arg = arg

        self.total_confirmed = 0
        self.total_recovered = 0
        self.total_deaths = 0

        self.country_data = {}

    def web_scrapper(self):

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

            county = report.get('Country_Region')
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

    def void_arg(self):

        self.web_scrapper()

        out = '**Coronavirus Update**\n\n'
        out += 'Da dove vengono presi i dati:\n'
        out += 'https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6\n\n'
        out += 'Totale Confermati: {}\n'.format(self.total_confirmed)
        out += 'Totale Morti: {}\n'.format(self.total_deaths)
        out += 'Totale Guariti: {}\n'.format(self.total_recovered)

        deathly_percentage = self.total_deaths / self.total_recovered * 100
        out += 'La mortalità attuale è del {}%'.format(str(deathly_percentage)[:5])

        self.bot.send_message(out, MSG_ON_SAME_CHAT, parse_mode_en=True)

        # countries to stamp data
        my_country = ['Mainland China', 'Italy', 'Japan', 'South Korea']
        for country in my_country:
            out = '**{}**\n\n'.format(country)
            d = self.country_data.get(country)
            if d:
                confirmed = d.get('confirmed')
                recovered = d.get('recovered')
                deaths = d.get('deaths')

                out += 'Confermati: {}\n'.format(confirmed)
                out += 'Morti: {}\n'.format(recovered)
                out += 'Guariti: {}\n'.format(deaths)

                deathly_percentage = deaths / recovered * 100 if deaths is not 0 else 0
                out += 'La mortalità attuale è del {}%'.format(str(deathly_percentage)[:5])

                self.bot.send_message(out, MSG_ON_SAME_CHAT, parse_mode_en=True)

    def run(self):

        chose = {
            '': self.void_arg,
        }

        chose[self.arg]()

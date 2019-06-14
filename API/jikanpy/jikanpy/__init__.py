import requests

session: requests.Session = requests.Session()

from API.jikanpy.jikanpy.jikan import Jikan
from API.jikanpy.jikanpy.aiojikan import AioJikan
from API.jikanpy.jikanpy.exceptions import *

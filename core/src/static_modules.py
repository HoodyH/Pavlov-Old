# API
from API.badass_character.badass_character import BadassCharacter
from API.bestemmia.bestemmia import Bestemmia
from API.pickup_line.pickup_line import PickupLine

# Database
from core.db.database import DB


# API
badass_character = BadassCharacter()
bestemmia = Bestemmia()
pickup_line = PickupLine()

# Database
db = DB('mongodb+srv://MainUserBot:AdminDb12@abot-3jqai.mongodb.net/test?retryWrites=true')

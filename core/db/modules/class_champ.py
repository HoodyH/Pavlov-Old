class ChampField(object):

    def __init__(self):

        self.level = 0
        self.xp = 0
        self.main_class = 0
        self.ability = []

        self.hp_points = 100
        self.hp_max = 100
        self.mana_points = 100
        self.mana_max = 100
        self.stamina = 100
        self.stamina_max = 100

    def extract_data(self, raw_data):
        self.level = raw_data.get('level', self.level)
        self.xp = raw_data.get('xp', self.xp)
        self.main_class = raw_data.get('main_class', self.main_class)
        self.ability = raw_data.get('ability', self.ability)

        self.hp_points = raw_data.get('hp_points', self.hp_points)
        self.hp_max = raw_data.get('hp_max', self.hp_max)
        self.mana_points = raw_data.get('mana_points', self.mana_points)
        self.mana_max = raw_data.get('mana_max', self.mana_max)
        self.stamina = raw_data.get('stamina', self.stamina)
        self.stamina_max = raw_data.get('stamina_max', self.stamina_max)

        return self

    def build_data(self):

        data_out = {
            'level': self.level,
            'xp': self.xp,
            'main_class': self.main_class,
            'ability': self.ability,

            'hp_points': self.hp_points,
            'hp_max': self.hp_max,
            'mana_points': self.mana_points,
            'mana_max': self.mana_max,
            'stamina': self.stamina,
            'stamina_max': self.stamina_max,
        }

        return data_out

    # level
    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, value):
        self.__level = value

    # xp
    @property
    def xp(self):
        return self.__xp

    @xp.setter
    def xp(self, value):
        self.__xp = value

    # main_class
    def get_main_class(self):
        return self.main_class

    def set_main_class(self, main_class):
        self.main_class = main_class

    # ability
    def get_ability(self):
        return self.ability

    def set_ability(self, ability):
        self.ability = ability

    # hp_points
    def get_hp_points(self):
        return self.hp_points

    def set_hp_points(self, hp_points):
        self.hp_points = hp_points

    # hp_max
    def get_hp_max(self):
        return self.hp_max

    def set_hp_max(self, hp_max):
        self.hp_max = hp_max

    # mana_points
    def get_mana_points(self):
        return self.mana_points

    def set_(self, mana_points):
        self.mana_points = mana_points

    # mana_max
    def get_mana_max(self):
        return self.mana_max

    def set_mana_max(self, mana_max):
        self.mana_max = mana_max

    # stamina
    def get_stamina(self):
        return self.stamina

    def set_stamina(self, stamina):
        self.stamina = stamina

    # stamina_max
    def get_stamina_max(self):
        return self.stamina_max

    def set_stamina_max(self, stamina_max):
        self.stamina_max = stamina_max







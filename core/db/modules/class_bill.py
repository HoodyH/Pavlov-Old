class BillField(object):

    def __init__(self):

        self.bits = 10
        self.last_bit_farm = None

        self.debit = []
        self.credit = []
        self.spent = 0
        self.given = 0

    def extract_data(self, raw_data):
        self.bits = raw_data.get('bits', self.bits)
        self.last_bit_farm = raw_data.get('last_bit_farm', self.last_bit_farm)

        return self

    def build_data(self):

        data_out = {
            'bits': self.bits,
            'last_bit_farm': self.last_bit_farm
        }

        return data_out

    # bits
    @property
    def bits(self):
        return self.__bits

    @bits.setter
    def bits(self, value):
        self.__bits = value

    # last_bit_farm
    @property
    def last_bit_farm(self):
        return self.__last_bit_farm

    @last_bit_farm.setter
    def last_bit_farm(self, value):
        self.__last_bit_farm = value

    # debit
    @property
    def debit(self):
        return self.__debit

    @debit.setter
    def debit(self, value):
        self.__debit = value

    # credit
    @property
    def credit(self):
        return self.__credit

    @credit.setter
    def credit(self, value):
        self.__credit = value

    # spent
    @property
    def spent(self):
        return self.__spent

    @spent.setter
    def spent(self, value):
        self.__spent = value

    # given
    @property
    def given(self):
        return self.__given

    @given.setter
    def given(self, value):
        self.__given = value

from datetime import timedelta


class CommandUseLog(object):

    def __init__(self):
        self.__log_time_by_hour = []
        self.__by_hour = []

        self.__log_time_by_day = []
        self.__by_day = []

        self.__log_time_by_month = []
        self.__by_month = []

        self.__total_count = 0

    def extract_data(self, raw_data):
        self.log_time_by_hour = raw_data.get('log_time_by_hour', self.log_time_by_hour)
        self.by_hour = raw_data.get('by_hour', self.by_hour)

        self.log_time_by_day = raw_data.get('log_time_by_day', self.log_time_by_day)
        self.by_day = raw_data.get('by_day', self.by_day)

        self.log_time_by_month = raw_data.get('log_time_by_month', self.log_time_by_month)
        self.by_month = raw_data.get('by_month', self.by_month)

        self.total_count = raw_data.get('total_count', self.total_count)

        return self

    def build_data(self):
        data_out = {
            'log_time_by_hour': self.log_time_by_hour,
            'by_hour': self.by_hour,

            'log_time_by_day': self.log_time_by_day,
            'by_day': self.by_day,

            'log_time_by_month': self.log_time_by_month,
            'by_month': self.by_month,

            'total_count': self.total_count,
        }

        return data_out

    def increment_command_interactions(self, datetime_log):

        for scope in ['hour', 'day', 'month']:

            """
            Genera la time stamp da loggare in base al tipo di log richiesto
            E salva in una variabile generica i dati da utilizzare sucessivamente.
            """
            if scope == 'hour':
                time = datetime_log.replace(minute=0, second=0, microsecond=0)
                max_len = 72
                log_time_by_scope = self.log_time_by_hour
                by_scope = self.by_hour
            elif scope == 'day':
                time = datetime_log.replace(hour=0, minute=0, second=0, microsecond=0)
                max_len = 90
                log_time_by_scope = self.log_time_by_day
                by_scope = self.by_day
            elif scope == 'month':
                time = datetime_log
                max_len = 120
                log_time_by_scope = self.log_time_by_month
                by_scope = self.by_month
            else:
                return

            """
            Controlla se gli array hanno raggiunto la dimensione massima per il log dei dati.
            Se si fa il pop dell'ultimo elemento, quello temporalmente più distante
            """
            try:
                db_timestamp = log_time_by_scope[0]
                if len(log_time_by_scope) > max_len:
                    log_time_by_scope.pop()
                if len(by_scope) > max_len:
                    by_scope.pop()
            except IndexError:
                db_timestamp = time
                log_time_by_scope.append(time)

            """
            Controlla se si trova ancora nella stessa ora.
            In tal caso è solo necessatio fare un add ai dati giè esistenti
            """
            if scope == 'hour':
                sub = time - db_timestamp
                condition = sub >= timedelta(hours=1)
            elif scope == 'day':
                sub = time - db_timestamp
                condition = sub >= timedelta(days=1)
            else:
                condition = time.month > db_timestamp.month or (time.month == 1 and db_timestamp.month == 12)

            if condition:
                log_time_by_scope.insert(0, time)
                by_scope.insert(0, 1)
            else:
                try:
                    by_scope[0] += 1
                except IndexError:
                    by_scope.append(1)

            """
            Salava i dati elaborati nelle rispettive variabili finali
            """
            if scope == 'hour':
                self.log_time_by_hour = log_time_by_scope
                self.by_hour = by_scope
            elif scope == 'day':
                self.log_time_by_day = log_time_by_scope
                self.by_day = by_scope
            elif scope == 'month':
                self.log_time_by_month = log_time_by_scope
                self.by_month = by_scope

        # Incrementa il total count per il comando. Questa variabile tiene conto dell'utilizzo complessimo
        self.total_count += 1

    # log_time_by_hour
    @property
    def log_time_by_hour(self):
        return self.__log_time_by_hour

    @log_time_by_hour.setter
    def log_time_by_hour(self, value):
        self.__log_time_by_hour = value

    # by_hour
    @property
    def by_hour(self):
        return self.__by_hour

    @by_hour.setter
    def by_hour(self, value):
        self.__by_hour = value

    # log_time_by_day
    @property
    def log_time_by_day(self):
        return self.__log_time_by_day

    @log_time_by_day.setter
    def log_time_by_day(self, value):
        self.__log_time_by_day = value

    # by_day
    @property
    def by_day(self):
        return self.__by_day

    @by_day.setter
    def by_day(self, value):
        self.__by_day = value

    # log_time_by_month
    @property
    def log_time_by_month(self):
        return self.__log_time_by_month

    @log_time_by_month.setter
    def log_time_by_month(self, value):
        self.__log_time_by_month = value

    # by_month
    @property
    def by_month(self):
        return self.__by_month

    @by_month.setter
    def by_month(self, value):
        self.__by_month = value

    # _commands
    @property
    def total_count(self):
        return self.__total_count

    @total_count.setter
    def total_count(self, value):
        self.__total_count = value


class CommandField(object):

    def extract_data(self, raw_data):

        try:
            for key in raw_data.keys():
                setattr(
                    self, key,
                    CommandUseLog().extract_data(raw_data.get(key, CommandUseLog().build_data()))
                )
        except Exception as exc:
            print('New User used Commands, db creation exception (accepted): ' + str(exc))
            pass

        return self

    def build_data(self):
        data_out = {}
        attrs = self.__dict__
        for key in attrs.keys():
            data_out[key] = attrs.get(key).build_data()

        return data_out

    def get_command_interactions(self, command_name):
        command_name = command_name.replace('.', '_')
        if command_name.replace('.', '_') in self.__dict__.keys():
            command_use_log = getattr(self, command_name)
            return command_use_log.total_count

    def increment_command_interactions(self, command_name, datetime_log):
        command_name = command_name.replace('.', '_')
        if command_name in self.__dict__.keys():
            command_use_log = getattr(self, command_name)
            command_use_log.increment_command_interactions(datetime_log)

        else:
            setattr(
                self,
                command_name,
                CommandUseLog()
            )

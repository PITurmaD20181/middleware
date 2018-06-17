from datetime import datetime

class Present:
    MATRICULA_SIZE = 9
    DATE_FORMAT = '%a %b %d %H:%M:%S %Y'

    def __init__(self, matricula, date):
        assert(len(matricula) == Present.MATRICULA_SIZE)
        assert(isinstance(date, datetime))

        self.matricula = matricula
        self.date = date

    def __str__(self):
        return 'registration: {}, date_time: {}'.format(self.matricula, self.date)

    def as_dict(self):
        d = dict()
        d['registration'] = str(self.matricula)
        d['date_time'] = str(self.date)
        return d


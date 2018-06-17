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
        return 'Matricula: ({}), Data: ({})'.format(self.matricula, self.date)

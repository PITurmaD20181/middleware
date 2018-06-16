chamada_file_name = 'Chamada.txt'

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

class Parser:

    def __init__(self, lines):

        self._process_lines(lines)

    def create_tuple(self, matricula, date):
        date_time = datetime.strptime(date, Present.DATE_FORMAT)
        tup = (matricula, date_time)
        self.tuples.append(tup)
        pass

    def get_tuples(self):
        return self.tuples

    def _process_lines(self, lines):
        assert(isinstance(lines, list))
        self.tuples = list()

        for line in lines:
            if line == '\n':
                print('Skipping blank line')
            else:
                self._process_line(line)

    def _process_line(self, line):
        assert(isinstance(line, str))
        EXPECTED_LINE_SIZE = 35
        assert(len(line) == EXPECTED_LINE_SIZE)

        line = line.strip()

        matricula = line[:Present.MATRICULA_SIZE].strip()
        date = line[Present.MATRICULA_SIZE:].strip()
        self.create_tuple(matricula, date)


if __name__ == '__main__':
    try:
        with open(chamada_file_name, 'r') as chamada_file:
            print('File \'{}\' opened successfully.'.format(chamada_file_name))
            data = chamada_file.readlines()

            p = Parser(data)
            tuples = p.get_tuples()
            for t in tuples:
                present = Present(*t)
                print(present)

    except FileNotFoundError:
            print('Can\'t open file \'{}\' in the current directory.'.format(chamada_file_name))

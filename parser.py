from datetime import datetime
from present import Present

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

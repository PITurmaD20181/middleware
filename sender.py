from parser import Parser
from present import Present
from utils import debug


class Curl:

    def __init__(self, data):
        assert(isinstance(data, dict))
        assert(isinstance(url, str))

        items = []
        for item in data.items():
            key, value = item
            key = self.escape(key)
            value = self.escape(value)

            key_value = ': '.join([key, value])
            items.append(key_value)

        d = '"{'
        d += ', '.join(items)
        d += '}"'
        self.data = d

    def escape(self, s):
        return '\\"' + s + '\\"'

    def get_post_command(self, url):
        command = 'curl -X POST --header "Content-Type: application/json" -d'
        u = '"{}"'.format(url)
        post = ' '.join([command, self.data, u])
        return post

class Sender:

    @staticmethod
    def post_data(data):
        assert(isinstance(data, dict))

if __name__ == '__main__':
    from present import Present
    from datetime import datetime

    date = datetime.strptime('2018-06-15 02:51:14', '%Y-%m-%d %H:%M:%S')
    p = Present(matricula='150039921', date=date)

    data = p.as_dict()
    url = 'http://0.0.0.0:8000/frequency_lists/add_presence/'

    c = Curl(data)
    query = c.get_post_command(url)
    print(query)


from present import Present
from utils import debug
import requests


class Initial:
    url = 'http://localhost:8000/frequency_lists/inicialize_presences_list/'

    def __init__(self):
        pass

    def initialize_presences_list(self):
        
        return requests.get(url=Initial.url)

class Request:
    url = 'http://0.0.0.0:8000/frequency_lists/add_presence/'

    def __init__(self):
        pass

    def post_presence(self, present):
        assert(isinstance(present, Present))

        data = present.as_dict()
        response = requests.post(url=Request.url, data=data)
        return response

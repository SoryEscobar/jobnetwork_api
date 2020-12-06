import requests
from flask import jsonify

class Consumer():
   
    def __init__(self):
        self.response = None

    def get(self, url):
        self.response = requests.get(url)
        return self._request('GET')
        


    def post(self, url, data=None):
        self.response = requests.post(url, data)
        return self._request('POST')

    
    def _request(self, method='GET'):
        if self.response.status_code != 200:
            return 'Zordon, we couldn\'t bring the Morphin Power! \n We had an issue when processing your request: Error code: {}'.format(self.response.status_code)
        else:
            if method == 'GET':
                return self.response.json()
            if method == 'POST':
                return self.response.json()
            else:
                return 'Invalid Method, for now...'

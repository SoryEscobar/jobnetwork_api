import requests

class Consumer():
   
    def __init__(self):
        self.response = None

    def get(self, url):
        self.response = requests.get(url)
        return self._request()
        


    def post(self, url, data):
        self.response = requests.post(url, data)
        return self._request()

    
    def _request(self):
        if self.response.status_code != 200:
            return 'Zordon, we couldn\'t bring the Morphin Power! \n We had an issue when processing your request: Error code: {}'.format(self.response.status_code)
        else:
            return self.response.json()

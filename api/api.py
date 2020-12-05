from flask import Flask
from flask import request

from .utils.consume_torre_api import Consumer as csm



api = Flask(__name__)
api.debug = True


@api.route('/')
def home():
    return "The API is online"


#JOBs
@api.route('/job', methods=['GET', 'POST'])
def job_requests():
    if request.method == 'GET':
        #TODO:Change the request from
        #id = 'JdmAREdm-welocalize-ltd-japanese-language-lead-for-marketing-contents-15'
        #url = f'https://torre.co/api/opportunities/{id}'
        #return csm().get(url)
        return "TODO"


    if request.method == 'POST':
        #TODO: Do the request to the torre API here.
        return "TODO"
    



#Users
@api.route('/user', methods=['GET', 'POST'])
def user_requests():
    if request.method == 'GET':
        #TODO:Change the request from Sory Escobar to something else.
        id = 'soryescobar'
        url = f'https://torre.bio/api/bios/{id}'
        return csm().get(url)

    if request.method == 'POST':
        #TODO: Do the request to the torre API here.
        return "TODO"

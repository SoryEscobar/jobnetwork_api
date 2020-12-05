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
        #TODO: Make request ID dynamic
        id = 'JdmAREdm'
        url = f'https://torre.co/api/opportunities/{id}'
        return csm().get(url)


    if request.method == 'POST':
        url = 'https://search.torre.co/opportunities/_search/?'
        return csm().post(url)
    



#Users
@api.route('/user', methods=['GET', 'POST'])
def user_requests():
    if request.method == 'GET':
        #TODO: Make request ID dynamic
        id = 'soryescobar'
        url = f'https://torre.bio/api/bios/{id}'
        return csm().get(url)

    if request.method == 'POST':
        url = 'https://search.torre.co/people/_search/?'
        return csm().post(url)


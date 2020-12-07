from flask import Flask
from flask import request

from .utils.consume_torre_api import Consumer as csm
from .utils.user import User, response_to_users_converter
from flask import jsonify



api = Flask(__name__)
api.debug = True


@api.route('/')
def home():
    return "The API is online"


#JOBs
@api.route('/job/<jobid>', methods=['GET'])
def job_requests_get(jobid = None):

    if request.method == 'GET':
        url = f'https://torre.co/api/opportunities/{jobid}'
        return csm().get(url)

    else:
        return "Not supported Request"


@api.route('/job', methods=['POST'])
def job_requests_post():
    if request.method == 'POST':
        url = 'https://search.torre.co/opportunities/_search/?'
        return csm().post(url)
    
    else:
        return "Not supported Request"
    



#Users
@api.route('/user/<username>', methods=['GET'])
def user_requests_get(username = None):

    if request.method == 'GET':
        url = f'https://torre.bio/api/bios/{username}'
        return csm().get(url)

    else:
        return "Not supported Request"


@api.route('/user', methods=['POST'])
def user_requests_post():

    if request.method == 'POST':
        url = 'https://search.torre.co/people/_search/?'
        json_response = csm().post(url)
        #return response_to_users_converter(json_response)
        return json_response

    else:
        return "Not supported Request"

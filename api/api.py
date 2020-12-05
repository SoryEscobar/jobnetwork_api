from flask import Flask
from flask import request

import consume_torre_api

api = Flask(__name__)
api.debug = True


@api.route('/')
def home():
    return "The API is online"


#JOBs
@api.route('/job', methods=['GET', 'POST'])
def job_requests():
    if request.method == 'GET':
        #TODO: Do the request to the torre API here.
        return "TODO"

    if request.method == 'POST':
        #TODO: Do the request to the torre API here.
        return "TODO"
    



#Users
@api.route('/user', methods=['GET', 'POST'])
def user_requests():
    if request.method == 'GET':
        #TODO: Do the request to the torre API here.
        return "TODO"

    if request.method == 'POST':
        #TODO: Do the request to the torre API here.
        return "TODO"

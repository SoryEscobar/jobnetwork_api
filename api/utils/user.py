import json
from flask import jsonify

class User():

    def __init__(self, json_data):
        return None


def response_to_users_converter(response_data):

    users = response_data.get('results')
    return jsonify(users)

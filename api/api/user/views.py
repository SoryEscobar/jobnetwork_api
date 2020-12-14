from flask import Blueprint, request
from api.utils.consume_torre_api import Consumer as csm


users_blueprint = Blueprint('users', __name__)



@users_blueprint.route('/<username>', methods=['GET'])
def user_requests_get(username = None):

    if request.method == 'GET':
        url = f'https://torre.bio/api/bios/{username}'
        return csm().get(url)

    else:
        return "Not supported Request"


@users_blueprint.route('/', methods=['POST'])
def user_requests_post():

    if request.method == 'POST':
        url = 'https://search.torre.co/people/_search/?'
        json_response = csm().post(url)
        return json_response

    else:
        return "Not supported Request"

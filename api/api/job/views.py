from flask import Blueprint, request
from api.utils.consume_torre_api import Consumer as csm



jobs_blueprint = Blueprint('jobs',__name__)




@jobs_blueprint.route('/<jobid>', methods=['GET'])
def job_requests_get(jobid = None):

    if request.method == 'GET':
        url = f'https://torre.co/api/opportunities/{jobid}'
        return csm().get(url)

    else:
        return "Not supported Request"


@jobs_blueprint.route('/', methods=['POST'])
def job_requests_post():
    if request.method == 'POST':
        url = 'https://search.torre.co/opportunities/_search/?'
        return csm().post(url)
    
    else:
        return "Not supported Request"

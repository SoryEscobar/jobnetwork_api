from flask import Flask


api = Flask(__name__)


from api.user.views import users_blueprint
from api.job.views import jobs_blueprint


api.register_blueprint(users_blueprint, url_prefix='/users')
api.register_blueprint(jobs_blueprint, url_prefix='/jobs')


@api.route('/')
def index():
    return "The API is online"

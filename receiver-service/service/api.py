from flask import Blueprint
from flask_restplus import Api, Resource


blueprint_v1 = Blueprint('api-v1', __name__)
api_v1 = Api(
    blueprint_v1,
    version='1.0',
    title='Receiver Service',
    validate=True,
)


@api_v1.route('/info')
class InfoResource(Resource):

    def get(self):
        return {
            'Receiver': 'Cisco is the best!',
        }

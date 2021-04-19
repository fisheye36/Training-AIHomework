from contextlib import suppress

import requests
from flask import abort, Blueprint
from flask_restplus import Api, fields, Resource

from service import app


blueprint_v1 = Blueprint('api-v1', __name__)
api_v1 = Api(
    blueprint_v1,
    version='1.0',
    title='Ping Service',
    validate=True,
)

ping = api_v1.model('Ping', {
    'url': fields.String(required=True),
})


@api_v1.route('/ping')
class PingResource(Resource):

    @api_v1.expect(ping)
    def post(self):
        url = api_v1.payload['url']

        try:
            response = requests.get(url, timeout=app.config['REQUEST_TIMEOUT'])
        except requests.RequestException:
            abort(400, f"Cannot access URL at '{url}'")

        if response.headers['Content-Type'] == 'application/json':
            with suppress(ValueError):
                return response.json()

        return response.text

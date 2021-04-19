import requests
from flask import abort, Flask
from flask_restplus import Api, fields, Resource


app = Flask(__name__)
api = Api(app, validate=True)

app.config['REQUEST_TIMEOUT'] = 1.0

ping = api.model('Ping', {
    'url': fields.String(required=True),
})


@api.route('/api/v1/ping')
class PingResource(Resource):

    @api.expect(ping)
    def post(self):
        url = api.payload['url']
        try:
            response = requests.get(url, timeout=app.config['REQUEST_TIMEOUT'])
        except requests.RequestException:
            abort(400, f"Cannot access URL at '{url}'")
        else:
            return response.text


@api.route('/health')
class HealthResource(Resource):

    def get(self):
        return {
            'status': 'reachable'
        }


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask
from flask_restplus import Api, Resource


app = Flask(__name__)
api = Api(app)


@api.route('/api/v1/ping')
class PingResource(Resource):

    def post(self):
        return {'hello': 'world'}


if __name__ == '__main__':
    app.run(debug=True)

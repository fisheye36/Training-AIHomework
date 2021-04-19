from flask import Flask


app = Flask(__name__)
app.config['REQUEST_TIMEOUT'] = 1.0


@app.route('/health')
def health():
    return {
        'status': 'reachable'
    }


from service.api import blueprint_v1


app.register_blueprint(blueprint_v1, url_prefix='/api/v1')

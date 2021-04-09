""" Main API server

    REST API that runs on flask, default port is 5000
    You can modify this script while server is running, it will restart automatically once file is saved!

    Currently contains placeholders for future implementation

"""

import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

response_header = [
    {
        'id': 0,
        'api_version': 1,
        'operation': {
            'type': 'compose',
            'instruments': 5,
            'algorithm': 'musegan-v0',
            'description': 'Music generated from scratch'
            },
        'format': 'midi',
     },
]

@app.route('/', methods=['GET'])
def home():
    return "<h1>PLD SMART</h1><p>Welcome to PLD SMART API</p>"

@app.route('/api/v1/compose/polyphonic/musegan/v0', methods=['GET'])
def api_compose_polyphonic_musegan_v0():
    return jsonify(response_header)

@app.route('/api/v1/compose/monophonic/lstm/v0', methods=['GET'])
def api_compose_monophonic_lstm_v0():
    return jsonify(response_header)

@app.route('/api/v1/jam/polyphonic/musegan/v0', methods=['POST'])
def api_jam_polyphonic_musegan_v0():
    return jsonify(response_header)

@app.route('/api/v1/interpolate/polyphonic/vae/v0', methods=['POST'])
def api_interpolate_polyphonic_vae_v0():
    return jsonify(response_header)

@app.route('/api/v1/styling/polyphonic/vae/v0', methods=['POST'])
def api_styling_polyphonic_vae_v0():
    return jsonify(response_header)

app.run()
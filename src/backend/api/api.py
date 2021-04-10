""" Main API server

    REST API that runs on flask, default port is 5000
    You can modify this script while server is running, it will restart automatically once file is saved!

    Currently contains placeholders for future implementation

"""

import flask
from flask import request, jsonify, send_file, make_response
from icecream import ic
import time
import datetime

import __init__

from wrappers import logger
from algo.LSTM import predict as lstm

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
    logger.info("GET /") # our own log message (flask already has its own logging system)
    ic() # debug example
    return "<h1>PLD SMART</h1><p>Welcome to PLD SMART API</p>"

@app.route('/api/v1/compose/polyphonic/musegan/v0', methods=['GET'])
def api_compose_polyphonic_musegan_v0():
    logger.info("GET /api/v1/compose/polyphonic/musegan/v0")
    return jsonify(response_header)

@app.route('/api/v1/compose/monophonic/lstm/v0', methods=['GET'])
def api_compose_monophonic_lstm_v0():
    
    # Parameter parsing
    style = request.args.get('style')
    length = request.args.get('length')
    
    # Generate song
    start_time = time.time()
    output_file_path = lstm.generate(music_name = style, max_extra_notes = int(length)) 
    elapsed_time = time.time() - start_time
        
    # Response body
    midi_file = open(output_file_path, 'rb')
    response = make_response(send_file(midi_file, mimetype='audio/midi'))
    
    # Response header
    response.headers['operation'] = 'compose'
    response.headers['instruments'] = 1
    response.headers['algorithm'] = 'lstm-v0'
    response.headers['description'] = 'Monophonic music generated from scratch'
    response.headers['format'] = 'midi'
    response.headers['elapsedTime'] = elapsed_time
    response.headers['style'] = style
    response.headers['length'] = length
    response.headers['timestamp'] = datetime.datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S')
    response.headers['api_version'] = 1
    
    return response

@app.route('/api/v1/jam/polyphonic/musegan/v0', methods=['POST'])
def api_jam_polyphonic_musegan_v0():
    return jsonify(response_header)

@app.route('/api/v1/interpolate/polyphonic/vae/v0', methods=['POST'])
def api_interpolate_polyphonic_vae_v0():
    return jsonify(response_header)

@app.route('/api/v1/styling/polyphonic/vae/v0', methods=['POST'])
def api_styling_polyphonic_vae_v0():
    return jsonify(response_header)

if __name__ == "__main__":
    logger.log_config("src/backend/log/", "api")
    app.run()
from flask import Flask, jsonify, request
import data_retreiver
import available_stations

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return "<h1>Meteo-gr-api</h1><p>Get live meteorological data from various Greek stations.</p>"


@app.route('/api/data', methods=['GET'])
def api_station():
    if 'station' in request.args:
        print(request.args['station'])
        return jsonify(data_retreiver.get_data(station=request.args['station']))
    else:
        return "Error: No station provided. Please specify a station."


@app.route('/api/available_stations', methods=['GET'])
def api_available_stations():
    return jsonify(available_stations.get_stations())


if __name__ == '__main__':
    app.run()

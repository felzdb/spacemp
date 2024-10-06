from flask import Blueprint, jsonify, render_template
import requests

space_weather_bp = Blueprint('space_weather', __name__, template_folder='Templates')

# Defina sua chave de API aqui
API_KEY = 'krtHTpfgfbNy56GfF1n8CBgCdL5Okfg9Pv726TLT'  # Substitua pela sua chave de API

@space_weather_bp.route('/space_weather')
def space_weather():
    url = f'https://api.nasa.gov/planetary/apod?api_key={API_KEY}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return render_template('weather.html', data=data)
    else:
        return jsonify({"error": "Unable to fetch data"}), response.status_code

@space_weather_bp.route('/space_weather/data')
def space_weather_data():
    url = f'https://api.nasa.gov/planetary/apod?api_key={API_KEY}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return jsonify(data)
    else:
        return jsonify({"error": "Unable to fetch data"}), response.status_code

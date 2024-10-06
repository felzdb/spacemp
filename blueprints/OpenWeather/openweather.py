from flask import Blueprint, render_template, jsonify
import requests

openweather_bp = Blueprint('openweather', __name__, template_folder='Templates')

API_KEY = '94d84e5dff66fb4d5c74a3b6bb0f8f25'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

@openweather_bp.route('/map')
def map_view():
    return render_template('openmap.html')

@openweather_bp.route('/weather/<city>')
def get_weather(city):
    response = requests.get(f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric")
    return jsonify(response.json())

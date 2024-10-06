from flask import Blueprint, jsonify, render_template
import requests

earth_api_bp = Blueprint('earth_api', __name__, template_folder='Templates')

# Defina sua chave de API aqui
API_KEY = 'krtHTpfgfbNy56GfF1n8CBgCdL5Okfg9Pv726TLT'  # Substitua pela sua chave de API

@earth_api_bp.route('/earth_data')
def earth_data():
    url = f'https://api.nasa.gov/planetary/earth/assets?api_key={API_KEY}&lon=-100.0&lat=40.0&date=2020-01-01'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return render_template('earth_data.html', data=data)
    else:
        return jsonify({"error": "Unable to fetch data"}), response.status_code

import requests
import datetime
from flask import Blueprint, render_template, redirect

dash_temp_bp = Blueprint("dash_temp_menu", __name__, template_folder="templates")


api_weather= '94d84e5dff66fb4d5c74a3b6bb0f8f25'
city = 'caxias do sul'

url_coord = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={api_weather}"

# Fazendo a requisição para a API
response = requests.get(url_coord)

# Verifica se a requisição foi bem sucedida
if response.status_code == 200:
    data = response.json()
    
    if data:
        # Salvando os dados de lat e lon
        lat = data[0]['lat']
        lon = data[0]['lon']
        print(f"Latitude: {lat}, Longitude: {lon}")
    else:
        print("Nenhum dado encontrado para a cidade fornecida.")
else:
    print(f"Erro na requisição: {response.status_code}")

url_current = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={api_weather}&lang=pt_br"

# Fazendo a requisição para a API
response = requests.get(url_current)

if response.status_code == 200:
    # Convertendo a resposta em JSON (um dicionário Python)
    data = response.json()

    # Salvando os dados 
    temp = data['main']['temp']
    umidade = data['main']['humidity']
    vento = data['wind']['speed']
    temp_min = data['main']['temp_min']
    temp_max = data['main']['temp_max']
    clima = data['weather'][0]['description']
    clima = clima.title()
    date_time = datetime.datetime.utcfromtimestamp(data['dt'])
    day_of_week = date_time.strftime('%A')
    icon_code = data['weather'][0]['main'] 

    # Exemplo de mapeamento de 'main' para ícones de Font Awesome
    weather_icon_mapping = {
        'Clear': 'fa-sun',
        'Clouds': 'fa-cloud',
        'Rain': 'fa-cloud-showers-heavy',
        'Drizzle': 'fa-cloud-rain',
        'Thunderstorm': 'fa-bolt',
        'Snow': 'fa-snowflake',
        'Mist': 'fa-smog',
        'Fog': 'fa-smog',
        'Haze': 'fa-smog'
    }

    # Buscar o ícone correspondente
    icon_class = weather_icon_mapping.get(icon_code, 'fa-question')

   # Exibindo os valores
    print(f"Clima: {clima}")
    print(f"Temperatura: {temp}")
    print(f"Umidade: {umidade}")
    print(f"Velocidade do vento: {vento}")
    print(f"Temperatura mínima: {temp_min}")
    print(f"Temperatura máxima: {temp_max}")

else:
    # Imprimindo o código de status caso haja erro
    print(f"Erro na requisição: {response.status_code}")

@dash_temp_bp.route("/dashboard")
def route_HomePage():
    return render_template('dash_temp.html',city=city,temp=temp,clima=clima,temp_min=temp_min,temp_max=temp_max,day=day_of_week,icon=icon_class)
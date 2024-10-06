import requests
import datetime
from flask import Blueprint, render_template, redirect, session, flash

dash_temp_bp = Blueprint("dash_temp_menu", __name__, template_folder="templates")

api_weather= '94d84e5dff66fb4d5c74a3b6bb0f8f25'

# Função auxiliar para obter os dados da API do OpenWeather
def get_weather_data(city):
    # Construir URL para coordenadas da cidade
    url_coord = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={api_weather}"
    
    # Fazer a requisição à API
    response = requests.get(url_coord)
    
    if response.status_code == 200:
        data = response.json()
        
        if data:
            # Obter latitude e longitude
            lat = data[0]['lat']
            lon = data[0]['lon']

            # Construir URL para obter o clima atual baseado nas coordenadas
            url_current = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={api_weather}&lang=pt_br"
            response_current = requests.get(url_current)

            if response_current.status_code == 200:
                weather_data = response_current.json()
                return weather_data  # Retorna os dados climáticos
            else:
                return None  # Erro ao obter o clima atual
        else:
            return None  # Nenhum dado de coordenada encontrado
    else:
        return None  # Erro ao obter coordenadas

@dash_temp_bp.route("/dashboard")
def route_HomePage():
    # Pegar a cidade da sessão
    city = session.get('region')
    
    if city:
        # Obter os dados de clima para a cidade
        weather_data = get_weather_data(city)

        if weather_data:
            # Extrair os dados relevantes
            temp = weather_data['main']['temp']
            umidade = weather_data['main']['humidity']
            vento = weather_data['wind']['speed']
            temp_min = weather_data['main']['temp_min']
            temp_max = weather_data['main']['temp_max']
            clima = weather_data['weather'][0]['description'].title()
            date_time = datetime.datetime.utcfromtimestamp(weather_data['dt'])
            day_of_week = date_time.strftime('%A')
            icon_code = weather_data['weather'][0]['main']

            # Mapeamento de 'main' para ícones de Font Awesome
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

            # Renderizar a página com os dados do clima
            return render_template(
                'dash_temp.html', 
                city=city, 
                temp=temp, 
                clima=clima, 
                temp_min=temp_min, 
                temp_max=temp_max, 
                day=day_of_week, 
                icon=icon_class
            )
        else:
            flash("Erro ao buscar os dados climáticos. Por favor, tente novamente.", "error")
            return redirect(url_for('route_HomePage'))
    else:
        flash("Nenhuma região selecionada. Por favor, faça o login novamente.", "error")
        return redirect(url_for('Login_Menu.route_login'))

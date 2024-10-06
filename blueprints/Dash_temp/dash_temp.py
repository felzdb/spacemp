import requests
import datetime
from flask import Blueprint, render_template, redirect, session, flash, url_for, request
import google.generativeai as genai
import os
from flask import Blueprint, jsonify, render_template, request
import requests

dash_temp_bp = Blueprint("dash_temp_menu", __name__, template_folder="templates")

api_weather= '94d84e5dff66fb4d5c74a3b6bb0f8f25'

# Função auxiliar para obter os dados da API do OpenWeather
def get_weather_data(city):
    # Construir URL para coordenadas da cidade
    url_coord = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={api_weather}"
    
    response = requests.get(url_coord)
        
    if response.status_code == 200:
        data = response.json()
            
        if data:
            # Obter latitude e longitude
            lat = data[0]['lat']
            lon = data[0]['lon']

            # Construir URL para obter o clima atual baseado nas coordenadas
            url_current = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={api_weather}"
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



def GPT_Generate(prompt):
    genai.configure(api_key="AIzaSyCOS8abrrK3XqAeGwYXcjlWwxODjp2Hhu0")

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text

@dash_temp_bp.route("/dashboard", methods=['GET', 'POST'])
def route_HomePage():
    city = session.get('region')
        
    if city:
        # Obter os dados de clima para a cidade
        weather_data = get_weather_data(city)

        if weather_data:
            # Extrair os dados relevantes
            lat = weather_data['coord']['lat']
            lon = weather_data['coord']['lon']
            temp = weather_data['main']['temp']
            humidity = weather_data['main']['humidity']
            wind_speed = weather_data['wind']['speed']
            temp_min = weather_data['main']['temp_min']
            temp_max = weather_data['main']['temp_max']
            pressure = weather_data['main']['pressure']
            clima = weather_data['weather'][0]['description'].title()
            date_time = datetime.datetime.utcfromtimestamp(weather_data['dt'])
            day_of_week = date_time.strftime('%A')
            icon_code = weather_data['weather'][0]['icon']

            print(lat)
            print(lon)


    if request.method == "POST":

        chat = request.form['prompt']
        mensagens_user = chat
        mensagens_bot = GPT_Generate(chat)
        return render_template(
                    'dash_temp.html', 
                    city=city, 
                    temp=temp, 
                    clima=clima, 
                    temp_min=temp_min, 
                    temp_max=temp_max, 
                    day=day_of_week, 
                    icon=icon_code,
                    lat=lat,
                    lon=lon,
                    humidity = humidity,
                    wind_speed = wind_speed,
                    pressure = pressure,
                    mensagens_bot=mensagens_bot, 
                    mensagens_user=mensagens_user
                )
    

    # Renderizar a página com os dados do clima
    else:
        return render_template(
                'dash_temp.html', 
                city=city, 
                temp=temp, 
                clima=clima, 
                temp_min=temp_min, 
                temp_max=temp_max, 
                day=day_of_week, 
                icon=icon_code,
                lat=lat,
                lon=lon,
                humidity = humidity,
                wind_speed = wind_speed,
                pressure = pressure
            )

print
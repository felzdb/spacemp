import requests
import datetime

api_weather= '94d84e5dff66fb4d5c74a3b6bb0f8f25'
lat = -29.03
lon = -51.18

url_current = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={api_weather}&lang=pt_br"

# Fazendo a requisição para a API
response = requests.get(url_current)

# Verifica se a requisição foi bem sucedida
if response.status_code == 200:
    data = response.json()
    date_time = datetime.datetime.utcfromtimestamp(data['dt'])
    day_of_week = date_time.strftime('%A')

    print(data)
    print(day_of_week)
else:
    # Imprimindo o código de status caso haja erro
    print(f"Erro na requisição: {response.status_code}")



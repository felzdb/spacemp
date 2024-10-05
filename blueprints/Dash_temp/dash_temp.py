import requests

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
import requests
import json

headers = {
    "Authorization": f"Bearer {""}"
}

requisicao = requests.get("https://api.openai.com/v1/models", headers=headers)

print(requisicao)
print(requisicao.text)

id_modelo = "gpt-3.5-turbo"
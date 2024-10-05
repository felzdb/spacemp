import requests
import json

headers = {
    "Authorization": f"Bearer {""}"
}
link = "a"
requisicao = requests.get(link, headers=headers)

print(requisicao)
print(requisicao.text)

id_modelo = "gpt-3.5-turbo"
import requests
import json

headers = {
    "Authorization": "Bearer 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"
}
link = "https://api.openai.com/v1/models"
requisicao = requests.get(link, headers=headers)

print(requisicao)
print(requisicao.text)

id_modelo = "gpt-3.5-turbo"
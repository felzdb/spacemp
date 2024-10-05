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
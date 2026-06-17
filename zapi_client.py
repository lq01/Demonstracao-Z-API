import requests
from dotenv import load_dotenv
from os import getenv

load_dotenv()

url = f"https://api.z-api.io/instances/{getenv('ZAPI_INSTANCE_ID')}/token/{getenv('ZAPI_TOKEN')}/send-text"

payload = {
    "phone": "<string>",
    "message": "<string>"
}
headers = {
    "Client-Token": getenv('ZAPI_CLIENT_TOKEN'),
    "Content-Type": "application/json"
}

def enviar_mensagem(telefone: str, mensagem: str) -> bool:
    payload['phone'] = telefone
    payload['message'] = mensagem
    response = requests.post(url, json=payload, headers=headers)
    return response.status_code == 200
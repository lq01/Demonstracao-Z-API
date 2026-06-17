import logging
import requests
from dotenv import load_dotenv
from os import getenv

logger = logging.getLogger(__name__)

load_dotenv()

instance_id = getenv('ZAPI_INSTANCE_ID')
zapi_token = getenv('ZAPI_TOKEN')
client_token = getenv('ZAPI_CLIENT_TOKEN')

if not instance_id or not zapi_token or not client_token:
    raise EnvironmentError("Variáveis ZAPI_INSTANCE_ID, ZAPI_TOKEN e ZAPI_CLIENT_TOKEN precisam estar definidas no .env")

url = f"https://api.z-api.io/instances/{instance_id}/token/{zapi_token}/send-text"

headers = {
    "Client-Token": client_token,
    "Content-Type": "application/json"
}

def enviar_mensagem(telefone: str, mensagem: str) -> bool:
    payload = {
        "phone": telefone,
        "message": mensagem
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=15)
        response.raise_for_status()
        return True
    except requests.exceptions.Timeout:
        logger.error(f"Timeout ao enviar mensagem para {telefone}")
    except requests.exceptions.ConnectionError:
        logger.error(f"Falha de conexão ao enviar mensagem para {telefone}")
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP {response.status_code} ao enviar para {telefone}: {e}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Erro inesperado ao enviar para {telefone}: {e}")

    return False
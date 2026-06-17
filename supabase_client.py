import supabase
from dotenv import load_dotenv
from os import getenv

load_dotenv()

url = getenv('SUPABASE_URL')
key = getenv('SUPABASE_KEY')

if not url or not key:
    raise EnvironmentError("Variáveis SUPABASE_URL e SUPABASE_KEY precisam estar definidas no .env")

supabase_client = supabase.create_client(url, key)

def listar_contatos() -> list[tuple[str, str]]:
    try:
        response = supabase_client.table("contatos").select("telefone_contato, nome_contato").limit(3).execute()
    except Exception as e:
        print(f"[ERRO] Falha ao consultar contatos no Supabase: {e}")
        return []

    if not response.data:
        print("[AVISO] Nenhum contato encontrado na tabela.")
        return []

    return [(contato['telefone_contato'], contato['nome_contato']) for contato in response.data]

import supabase
from dotenv import load_dotenv
from os import getenv

load_dotenv()
supabase_client = supabase.create_client(getenv('SUPABASE_URL'), getenv('SUPABASE_KEY'))

def listar_contatos() -> list[tuple[str, str]]:
    response = supabase_client.table("contatos").select("telefone_contato, nome_contato").limit(3).execute()
    return [(contato['telefone_contato'], contato['nome_contato']) for contato in response.data]

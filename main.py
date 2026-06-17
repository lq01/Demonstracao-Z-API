from supabase_client import listar_contatos
from zapi_client import enviar_mensagem

contatos = listar_contatos()
for contato in contatos:
    mensagem = f"Olá {contato[1]}, tudo bem com você?"
    enviar_mensagem(contato[0], mensagem)
from supabase_client import listar_contatos
from zapi_client import enviar_mensagem

def main():
    contatos = listar_contatos()
    if not contatos:
        print("[INFO] Nenhum contato para processar. Encerrando.")
        return

    for telefone, nome in contatos:
        mensagem = f"Olá {nome}, tudo bem com você?"
        try:
            sucesso = enviar_mensagem(telefone, mensagem)
            if sucesso:
                print(f"[OK] Mensagem enviada para {nome} ({telefone})")
            else:
                print(f"[FALHA] Não foi possível enviar para {nome} ({telefone})")
        except Exception as e:
            print(f"[ERRO] Erro inesperado ao processar {nome} ({telefone}): {e}")


if __name__ == "__main__":
    main()
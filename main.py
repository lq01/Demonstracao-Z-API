import logging
from supabase_client import listar_contatos
from zapi_client import enviar_mensagem

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("app.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)
logging.getLogger("httpx").setLevel(logging.WARNING) #isso aqui é pra não misturar log comum da API com o do app

def main():
    contatos = listar_contatos()
    if not contatos:
        logger.info("Nenhum contato para processar. Encerrando.")
        return

    for telefone, nome in contatos:
        mensagem = f"Olá {nome}, tudo bem com você?"
        try:
            sucesso = enviar_mensagem(telefone, mensagem)
            if sucesso:
                logger.info(f"Mensagem enviada para {nome} ({telefone})")
            else:
                logger.warning(f"Não foi possível enviar para {nome} ({telefone})")
        except Exception as e:
            logger.error(f"Erro inesperado ao processar {nome} ({telefone}): {e}")


if __name__ == "__main__":
    main()
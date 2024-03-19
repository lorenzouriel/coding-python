from loguru import logger

logger.add("meu_app.log", level="CRITICAL")

def soma(x, y):
    try:
        soma = x + y
        logger.info(f"Você digitou valores corretos: {soma}")
        return x + y
    except:
        logger.critical("Você precisa digitar valores corretos!")

soma(2,3)
soma(2,"3")
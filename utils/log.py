import logging

def setup_logger():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    return logging.getLogger(__name__)

logger = setup_logger()

def log_error(mensaje):
    logger.error(mensaje)
    
def log_info(mensaje):  # Para mensajes informativos
    logger.info(mensaje)

def log_debug(mensaje):  # Para mensajes de depuración
    logger.debug(mensaje)
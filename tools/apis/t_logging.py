import logging
from functools import wraps

path: str = "tools/apis/log/logs.log"

# Configuración del logging
logging.basicConfig(
    filename=path,  # Nombre del fichero donde se guardarán los errores
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def error_logs(func):
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Function '{func.__name__}', ERROR: {str(e)}")
            raise  # Vuelve a lanzar la excepción después de registrarla
    return wrapper
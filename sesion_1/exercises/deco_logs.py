import logging
from functools import wraps
import os

def log_errors(path="exercises/logs/log.log"):

    check_path: str = os.path.dirname(path)
    if check_path and not os.path.exists(check_path):
        os.mkdir(check_path)
        
    logging.basicConfig(filename=path,
                        level=logging.ERROR,
                        format=("%(asctime)s - %(levelname)s - %(message)s")
                        )
    
    def decorator(fun: callable)-> callable:
        
        @wraps(fun)
        def wrapper(*args,**kwargs):
            try:
                return fun(*args,**kwargs)
            except Exception as ex:
                logging.error(f"In the function '{fun.__name__}', in the module '{fun.__module__}', a error has ocurred {ex}" , exc_info=True)
                raise
        
        return wrapper
    return decorator
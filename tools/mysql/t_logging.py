import logging
from functools import wraps
import os

def log_error(PATH = "tools/sqlite3/log/logs.log"):
    """ creating the log format """
    
    path_name = os.path.dirname(PATH)
    if path_name and not os.path.exists(path_name):
        os.mkdir(path_name)
        
    logging.basicConfig(
                filename=PATH,
                level=logging.ERROR,
                format = ('%(asctime)s - %(levelname)s - %(message)s')
                )

    def decorator(fun: callable) -> callable:
        @wraps(fun)
        def wrapper(*args, **kwargs) -> callable:
            
            try:
                
                logging.debug(f"Entry into the function '{fun.__name__}' in the module '{fun.__module__}'")
                result = fun(*args,**kwargs)
                logging.info(f"Correct execution of the function '{fun.__name__}.'")
                return result
            
            except Exception:
                logging.error(f"The error ocurred in the funtion '{fun.__name__}', in the module '{fun.__module__}'", exc_info=True)
                raise
            
        return wrapper
    return decorator

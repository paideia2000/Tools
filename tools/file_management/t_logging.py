import logging
from functools import wraps
import os

def log_error(PATH = "tools/file_management/log/logs.log"):
    
    
    path_file = os.path.dirname(PATH)
    if path_file and not os.path.exists(path_file):
        os.mkdir(path_file)
        
    logging.basicConfig(
        filename=PATH,
        level=logging.ERROR,
        format = ('%(asctime)s - %(levelname)s - %(message)s')
    )
    
    def decorator(fun: object) -> object:
        @wraps(fun)
        def wrapper(*args, **kwargs):
            
            try:
                
                return fun(*args, *kwargs)
            
            except Exception:
                logging.error(f"The error ocurred in the funtion '{fun.__name__}', in the module '{fun.__module__}'", exc_info=True)
                raise
        
        return wrapper
    return decorator
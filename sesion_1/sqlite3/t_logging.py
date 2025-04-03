import logging
import os
from functools import wraps

def log_error(PATH = "sqlite3/log/log.log"):
    
    mk_direc: str = os.path.dirname(PATH)
    if mk_direc and not os.path.exists(mk_direc):
        os.mkdir(mk_direc)

    logging.basicConfig(filename=PATH, 
                        level=logging.ERROR,
                        format=('%(asctime)s - %(levelname)s  - %(message)s' )
                        )
    
    def decorator(fun):
        @wraps(fun)
        def wrapper(*arg, **kwargs):
            
            try:
                get_data = fun(*arg, **kwargs)
                return get_data
            except  Exception as ex:
                logging.error(f"In the function: '{fun.__name__}()', an error ocurred: {ex}", exc_info=True)
                raise
    
        return wrapper
    return decorator
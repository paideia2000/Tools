import logging
from functools import wraps
import os

def log_anything(path_file="poo/Curso_cepi/logs/logs.log"):
    
    name_dir = os.path.dirname(path_file)
    if name_dir and not os.path.exists(name_dir):
        os.mkdir(name_dir)
    
    logging.basicConfig(filename=path_file, 
                        level=logging.DEBUG,
                        filemode="w",
                        format = ('%(asctime)s - %(levelname)s - %(message)s')
                        )

    def decorator(fun: callable) -> callable:
        @wraps(fun)
        def wrapper(*args,**kwargs):
            try:
                
                logging.debug(f"Entry into the function '{fun.__name__}' in the module '{fun.__module__}'")
                result = fun(*args,**kwargs)
                logging.info(f"Correct execution of the function '{fun.__name__}.'")
                return result
            
            except Exception:
                logging.error(f"Error in the function '{fun.__name__}'.", exc_info = True)
                raise 
            
        
        return wrapper
    
    return decorator


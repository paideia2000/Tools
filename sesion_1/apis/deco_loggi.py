import logging
import os
from functools import wraps

def error_logs(path="apis/log/logs.log"):
    
    path_file = os.path.dirname(path)
    if path_file and not os.path.exists(path_file):
        os.mkdir(path_file)

    logging.basicConfig(filename=path,
                        level=logging.DEBUG,
                        filemode="a",
                        format=("%(asctime)s - %(levelname)s - %(message)s")
                        )
    
    def decorator(func: callable) -> callable:
        @wraps(func)
        def warpper(*args,**kwargs):
            try:
                logging.debug("Entre to the function.")
                result = func(*args,**kwargs)
                logging.info("The function was executed succesffuly.")
                return result
            except Exception as exp:
                logging.error(exp, exc_info=True)
                raise
        
        return warpper
    
    return decorator
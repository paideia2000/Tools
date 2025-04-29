import logging
import time
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(level=logging.INFO, format = (' %(asctime)s - %(levelname)s - %(threadName)s - %(message)s'))



def sumar(a: int, b:int) ->None:
    """ sum two numbers """
    time.sleep(1)
    logging.info("Execute the funtion 'sumar'")
    print(a+b)


if __name__=="__main__":
    
    executor = ThreadPoolExecutor(max_workers=2)
    executor.submit(sumar, 5,5)
    executor.submit(sumar, 5,5)
    executor.submit(sumar, 5,5)
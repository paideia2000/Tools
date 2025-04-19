import threading
import logging

logging.basicConfig(level=logging.INFO, format = ('%(levelname)s - %(threadName)s - %(message)s'))



def sumar(a: int, b:int) ->None:
    """ sum two numbers """
    logging.info("Execute the funtion 'sumar'")
    print(a+b)
    



h1 = threading.Thread(name="hilo1", target=sumar, args=(5,5))#make the thread with the module threading.Thread

h1.start()
h1.join()


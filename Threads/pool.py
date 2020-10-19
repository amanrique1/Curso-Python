import time
import logging
import os
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(level=logging.DEBUG,format="%(threadName)s: %(message)s")

def superTask(a,b):
    time.sleep(1)
    logging.info(f"Terminamos la tarea compleja con valores {a}/{b}\n")

if __name__=="__main__":
    maxThreads = os.cpu_count()
    executor=ThreadPoolExecutor(max_workers=maxThreads)
    executor.submit(superTask,1,2)
    executor.submit(superTask,3,4)
    #si queremos que el pool de thread tenga un tiempo de vida se usa la palabra with
    with ThreadPoolExecutor(max_workers=maxThreads) as executor2:
        executor2.submit(superTask,5,6)
        executor2.submit(superTask,7,8)
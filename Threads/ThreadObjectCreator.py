import time
import datetime
import logging
from SearchThread import SearchThread
from SaveThread import SaveThread

logging.basicConfig(level=logging.INFO,format='[%(levelname)s](%(threadName)-s) %(message)s')

def search(personId):
    logging.info("Looking for the person id: "+str(personId))
    time.sleep(2)
    return

def save(personId,data):
    logging.info("Looking for the person id: "+str(personId)+ " with data: "+ data)
    time.sleep(5)
    return

startTime = datetime.datetime.now()

t1 = SearchThread("Thread 1",1,"")
t2 = SaveThread("Thread 2",1,"Python is la monda")
#start the work
t1.start()
t2.start()
#with join we can synchronize the created thread with the main thread
t1.join()
t2.join()
finTime = datetime.datetime.now()
print("Total time "+str(finTime-startTime))
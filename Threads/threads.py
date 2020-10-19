import threading
import time
import datetime
import logging

logging.basicConfig(level=logging.INFO,format='[%(levelname)s](%(threadName)-s) %(message)s')

def search(personId):
    logging.info("Looking for the person id: "+str(personId))
    time.sleep(2)

def save(personId,data):
    logging.info("Looking for the person id: "+str(personId)+ " with data: "+ data)
    time.sleep(5)

startTime = datetime.datetime.now()
"""
1. we set a name for the thread
2. we set the target that is also function to run
3. we set the args for the target (we send them in a tuple form)
"""
#In t1 case we just send 1 param with the coma to complete the tuple
t1 = threading.Thread(name="thread_1",target=search,args=(1,))
t2 = threading.Thread(name="thread_2",target=save,args=(1,"Looking for something"))
#start the work
t1.start()
t2.start()
#with join we can synchronize the created thread with the main thread
t1.join()
t2.join()
finTime = datetime.datetime.now()
print("Total time "+str(finTime-startTime))
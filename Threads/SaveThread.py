import threading
import time
import logging

logging.basicConfig(level=logging.INFO,format='[%(levelname)s](%(threadName)-s) %(message)s')

class SaveThread(threading.Thread):
    #Constructor
    def __init__(self,name,personId,data):
        #In the init we can can also send it directly to the save method passing the args like in the other example
        threading.Thread.__init__(self,name=name,target=SaveThread.run)
        self.name = name
        self.personId = personId
        self.data= data
    #Run method, necessary for Thread class extending
    def run(self):
        self.save(self.personId,self.data)

    def save(self,personId,data):
        logging.info("Looking for the person id: "+str(personId)+ " with data: "+ data)
        time.sleep(5)
        return

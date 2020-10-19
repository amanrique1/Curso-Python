import threading
import time
import logging

logging.basicConfig(level=logging.INFO,format='[%(levelname)s](%(threadName)-s) %(message)s')

class SearchThread(threading.Thread):
    #Constructor
    def __init__(self,name,personId,data):

        #In the init we can can also send it directly to the search method passing the args like in the other example
        threading.Thread.__init__(self,name = name,target=SearchThread.run)
        self.name = name
        self.personId = personId
        self.data= data
    #Run method, just a convention
    def run(self):
        self.search(self.personId)

    def search(self,personId):
        logging.info("Looking for the person id: "+str(personId))
        time.sleep(2)
        return

import time
import threading
from multiprocessing import Process, current_process

def countdown(number):
    while number>0:
        number-=1
    #print(f'Current process id: {current_process.name}')

if __name__ == '__main__':
    start = time.time()
    count=10000000

    t1= Process(target=countdown,args=(count,))
    t2= Process(target=countdown,args=(count,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print(f'Total time multi processing {time.time()-start}')

    start2=time.time()
    count2=10000000
    t3= threading.Thread(target=countdown,args=(count,))
    t4= threading.Thread(target=countdown,args=(count,))

    t3.start()
    t4.start()

    t3.join()
    t4.join()
    print(f'Total time multi thread {time.time()-start2}')

    """
    As a result we can see that the time in threading isn't better and that happens because both threads are pointing the same variable and GIL doesn't allow this so the other thread has to wait until the first one stop.
    In multiprocessing each process has its own interpreter
    """
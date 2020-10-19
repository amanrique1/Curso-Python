""" A lock or mutex is a sychronization mechanism for enforcing
limits on access to a resource in an environment where there
are many threads of execution. """
import time
import logging
from multiprocessing import Process, Lock, Value, Array
from multiprocessing import log_to_stderr, get_logger

def add_500_no_lock(total):
    for _ in range(100):
        time.sleep(0.01)
        total.value += 5
    return total.value

def sub_500_no_lock(total):
    for _ in range(100):
        time.sleep(0.01)
        total.value -= 5
    return total

def add_500_lock(total, lock):
    for _ in range(100):
        time.sleep(0.01)
        lock.acquire()
        total.value += 5
        lock.release()


def sub_500_lock(total, lock):
    for _ in range(100):
        time.sleep(0.01)
        lock.acquire()
        total.value -= 5
        lock.release()

if __name__ == '__main__':
    #With value type we say that it is a shared resource
    total = Value('i',500)
    arr_val = Array('i', range(10))

    lock = Lock()

    log_to_stderr()
    logger=get_logger()
    logger.setLevel(logging.INFO)

    addProcess = Process(target=add_500_lock,args=(total,lock))
    subProcess = Process(target=sub_500_lock,args=(total,lock))
    addProcess.start()
    subProcess.start()
    addProcess.join()
    subProcess.join()
    print(total.value) #Same Value (500)

    addProcess = Process(target=add_500_no_lock,args=(total,))
    subProcess = Process(target=sub_500_no_lock,args=(total,))
    addProcess.start()
    subProcess.start()
    addProcess.join()
    subProcess.join()
    print(total.value) #Not necessary the same value
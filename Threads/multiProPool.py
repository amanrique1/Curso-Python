import time
import logging
from multiprocessing import Pool

logging.basicConfig(level=logging.INFO,format='[%(levelname)s](%(processName)-s) %(message)s')

def sum_square(number):
    counter = 0
    for i in range(number):
        counter += i * i
    return counter


def sum_square_with_mp(numbers):

    start_time = time.time()
    # We can send the number of processors that we want to use as default it uses all the processors availables
    pool = Pool()
    #Map function receive the function and the parameters
    result = pool.map(sum_square, numbers)

    #Wait until all is compleated
    pool.close()
    pool.join()

    end_time = time.time() - start_time

    print(f"Processing {len(numbers)} numbers took {end_time}s time using multiprocessing.")


def sum_square_no_mp(numbers):

    start_time = time.time()
    result = []

    for i in numbers:
        result.append(sum_square(i))
    end_time = time.time() - start_time

    print(f"Processing {len(numbers)} numbers took {end_time}s time using serial processing.")


if __name__ == '__main__':
    #try with different values because create a new process could became expensive but when the operations takes few time is better don't use processes or just threads if is the case
    numbers = range(10000)
    sum_square_with_mp(numbers)
    sum_square_no_mp(numbers)
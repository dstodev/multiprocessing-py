import multiprocessing as mp
import time


def print_number(number: int):
    time.sleep((2 - number) * (50 / 1000))  # (2 - number) * 50ms
    print(number)  # Prints in reverse order because of the delay
    return number


if __name__ == '__main__':
    numbers = []
    pool = mp.Pool()
    # Callback is called once with an ordered list of results. Function is
    # called once per input argument using parallel processes.
    job = pool.map_async(print_number, (0, 1, 2), callback=numbers.extend)
    pool.close()
    pool.join()
    print(numbers)

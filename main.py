import multiprocessing as mp
import time


def main():
    numbers = []
    pool = mp.Pool()

    # Using map_async(), print_number() is called once per input in parallel:
    #   print_number(2)
    #   print_number(1)
    #   print_number(0)
    # map_async() requires print_number() to take one parameter. To provide
    # more than one parameter to a function, consider starmap_async().
    # Once all functions calls complete, a list of all returned values is
    # provided to the callback function:
    #   numbers.extend([2, 1, 0])
    job_map = pool.map_async(print_number, (2, 1, 0), callback=numbers.extend)

    # Using apply_async(), print_number() is called once on the pool:
    #   print_number(3)
    # and the returned value is provided to the callback function:
    #   numbers.append(3)
    job_apply = pool.apply_async(print_number, (3,), callback=numbers.append)

    pool.close()  # close() must precede join()
    pool.join()  # join() will block until all processes complete

    # Numbers are printed in order, but the returned values are not in order.
    # This is because they are printed in "time sort" order: numbers print
    # after waiting, in time, their value multiplied by some scalar.
    # However, the order of returned values is not in order: [2, 1, 0, 3].
    # This is because map_async() (and starmap_async()) wait for all
    # function calls to complete before giving the full list of results to
    # the callback, so are able to preserve order. apply_async() gives
    # the result to the callback immediately after the function completes.

    print(numbers)


def print_number(number: int):
    time.sleep(number * (50 / 1000))  # number * 50ms
    print(number)
    return number


if __name__ == '__main__':
    main()

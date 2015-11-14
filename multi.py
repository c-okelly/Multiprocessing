__author__ = "Conor O'Kelly"

"""
Have prime calculator function. Will return a list of all the prime between certain numbers.

Have second function that will run prime calculator on a number of cores depending on selection.

"""

import time
from multiprocessing import Process


# Prime calculator

def prime_calculator(start,finish):
    print ("Start of calculator starting %i to %i " % (start, finish))
    list_of_primes = []

    for number in range(start,finish+1):
        factor_list = []

        # Try find factor. If exists append to list of factors.
        for i in range(2, number):
            if number % i == 0:
                factor = ("%i * %i") % (number/i, i)
                factor_list.append(factor)

        if len(factor_list) == 0:
            # loop fell through without finding a factor
            # print (number, "is a prime number")
            list_of_primes.append(number)

    #print(list_of_primes)
    return list_of_primes

def calculator_1_process():

     a = Process(target=prime_calculator, args=(1,10000))

     start_time = time.time()
     a.start()
     a_boolen = a.is_alive()

     while a_boolen == True:
         a_boolen = a.is_alive()

     print("--- 1 process took %s seconds --- \n" % (time.time() - start_time))

def calculator_2_process():

    a = Process(target=prime_calculator, args=(1,5000))
    b = Process(target=prime_calculator, args=(5000,10000))

    start_time = time.time()
    a.start()
    b.start()
    a_boolen, b_boolen = a.is_alive(), b.is_alive()

    while a_boolen == True or b_boolen == True:
         a_boolen, b_boolen = a.is_alive(), b.is_alive()

    print("--- 2 process took %s seconds --- \n" % (time.time() - start_time))

def calculator_4_process():

    a = Process(target=prime_calculator, args=(1,2500))
    b = Process(target=prime_calculator, args=(2500,5000))
    c = Process(target=prime_calculator, args=(5000,7500))
    d = Process(target=prime_calculator, args=(7500,10000))


    start_time = time.time()
    a.start()
    b.start()
    c.start()
    d.start()

    a_boolen, b_boolen, c_boolen, d_boolen = a.is_alive(), b.is_alive(), c.is_alive(), d.is_alive()

    while a_boolen == True or b_boolen == True or c_boolen == True or d_boolen == True:
         a_boolen, b_boolen, c_boolen, d_boolen = a.is_alive(), b.is_alive(), c.is_alive(), d.is_alive()

    print("--- 4 process took %s seconds --- \n" % (time.time() - start_time))


def run_all_calcultators():

    print ("""This program will run a prime calculator in four different ways
    First by using just one process. Then buy using two and then 4.
    Each process run time will be measured adn printed out.
    The process will also be running an extra process used to monitor
    (using a while loop) if the process has completed.
    """)

    calculator_1_process()
    calculator_2_process()
    calculator_4_process()

if __name__ == '__main__':

    run_all_calcultators()
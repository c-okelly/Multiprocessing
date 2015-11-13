__author__ = "Conor O'Kelly"

"""
Have prime calculator function. Will return a list of all the prime between certain numbers.

Have second function that will run prime calculator on a number of cores depending on selection.

"""

from multiprocessing import Process


# Prime calculator

def prime_calculator(start,finish):
    print ("Start of calculator starting at ", start)
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

    print(list_of_primes)
    return list_of_primes



if __name__ == '__main__':

    jobs = []

    a = Process(target=prime_calculator, args=(1,10000))
    b = Process(target=prime_calculator, args=(10000,20000))

    a.start()
    b.start()


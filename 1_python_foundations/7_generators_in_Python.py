### This script is a walk through the article at:
# https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/

import math
import pickle
import os

# 0. define exceptions that will be used later on
class NotInteger(Exception):
    pass


class NegativeArgument(Exception):
    pass


class NotList(Exception):
    pass


# 1. The first problem that is posed is recognizing prime numbers in a list of numbers.
# To this end, an algorithm is needed to say whether a given number is a prime number.
def eratosthenes_sieve(n):
    """
    This function checks whether its input is a prime number
    :param n: a nonnegative integer
    :return: boolean saying whther n is prime
    """
    # check the input
    if not isinstance(n, int):
        raise NotInteger("Function eratosthenes_sieve got non-integer argument!")
    elif n < 0:
        raise NegativeArgument("Function eratosthenes_sieve got negative integer argument!")
    if n == 0 or n == 1:
        return False
    else:
        # walk through divisors up to sqrt of the input and check the residual
        for divisor in range(2, int(math.floor(math.sqrt(n)))+1, 1):
            if n % divisor == 0:
                return True
        # if none of those numbers turned out to be a divisor, return False
        return False


def select_primes_from_list(list_in):
    """
    This function takes in a list and filters out its elements that are not integers
    :param list_in: list to be filtered
    :return: list of integers that are prime numbers
    """
    # check the input
    if not isinstance(list_in, list):
        raise NotList("The argument passed to select_primes_from_list is not a list!")
    # iterate through the elements of the list
    primes_list = list()
    for item in list_in:
        try:
            # it might happen that list element is not an integer...
            if eratosthenes_sieve(item):
                primes_list.append(item)
        except NotInteger:
            print("List element is not an integer!")
        except NegativeArgument:
            print("List element is negative!")
        except Exception:
            print("General error in select_primes_from_list!")
    return primes_list


test_list = list(range(0, 20))
print(test_list)
print(select_primes_from_list(test_list))

# 2. Now, for the purpose of illustration, create a very big list of consecutive integers and show that if the size
# gets bigger it becomes problematic to work with such objects
list_of_integers = list()
for item in range(100000000):
    list_of_integers.append(item)

# save the list into a file in current directory
print("Current working directory: ", os.getcwd())
file_path = os.path.join(os.getcwd(), "big_list.p")
file1 = open(file=file_path, mode="wb")
pickle.dump(obj=list_of_integers, file=file1)
file1.close()
del list_of_integers

# in this setting, looking for consecutive numbers requires creation of big arrays of integers

# 3.
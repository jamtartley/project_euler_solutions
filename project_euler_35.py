"""
Project Euler 35

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""
import itertools
from functools import reduce

def isPrime(number):
    """
    Check if the given number is prime
    """
    for x in range(2, number):
        if (number % x == 0):
            return False

    return True

def getSetOfPrimes(limit):
    """
    Generates the primes upto the given limit
    """
    primes = []
    
    for x in range(2,limit):
        if(isPrime(x)):
            primes.append(x)
        
    return primes

def getCircularPrimes():
    primes = getSetOfPrimes(200)
    circular = []

    for x in primes:
        isCircular = True
        """
        MISUNDERSTOOD QUESTION, DOESN'T WANT ALL PERMUTATIONS, WANTS DIGITS ROTATIONS
        """
        for y in itertools.permutations([int(i) for i in str(x)]):
            if not isPrime(int(reduce(lambda a,b : a+str(b), y, ''))):
                isCircular = False
        if isCircular:
            circular.append(x)

    return circular
            

for x in getCircularPrimes():
    print(x)

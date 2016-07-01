"""
Project Euler 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

import math

def isPrime(number):
    """
    Check if the given number is prime
    """
    for x in range(2, int(math.sqrt(number)) + 1):
        if (number % x == 0):
            return False

    return True

def getSetOfPrimes(numNeeded):
    """
    Generates the first numNeeded in the prime sequence
    """
    primes = []
    current = 2
    
    while(len(primes) < numNeeded):
        if(isPrime(current)):
            primes.append(current)

        current += 1
        
    return primes

def getPrimeByNumber(number):
    """
    Get the number-th prime number
    """
    return getSetOfPrimes(number)[number - 1]

print(getPrimeByNumber(10001))

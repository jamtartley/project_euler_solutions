"""
Project Euler 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
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

def getPrimesBelowLimit(limit):
    """
    Get all primes below limit
    """
    primes = []

    for x in range(2, limit):
        if (isPrime(x)):
            primes.append(x)

    return primes

print(sum(getPrimesBelowLimit(2000000)))

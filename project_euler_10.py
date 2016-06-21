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

def getPrimesUpto(limit):
    """
    Uses Sieve of Eratosthenes
    """
    allNumbers = [True for x in range(2, limit)]
    
    for x in range(2, int(math.sqrt(limit))):
        if allNumbers[x - 2] == True:
            for y in range(x**2, limit, x):
                allNumbers[y - 2] = False

    for i in range(len(allNumbers)):
        if allNumbers[i]:
            yield i + 2
            
print(sum(getPrimesUpto(2000000)))

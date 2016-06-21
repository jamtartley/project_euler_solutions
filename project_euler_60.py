"""
Project Euler 60

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""

import math

def isPrime(number):
    for x in range(2, int(number / 2) + 1):
        if number % x == 0:
            return False
    return True

def isConcatPrime(a,b):
    return isPrime(int(str(a) + str(b))) and isPrime(int(str(a) + str(b)))

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
            
print(list(getPrimesUpto(10000)))
    


"""
Project Euler 47

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
"""

import math

def isPrime(number):
    """
    Checks whether given number is prime
    """
    for x in range(2, int(math.sqrt(number) + 1)):
        if number % x == 0:
            return False
    return True

def getNextPrime(prev):
    """
    Get next number in the prime sequence
    """
    x = prev + 1
    while not isPrime(x):
        x += 1
    return x

def getPrimeFactors(primes, number):
    """
    Returns the prime factors of a given number
    """

    while primes[len(primes) - 1] < number:
        primes.append(getNextPrime(primes[len(primes) - 1]))

    pIndex = 0
    
    while number != 1:
        while number % primes[pIndex] == 0:
            number /= primes[pIndex]
            yield primes[pIndex]
        pIndex += 1

def main():
    CONSEC_NEEDED = 4
    PRIME_FACTORS_NEEDED = 4
    currentRun = []
    primes = [2]
    x = 647

    while len(currentRun) != CONSEC_NEEDED:
        if (len(set(list(getPrimeFactors(primes, x)))) == PRIME_FACTORS_NEEDED):
            currentRun.append(x)
        else:
            currentRun.clear()
        x += 1

    print(currentRun)

main()
    

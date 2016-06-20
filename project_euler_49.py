"""
Project Euler 49

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
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

def isPermutation(a,b):
    """
    Checks whether two numbers are permutations of each other
    i.e. 1487 is a permutation of 4817
    """
    return sorted(str(a)) == sorted(str(b))

def main():
    difference = 3330
    for x in range(1000,3600):
        y = x + difference
        z = y + difference

        if not isPermutation(x,y) or not isPermutation(y,z):
            continue

        if isPrime(x) and isPrime(y) and isPrime(z):
            print(str(x) + str(y) + str(z))

main()

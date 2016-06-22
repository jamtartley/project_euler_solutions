"""
Project Euler 35

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
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

def isCircularPrime(number):
    """
    Converts number into a string and tests each rotation of the string for primality
    """
    rotations = [str(number)]

    for x in range(len(str(number)) - 1):
        prev = rotations[len(rotations) - 1]
        rotations.append(prev[1:len(prev)] + prev[0])

    
    for rotation in rotations:
        if not isPrime(int(rotation.lstrip('0'))):
            return False

    return True


def main():
    circulars = 0

    for x in range(2, 1000000):
        if isCircularPrime(x):
            circulars += 1

    print(circulars)

main()

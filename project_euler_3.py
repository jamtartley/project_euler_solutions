"""
Project Euler - 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import math

def getPrimeFactors(number):
    """
    Calculates all prime factors of a given number
    """
    factors = []

    for x in range(2,round(math.sqrt(number))):
        while (number % x == 0):
            number /= x
            factors.append(x)
        x += 1

    return set(factors)

print(max(getPrimeFactors(600851475143)))

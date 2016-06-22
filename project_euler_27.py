"""
Project Euler 27

Euler discovered the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n² + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |−4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
"""
import math
from time import time
def isPrime(number):
    """
    Checks primality of given number
    """
    if number < 0:
        return False
    
    for x in range(2, round(math.sqrt(number)) + 1):
        if number % x == 0:
            return False
    return True

def getValueFromFormula(n, a, b):
    """
    Get value for formula n^2 + na + b
    """
    return n**2 + n * a + b

def main():
    highestPrimeChain = -1
    highestCoeffProduct = -1

    for a in range(-999, 1000, 2):
        for b in range(1, 1000, 2):
            n = 0
            while isPrime(getValueFromFormula(n, a, b)):
                n += 1

            if n > highestPrimeChain:
                highestPrimeChain = n
                highestCoeffProduct = a * b

    print(highestCoeffProduct)
start= time()
main()
print(time()-start)

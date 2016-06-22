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

def getValueFromFormula(n, a, b):
    """
    Get value for formula n^2 + na + b
    """
    return n**2 + n * a + b

def main():
    primes = list(getPrimesUpto(100000))
    bPrimes = list(getPrimesUpto(1000))
    highestPrimeChain = -1
    highestCoeffProduct = -1

    for a in range(-999, 1000):
        for b in bPrimes:
            n = 0
            while getValueFromFormula(n, a, b) in primes:
                n += 1

            if n > highestPrimeChain:
                highestPrimeChain = n
                highestCoeffProduct = a * b

    print(highestCoeffProduct)

main()

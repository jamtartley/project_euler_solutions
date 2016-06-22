"""
Project Euler 32

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""
import itertools

def isPandigital(a, b, product):
    """
    Checks if a * b = product contains numbers 1-9
    """
    return sorted(str(a) + str(b) + str(product)) == sorted('123456789')

def main():
    pandigitals = []

    for x in range(1, 10000):
        for y in range(int(10000 / x) + 1):
            if isPandigital(x, y, x * y):
                pandigitals.append(x * y)

    print(sum(set(pandigitals)))

main()


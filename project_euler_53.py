"""
Project Euler 53

There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

nCr =	
n!
r!(n−r)!
,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?
"""

import math

def getNCR(n,r):
    """
    Calculates nCr where nCr = n! / r!(n-r)!
    """
    return int(math.factorial(n) / (math.factorial(r) * math.factorial(n - r)))

def getNCRValuesOver(maxN, value):
    """
    Counts all nCr upto some maximum n where the result > value
    """
    count = 0
    for n in range(1, maxN + 1):
        for r in range(1, n + 1):
            if getNCR(n, r) > value:
                count += 1
    return count

def main():
    print(getNCRValuesOver(100, 1000000))

main()

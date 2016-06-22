"""
Project Euler 23

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

import itertools
import math

def getProperDivisors(number):
    """
    Creates a list of all proper divisors of the given number
    """
    divisors = []
    
    for x in range(1, round(math.sqrt(number) + 1)):
        if number % x == 0:
            divisors.append(x)
            if number // x != number:
                divisors.append(number // x)
                
    return sorted(set(divisors))

def isAbundant(number):
    """
    Checks if a number is abundant, i.e. the sum of the proper divisors of number > number
    """
    return sum(getProperDivisors(number)) > number

def main():
    abundants = [x for x in range(12, 28124) if isAbundant(x)]

    #Calculate the sum of every possible pair of abundants (including the same 2 numbers)
    sums = set([sum(pair) for pair in itertools.combinations_with_replacement(abundants, 2)])
    cannots = []
            
    for x in range(28124):
        if x not in sums:
            cannots.append(x)

    print(sum(cannots))
        
main()

"""
Project Euler 34

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
import math

def isSumFactorial(number):
    """
    Checks if the factorials of each digit add upto the number itself
    """
    decomposition = [int(x) for x in str(number)]
    factorialTotal = 0

    for x in decomposition:
        factorialTotal += math.factorial(x)

    return factorialTotal == number

def main():
    total = 0

    #Upper bound is 9! * 7 as 9! * 8 produces a number with more than 8 digits
    for x in range(3, math.factorial(9) * 7):
        if isSumFactorial(x):
            total += x

    print(total)

main()

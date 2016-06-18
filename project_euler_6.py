"""
Project Euler 6

The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def getSquareOfSum(limit):
    """
    Calculates the square of the sum of integers upto limit
    """
    numberList = [int(i) for i in range(limit + 1)] 
    return sum(numberList) * sum(numberList)

def getSumOfSquares(limit):
    """
    Calculates the sum of the squares of integers upto limit
    """
    return sum([int(i) * i for i in range(limit + 1)] )

limit = 100
print(getSquareOfSum(limit) - getSumOfSquares(limit))


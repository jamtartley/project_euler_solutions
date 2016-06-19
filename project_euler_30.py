"""
Project Euler 30

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

def decomposeNumber(number):
    """
    Decompose a number into a list of its digits
    """
    return [int(x) for x in str(number)]

def isSumFifthPowers(number):
    """
    Checks if a given number is the sum of the 5th powers of each of its digits
    """
    decomposition = decomposeNumber(number)
    total = 0
    
    for x in decomposition:
        total += x ** 5

    return total == number

total = 0

for x in range(2, 1000000):
    if (isSumFifthPowers(x)):
        total += x

print(total)

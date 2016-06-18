"""
Project Euler 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def isDivisibleByAll(number, maxDivisor):
    """
    Checks if a number is divisible
    """    
    for x in range(2,maxDivisor):
        if (number % x != 0):
            return False

    return True

x = 2520

while(not isDivisibleByAll(x, 21)):
    #We already know the number has to be divisible by 2520 as it is given in the question, massive performance increase
    x += 2520

print(x)
    

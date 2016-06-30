"""
Project Euler 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def isDivisibleByAll(number):
    """
    Checks if a number is divisible by 1-20
    """    
    for x in range(2, 21):
        if number % x != 0:
            return False

    return True

def main():
    x = 2520

    while not isDivisibleByAll(x):
        x += 2520

    print(x)

main()
    

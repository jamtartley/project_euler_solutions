"""
Project Euler 14

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def isEven(number):
    """
    Check if given number is even
    """
    return number % 2 == 0

def getNextCollatz(number):
    """
    Get the next number in the Collatz sequence
    """
    if isEven(number):
        return number / 2
    else:
        return 3 * number + 1

def main():
    highest = 0
    greatestSize = -1

    for x in range(1, 1000001):
        size = 0
        number = x
        while number != 1:
            number = getNextCollatz(number)
            size += 1

        if size > greatestSize:
            highest = x
            greatestSize = size

    print(highest)
    
main()

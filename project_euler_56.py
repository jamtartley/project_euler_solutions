"""
Project Euler 56

A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
"""

def getDigitalSum(number):
    """
    Gets the sum total of all digits of a given number
    """
    return sum([int(digit) for digit in str(number)])

def main():
    MAX_VALUE = 100
    highest = -1

    for a in range(1, MAX_VALUE):
        for b in range(1, MAX_VALUE):
            highest = max(highest, getDigitalSum(a**b))

    print(highest)

main()
    

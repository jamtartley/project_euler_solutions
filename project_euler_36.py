"""
Project Euler 36

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

def getBinary(number):
    """
    Returns the binary representation of a base 10 number
    """
    return "{0:#b}".format(number)[2:]

def isPalindrome(number):
    """
    Checks to see if a number is a palindrome.
    """
    return str(number) == str(number)[::-1]

def main():
    total = 0

    for x in range(1000000):
        if isPalindrome(x) and isPalindrome(getBinary(x)):
            total += x

    print(total)

main()

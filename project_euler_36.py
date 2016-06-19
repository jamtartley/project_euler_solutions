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
    Works by splitting number into a list of its digits and checking
    xth position == (length - xth position)
    for every x upto the length of the list
    """
    listDigits = [int(x) for x in str(number)]

    for x in range(len(listDigits)):
        if listDigits[x] != listDigits[len(listDigits) - 1 - x]:
            return False
    
    return True

def main():
    total = 0

    for x in range(1000000):
        if isPalindrome(x) and isPalindrome(getBinary(x)):
            total += x

    print(total)

main()

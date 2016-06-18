"""
Project Euler - 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def splitNumberIntoList(number):
    """
    Splits a number into a list of digits
    """
    return [int(i) for i in str(number)]

def isPalindrome(number):
    """
    Checks to see if a number is a palindrome.
    Works by splitting number into a list of its digits and checking
    xth position == (length - xth position)
    for every x upto the length of the list
    """
    listDigits = splitNumberIntoList(number)

    for x in range(len(listDigits)):
        if listDigits[x] != listDigits[len(listDigits) - 1 - x]:
            return False
    
    return True

def getSetAllPalindromeProducts(start,limit):
    """
    Calculates cross-product of two sets consisting of integers from start to limit.
    Appends to a list if the product is palindromic
    """
    palindromes = []

    for x in range(start,limit):
        for y in range(start,limit):
            if (isPalindrome(x * y)):
                palindromes.append(x * y)

    return set(palindromes)

print(max(getSetAllPalindromeProducts(100,1000)))


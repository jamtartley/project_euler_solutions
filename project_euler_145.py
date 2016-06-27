"""
Project Euler 145

Some positive integers n have the property that the sum [ n + reverse(n) ] consists entirely of odd (decimal) digits. For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and 904 are reversible. Leading zeroes are not allowed in either n or reverse(n).

There are 120 reversible numbers below one-thousand.

How many reversible numbers are there below one-billion (109)?
"""

def getReverse(number):
    return str(number)[::-1]

def isReversible(number):
    reverse = getReverse(number)
    
    if reverse[:1] == '0':
        return False

    for digit in str(number + int(reverse)):
        if int(digit) % 2 == 0:
            return False

    return True

def main():
    count = 0

    for x in range(1, 10**9):
        if isReversible(x):
            count += 1

    print(count)

main()

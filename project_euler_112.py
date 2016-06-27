"""
Project Euler 112

Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.
"""

def isBouncyNumber(number):
    """
    Check if a number is bouncy.

    A number is bouncy if when checked digit-wise from left to right there are both increases and decreases
    """
    digits = [int(x) for x in str(number)]
    hasIncreased = False
    hasDecreased = False

    for x in range(1, len(digits)):
        if digits[x] < digits[x-1]:
            hasDecreased = True
        elif digits[x] > digits[x-1]:
            hasIncreased = True

        if hasDecreased and hasIncreased:
            return True

    return False

def main():
    bouncyCount = 0
    totalCount = 1
    number = 2
    
    while bouncyCount / totalCount != 0.99:
        if isBouncyNumber(number):
            bouncyCount += 1

        totalCount += 1
        number += 1

    print(totalCount)

main()

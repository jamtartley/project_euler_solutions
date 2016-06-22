"""
Project Euler 21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
import math

def getProperDivisors(number):
    """
    Creates a list of all proper divisors of the given number
    """
    divisors = []
    
    for x in range(1, round(math.sqrt(number) + 1)):
        if number % x == 0:
            divisors.append(x)
            if number // x != number:
                divisors.append(number // x)
                
    return sorted(divisors)

def main():
    total = 0
    matches = []
    
    for x in range(1, 10001):
        if x in matches:
            continue
        
        y = sum(getProperDivisors(x))
        
        if x == sum(getProperDivisors(y)) and x != y:
            matches.append(x)
            matches.append(y)

    print(sum(set(matches)))

main()

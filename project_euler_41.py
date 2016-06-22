"""
Project Euler 41

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""
import itertools
import math

def isPrime(number):
    """
    Tests given number for primality
    """
    if number < 2:
        return False

    for x in range(2, int(math.sqrt(number)) - 1):
        if number % x == 0:
            return False

    return True

def getPandigitals(digits):
    """
    Returns a digits digits number from 1-digits
    """
    return itertools.permutations(range(1,digits + 1))

def main():
    for x in range(9, 0, -1):
        pandigitals = list(getPandigitals(x))
        panNums = []
        
        for pandigital in pandigitals:
            panNums.append(int(''.join(map(str, pandigital))))

        panNums.reverse()

        for number in panNums:
            if isPrime(number):
                print(number)
                return
    
main()


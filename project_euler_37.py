"""
Project Euler 37

The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
import math

def isPrime(number):
    """
    Check if the given number is prime
    """
    if number < 2:
        return False
    
    for x in range(2, int(math.sqrt(number)) + 1):
        if (number % x == 0):
            return False

    return True

def isTruncatablePrime(prime):
    """
    Checks whether prime number is prime in every right- and left-truncated state
    """
    for x in range(len(str(prime))):
        if isPrime(int(str(prime)[x:])) and isPrime(int(str(prime)[:x+1])):
            pass
        else:
            return False
    
    return True

def main():
    truncatables = []
    x = 11

    while len(truncatables) != 11:
        if not isPrime(x):
            x += 1
            next

        if isTruncatablePrime(x):
            truncatables.append(x)

        x += 1

    print(sum(truncatables))

main()

"""
Project Euler 52

It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

def isPermutation(a,b):
    """
    Checks whether two numbers are permutations of one another
    """
    return sorted(str(a)) == sorted(str(b))

def check(number):
    """
    Checks if number * 2-6 are permutations of number
    """
    for x in range(1,7):
        if not isPermutation(number, number * x):
            return False
    return True
        
def main():
    current = 1
    found = False
    
    while not found:
        if check(current):
            found = True
            print(current)
        current += 1
    
main()

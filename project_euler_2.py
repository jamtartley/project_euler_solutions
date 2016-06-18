"""
Project Euler - 2

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

def isEven(number):
    """
    Checks a number is even
    """
    return number % 2 == 0

def fibonacci(limit):
    """
    Calculates the Fibonacci sequence until one of the terms reaches the given limit
    """
    fibs = [1,2]
    next = 3
    while next <= limit:
        fibs.append(next)
        next = next + fibs[len(fibs)-2]

    return fibs
        
def getAllEvens(listTerms):
    """
    Creates a new list of all even numbers in the given list
    """
    return [int(i) for i in listTerms if isEven(i)]
    
print(sum(getAllEvens(fibonacci(4000000))))
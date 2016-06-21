"""
Project Euler 67

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
"""
from time import time
def getTriangle():
    """
    Read in a triangle from a text file
    """
    file = open('p067_triangle.txt', 'r')
    lines = file.readlines()
    triangle = []
                
    for line in lines:
        triangle.append([int(number) for number in line.split()])

    return triangle

def sumCascadeUp(triangle):
    """
    Calculate max value of triangle by working from the bottom and calculating max value at each step
    """
    for lineIndex in range(len(triangle) - 2, -1, -1):
        for numberIndex in range(len(triangle[lineIndex])):
            triangle[lineIndex][numberIndex] = max(triangle[lineIndex][numberIndex] + triangle[lineIndex+1][numberIndex], triangle[lineIndex][numberIndex] + triangle[lineIndex+1][numberIndex+1])

    return triangle[0][0]
start = time()
print(sumCascadeUp(getTriangle()))
print(time() - start)















        
        

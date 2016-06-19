"""
Project Euler 39

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

import math

def getTriangles():
    maxLength = 1000
    
    for x in range(1,maxLength):
        for y in range(1,maxLength):
            z = math.sqrt(x**2 + y**2)
            if z == int(z):
                yield(x,y,int(z))

def getTotalCounts(triangles):
    counts = []
    for x in triangles:
        if (sum(x) <= 1000):
            counts.append(sum(x))
    return counts


def main():
    counts = getTotalCounts(getTriangles())
    print(max(set(counts), key=counts.count))

main()
    


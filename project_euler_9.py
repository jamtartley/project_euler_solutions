"""
Project Euler 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def getCorrectTripleProductForTotal(total):

    current = 1

    while(True):  
        for a in range(current):
            for b in range(current):
                for c in range(current):
                    if ((a*a) + (b*b) == (c*c)):
                        if (a+b+c == total):
                            return a*b*c


        current += 1

print(getCorrectTripleProductForTotal(234))

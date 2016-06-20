"""
Project Euler 42

The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""
import string
import math

def getLetterValueDict():
    """
    Creates a dictionary of letter values, i.e. 'A' -> 1
    """
    for x in range(len(string.ascii_uppercase)):
        yield string.ascii_uppercase[x], x+1

def isTriangular(number):
    """
    Tests whether a number is triangular
    """
    return (math.sqrt(8*number+1)-1)/2 == int((math.sqrt(8*number+1)-1)/2)

def getWords():
    """
    Read in text file and strip unnecessary marks
    """
    wordFile = open('p042_words.txt', 'r')
    words = wordFile.read().replace('"',"").split(',')
    for x in words:
        yield x
    
def getWordScore(word):
    """
    Calculates the 'score' of a word
    """
    values = dict(getLetterValueDict())
    score = 0

    for x in word:
        score += values.get(x)

    return score

def getTriangularWordCount():
    """
    Counts the number of words for which the score is triangular
    """
    words = getWords()
    total = 0

    for word in words:
        if isTriangular(getWordScore(word)):
            total += 1

    return total

print(getTriangularWordCount())


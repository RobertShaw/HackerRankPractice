#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    if s is None or s == "":
        return "YES"
    letterCount = {}


    for letter in s:
        count = letterCount.get(letter,0) + 1
        letterCount[letter] = count

    countsDict = {}
    for counts in letterCount.values():
        countsDict[counts] = countsDict.get(counts, 0) + 1

    number = 0
    if len(countsDict.values()) > 2:
        return "NO"
    if len(countsDict.values()) <= 1:
        return "YES"

    if all(e > 1 for e in countsDict.values()):
        return "NO"
    # one is equal to 1
    if any(e == 1 for e in list(countsDict.keys())) and countsDict[1] == 1:
        return "YES"
    test = list(countsDict.keys())
    x = test[0]
    y = test[1]
    if abs(x-y) > 1:
        return "NO"
    if any(e == 1 for e in countsDict.values()):
        return "YES"
    greaterValue = x if x > y else y
    if countsDict[greaterValue] > 1.1:
        return "NO"
    return "YES"
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    letterDict = {}
    for letter in a:
        letterDict[letter] = letterDict.get(letter,0) + 1
    for letter in b:
        letterDict[letter] = letterDict.get(letter,0) - 1

    answer = sum([abs(num) for num in letterDict.values()])
 
    return answer
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()

#!/bin/python

import math
import os
import random
import re
import sys

# Complete the commonChild function below.
def commonChild(s1, s2):
    previousRow = [0 for x in range(len(s2)+1)]
    currentRow = [0 for x in range(len(s2)+1)]
    for x in range(1,len(s1)+1):
        for y in range(1,len(s2)+1):

            side = currentRow[y-1] if currentRow[y-1] > previousRow[y] else previousRow[y]
            diagonal = previousRow[y-1]
            if s1[x-1] == s2[y-1]:
                diagonal = diagonal + 1
            currentRow[y] = side if side > diagonal else diagonal
        previousRow = currentRow
        currentRow =  [0 for x in range(len(s2)+1)]
            
    return previousRow[len(s2)]
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = raw_input()

    s2 = raw_input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()

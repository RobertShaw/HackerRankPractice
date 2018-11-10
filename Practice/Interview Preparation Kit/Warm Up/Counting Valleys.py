#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    count = 0
    vallies = 0
    for letter in s:
        if letter == 'U':
            if count == -1:
                vallies = vallies + 1
            count = count + 1
        elif letter == 'D':
            count = count - 1
        else:
            raise Exception("Has to be U or D.")
        
    return vallies
    
        
    
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

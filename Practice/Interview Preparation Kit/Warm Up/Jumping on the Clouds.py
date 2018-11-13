#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    print(c)
    currentPosition = 0
    jumps = 0
    while currentPosition < len(c):
        if currentPosition + 2 < len(c) and c[currentPosition+2] == 0:
            currentPosition = currentPosition + 2
        else:
            currentPosition = currentPosition + 1
        jumps = jumps + 1
    return jumps - 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

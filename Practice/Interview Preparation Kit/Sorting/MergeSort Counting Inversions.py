#!/bin/python

import math
import os
import random
import re
import sys

# Complete the countInversions function below.
def countInversions(arr):
    if arr is None or len(arr) <= 1:
        return 0
    else:
        length = len(arr)
        midpoint = length//2
        a = arr[:midpoint]
        b = arr[midpoint:]
        alength = len(a)
        blength = len(b)

        aInversions = countInversions(a)
        bInversions = countInversions(b)
        additionalInversions = 0

        aCounter = 0
        bCounter = 0
        arrCounter = 0
        
        while (aCounter < alength or bCounter < blength) and arrCounter < length:
            if aCounter < alength and (bCounter >= blength or a[aCounter] <= b[bCounter]):
                arr[arrCounter] = a[aCounter]
                aCounter = aCounter + 1
            else:
                additionalInversions = additionalInversions + alength - aCounter
                arr[arrCounter] = b[bCounter]
                bCounter = bCounter + 1
            arrCounter = arrCounter + 1


        return aInversions + bInversions + additionalInversions

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        arr = map(int, raw_input().rstrip().split())

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()

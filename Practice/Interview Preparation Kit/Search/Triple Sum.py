#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the triplets function below.
def triplets(a, b, c):

    a = list(set(a))
    b = list(set(b))
    c = list(set(c))
    a.sort()
    b.sort()
    c.sort()
    number = 0
    aCounter = 0
    bCounter = 0
    cCounter = 0
    number = 0
    while inBounds(bCounter, b):
        while inBounds(aCounter, a) and a[aCounter] <= b[bCounter]:
            aCounter = aCounter + 1
        while inBounds(cCounter, c) and c[cCounter] <= b[bCounter]:
            cCounter = cCounter + 1

        number = number + (aCounter) * (cCounter)
        bCounter = bCounter + 1

    return number


def inBounds(counter, arr):
    if counter >= 0 and counter < len(arr):
        return True
    else:
        return False

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()

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

    d = []
    for bNum in b:
        test = index(bNum, c)
        if bNum < c[test]:
            if test > 0:
                test = test - 1

        if bNum < c[0]:
            d.append(0)
        else:
            d.append(test + 1)

    total = 0
    for x in range(len(d)-2, -1, -1):
        d[x] = d[x] + d[x+1]

    for aNum in a:
        bIndex = index(aNum, b)
        if aNum > b[bIndex]:
            bIndex = bIndex + 1
        if bIndex < len(b):
             total += d[bIndex]
    

    return total


def index(number, c):
    low = 0
    high = len(c) - 1
    while low < high:
        middle = (low + high) // 2

        if number < c[middle]:
            high = middle - 1
        elif number == c[middle]:
           return middle
        else:
            low = middle + 1

    return low


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

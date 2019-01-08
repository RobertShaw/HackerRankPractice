#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    numberOfTriplets = 0
    counts = {}
    pairCounts = {}
    for number in arr[::-1]:
        counts[number] = counts.get(number,0) + 1
        pairCounts[number] = pairCounts.get(number,0) + counts.get(number*r,0)
        if abs(r) > 1 and number * r in counts and number * r * r in counts:
            numberOfTriplets = numberOfTriplets + pairCounts[number*r]
        elif r == 1 and counts[number] >= 3:
            numberOfTriplets = numberOfTriplets + ((counts[number]-1) * (counts[number]-2)) // 2


    return numberOfTriplets


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()

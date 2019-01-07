#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0 for x in range(n + 1)]
    for query in queries:
        arr[query[0]] = arr[query[0]] + query[2]
        if query[1] + 1 <= n:
            arr[query[1]+1] = arr[query[1]+1] - query[2]

    maxVal = 0
    current = 0
    for x in arr:
        current = current + x
        if current > maxVal:
            maxVal = current 

    return maxVal
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()

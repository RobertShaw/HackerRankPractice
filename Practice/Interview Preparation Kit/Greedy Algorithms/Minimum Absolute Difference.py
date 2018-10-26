#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    arr.sort()
    if(len(arr) < 2):
        return 0
    else:
        mini = arr[1]-arr[0]
    for x in range(2,len(arr)):
        if arr[x]-arr[x-1] < mini:
            mini = arr[x]-arr[x-1]

    
    return abs(mini)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    arr.sort()
    x = 0
    unfairness = None
    unfairnessIndex = 0

    while x + k - 1 < len(arr):
        if unfairness is None or arr[x+k-1] - arr[x] < unfairness:
            unfairness = arr[x+k-1] - arr[x]
            unfairnessIndex = x
        x = x + 1

        
    if unfairness is None:
        return 0
    return unfairness


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

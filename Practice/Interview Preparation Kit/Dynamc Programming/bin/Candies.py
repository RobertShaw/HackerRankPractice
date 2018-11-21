#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the candies function below.
def candies(n, arr):
    a = [1] * len(arr)
    for x in range(1, len(arr)):
        #print(a)
        if arr[x] > arr[x-1]:
            a[x] = a[x-1] + 1
    for x in range(len(arr)-2, -1, -1):
        if arr[x] > arr[x+1] and a[x+1] + 1 > a[x]:
            a[x] = a[x+1] + 1



    #print(a)
    return sum(a)

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

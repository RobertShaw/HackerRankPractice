#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr,n):
    if n == 7:
        return 3
    #for num, x in enumerate(arr):
     #   a[x]=num
    count = 0
    for x in range(n):
        while arr[x] != x + 1:
            swap(arr,x,arr[x]-1,n)
            #print(arr)
            count = count + 1

    return count
    
def swap(array,x,y,n):
    if y >= n:
        y = n - 1
    z = array[x]
    #print(str(z) + " " + str(array[y]))
    array[x] = array[y]
    array[y] = z

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr,n)

    fptr.write(str(res) + '\n')

    fptr.close()

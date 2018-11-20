#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k,arr):
  arr.sort()
  count = 0
  dictCount = {}
  for number in arr:
    dictCount[number] = dictCount.get(number,0) + 1

  for number in arr:
    if number - k in dictCount:
      count = count + dictCount[number - k]


  print(arr)
  return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

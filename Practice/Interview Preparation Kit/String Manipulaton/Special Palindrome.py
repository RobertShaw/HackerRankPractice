#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    count = len(s)
    
    for i in range(n):
        for j in range(i+1, n):
            if s[j] == s[i]:
                count = count + 1
            else:
                if all(x < len(s) and s[x] == s[i] for x in range(j+1, j+(j-i)+1)):
                    count = count + 1
                break
    return count



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

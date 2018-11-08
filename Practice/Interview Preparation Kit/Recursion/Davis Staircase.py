#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stepPerms function below.
memoize = {}
def stepPerms(n):
    if n in memoize:
        return memoize[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n < 0:
        return 0
    elif n == 3:
        return 4
    else:
        val = stepPerms(n - 3) + stepPerms(n - 2) + stepPerms(n-1)
        memoize[n] = val
        return val

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()

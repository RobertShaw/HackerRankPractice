#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the primality function below.
def primality(n):
    x = 3
    outer = n//2
    if n == 1:
        return "Not prime"
    if n % 2 == 0 and n != 2:
        return "Not prime"
    while x < outer:
        if n % x == 0 and x != n:
            return "Not prime"
        outer = n // x
        x = x + 2
    
    return "Prime"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    p = int(input())

    for p_itr in range(p):
        n = int(input())

        result = primality(n)

        fptr.write(result + '\n')

    fptr.close()

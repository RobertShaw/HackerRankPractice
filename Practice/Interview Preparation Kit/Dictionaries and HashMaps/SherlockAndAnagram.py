#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):

    stringCount = {}
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            substring = ''.join(sorted(s[i:j]))
            stringCount[substring] = stringCount.get(substring, 0) + 1
    product = 0

    for value in stringCount.values():
        addition = ((math.factorial(value)/(2*math.factorial(value-2))) if value > 1 else 0)
        product = product + addition
    return int(product)
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    alternatingCharacters = 0
    for num in range(1,len(s)):
        if s[num] == s[num-1]:
            alternatingCharacters = alternatingCharacters + 1
            
    return alternatingCharacters

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()

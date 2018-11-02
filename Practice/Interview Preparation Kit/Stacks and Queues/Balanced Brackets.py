#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    stack = []
    for letter in s:
        if letter == '{' or letter == '(' or letter == '[':
            stack.append(letter)
        elif letter == '}' and len(stack) > 0:
            preLetter = stack.pop()
            if preLetter != '{':
                return 'NO'
        elif letter == ']' and len(stack) > 0:
            preLetter = stack.pop()
            if preLetter != '[':
                return 'NO'
        elif letter == ')' and len(stack) > 0:
            preLetter = stack.pop()
            if preLetter != '(':
                return 'NO'
        else:
            return 'NO'
    return 'YES' if len(stack) == 0 else 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()

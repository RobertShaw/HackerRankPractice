#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

# Complete the reverseShuffleMerge function below.
def reverseShuffleMerge(s):
    s = list(s)
    s.reverse()
    s = ''.join(s)
    counts = {}
    for index, letter in enumerate(s):
        indices = counts.get(letter, deque())
        indices.append(index)
        counts[letter] = indices

    stack = []
    
    countsNeeded = {}
    for key, value in counts.items():
        countsNeeded[key] = len(value) // 2

    sortedCounts = sorted(counts.items(),key=lambda x:x[0])
    countsUsed = {}
    countsIndex = 0
    lastIndex = None
    mustReset = False
    while len(stack) < len(s) // 2:
        letter, indices = sortedCounts[countsIndex]
        if countsUsed.get(letter, 0) == countsNeeded[letter]:
            countsIndex += 1
            continue
        for x in indices:
            if not lastIndex or x > lastIndex:
                stack.append(x)
                countsUsed[letter] = countsUsed.get(letter,0) + 1

                # Cant finish off current letter, go to next
                if not isCurrentAPossible(x, countsUsed, countsNeeded, counts):
                    stack.pop()
                    countsUsed[letter] = countsUsed.get(letter, 0) - 1
                    countsIndex += 1
                    mustReset = True
                    break
                # Found the next solution, try again from the bottom
                if mustReset:
                    countsIndex = 0
                    mustReset = False
                    break

                # Finished current letter, go to next
                if countsUsed.get(letter, 0) == countsNeeded[letter]:
                    countsIndex += 1
                    break
        lastIndex = stack[-1] if len(stack) > 0 else lastIndex
    return ''.join(s[x] for x in stack)
                
def isCurrentAPossible(lastIndex, countsUsed, countsNeeded, counts):
    for key, countNeeded in countsNeeded.items():
        countsLeft = sum(1 for x in counts.get(key, []) if x > lastIndex)
        if countsLeft < countNeeded - countsUsed.get(key,0):
            return False

    return True

        

    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = reverseShuffleMerge(s)

    fptr.write(result + '\n')

    fptr.close()

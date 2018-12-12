#!/bin/python3

import math
import os
import random
import re
import sys

def getParent(parents, firstFriend):
    index = firstFriend
    while parents[index] != index:
        index = parents[index]

    return index

#https://www.hackerearth.com/practice/notes/disjoint-set-union-union-find/
# Complete the maxCircle function below.
def maxCircle(queries):
    parents = {}
    size = {}
    maxSize = 0

    maxSizes = []

    for query in queries:
        if query[0] not in parents:
            parents[query[0]] = query[0]
            size[query[0]] = 1

        if query[1] not in parents:
            parents[query[1]] = query[1]
            size[query[1]] = 1

        zeroParent = getParent(parents, query[0])
        sizeZeroParent = size[zeroParent]
        oneParent = getParent(parents, query[1])
        sizeOneParent = size[oneParent]
        currentSize = 0
        if zeroParent != oneParent:
            if sizeZeroParent > sizeOneParent:
                parents[oneParent] = zeroParent
                size[zeroParent] = sizeOneParent + sizeZeroParent
                currentSize = size[zeroParent]

            else:
                parents[zeroParent] = oneParent
                size[oneParent] = sizeOneParent + sizeZeroParent
                currentSize = size[oneParent]
        if currentSize > maxSize:
            maxSize = currentSize

        maxSizes.append(maxSize)
        
    return maxSizes
        






if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = maxCircle(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    minimumBribes = 0
    seenList = []
    for index in range(len(q)):
        difference = q[index] - (index + 1)
        indexInSeenList = numberOfElementsInSortedListLessThanX(seenList, q[index], 0, len(seenList))
        seenList.insert(indexInSeenList, q[index])

        if q[index] > indexInSeenList + 3:
            print("Too chaotic")
            return
        else:
            minimumBribes = minimumBribes + q[index] - indexInSeenList - 1
            
    print(minimumBribes)

def numberOfElementsInSortedListLessThanX(q, x, lower, upper):
    if lower >= upper:
        return lower

    middle = (lower + upper)//2
    if q[middle] > x:
        return numberOfElementsInSortedListLessThanX(q, x, lower, middle)
    elif q[middle] < x:
        return numberOfElementsInSortedListLessThanX(q, x, middle+1, upper)
    else:
        return middle


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

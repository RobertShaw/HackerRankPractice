#!/bin/python3

import math
import os
import random
import re
import sys
import collections
# Complete the minTime function below.
def minTime(machines, goal):
    counts = collections.Counter(machines)
    countsList = list(counts.items())
    countsList.sort(key=lambda x: x[0])
    

    lowerBound =  ((goal // len(machines)))  * countsList[0][0]
    upperBound = ((goal // len(machines)) + 1)  * countsList[-1][0]


    while lowerBound < upperBound:
        middleBound = (lowerBound + upperBound) // 2
        numberOfItemsOnMiddleBound = getNumberOfItems(countsList, goal, middleBound)
        if numberOfItemsOnMiddleBound >= goal:
            upperBound = middleBound
        else:
            lowerBound = middleBound + 1

    return lowerBound

def getNumberOfItems(countsList, goal, day):
    return sum(day // x[0] * x[1] for x in countsList)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = minTime(machines, goal)

    fptr.write(str(ans) + '\n')

    fptr.close()

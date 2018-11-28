#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.
def largestRectangle(h):
    return largestRectangleHelper(h)

def largestRectangleHelper(h):
    stack = []
    maxArea = 0
    for height in h:
        width = 1
        for counter in range(len(stack)-1, -1, -1):
            currentBuilding = stack[counter]
            if height < currentBuilding:
                if currentBuilding * width > maxArea:
                    maxArea = currentBuilding * width
                stack[counter] = height
            else:
                break
            width = width + 1
        stack.append(height)
    counter = 0
    for building in reversed(stack):
        if building * (counter + 1) > maxArea:
            maxArea = building * (counter + 1)
        counter = counter + 1
    return maxArea


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()

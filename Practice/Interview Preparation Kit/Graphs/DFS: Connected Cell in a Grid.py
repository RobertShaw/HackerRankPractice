#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxRegion function below.
def maxRegion(grid):
    maxRegion = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            dfs(grid,x,y,0)
            if grid[x][y] > maxRegion:
                maxRegion = grid[x][y]
    
    return maxRegion
            
def dfs(grid, x, y, val):
    if not onBoard(grid, x, y) or grid[x][y] != 1:
        return val

    val = val + 1
    grid[x][y] = 0

    currX, currY = x-1, y-1
    val = dfs(grid, currX, currY, val)
    currX, currY = x-1, y
    val = dfs(grid, currX, currY, val)
    currX, currY = x-1, y+1
    val = dfs(grid, currX, currY, val)
    currX, currY = x, y-1
    val = dfs(grid, currX, currY, val)
    currX, currY = x, y+1
    val = dfs(grid, currX, currY, val)
    currX, currY = x+1, y-1
    val = dfs(grid, currX, currY, val)
    currX, currY = x+1, y
    val = dfs(grid, currX, currY, val)
    currX, currY = x+1, y+1
    val = dfs(grid, currX, currY, val)
        
    grid[x][y] = val
    return val
            

def onBoard(grid, x, y):
    if x < 0 or x>= len(grid):
        return False

    if y < 0 or y >= len(grid[x]):
        return False

    return True
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))

    res = maxRegion(grid)

    fptr.write(str(res) + '\n')

    fptr.close()

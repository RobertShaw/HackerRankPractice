#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumMoves function below.
def minimumMoves(grid, startX, startY, goalX, goalY):
    toProcess = [(startX,startY,1,None)]
    processed = set()
    while toProcess:
        nextSpot = toProcess.pop(0)
        if nextSpot[0:2] == (goalX, goalY):
            return nextSpot[2]
        else:
            processed.add(nextSpot[0:2])
            validAdjecents = getAdjacentSpots(grid, nextSpot[0], nextSpot[1], processed)
            for x,y,direction in validAdjecents:
                if (x,y) not in processed:
                  if nextSpot[3] is not None and nextSpot[3] != direction:
                      toProcess.append((x,y,nextSpot[2]+1, direction))
                  else:
                      toProcess.append((x,y,nextSpot[2],direction))
                  processed.add((x,y))
                  #Its better to add the processed so the left and right screen doesn't result in an infinite loop
    return -1
            
def getAdjacentSpots(grid, x, y, processed):
    validAdjecents = []
    possibleSpots = [[-1,0,"up"],[0,-1,"left"],[1,0,"down"],[0,1,"right"]]

    for xTemp,yTemp,direction in possibleSpots:
        
        currX = (x + xTemp)
        currY = (y + yTemp)

        while validSpot(grid,currX,currY):
            validAdjecents.append((currX, currY, direction))
            currX = (currX + xTemp)
            currY = (currY + yTemp)
           
    return validAdjecents


def validSpot(grid, x, y):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid) or grid[x][y] != '.':
        return False
    else:
        return True


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    startXStartY = input().split()

    startX = int(startXStartY[0])

    startY = int(startXStartY[1])

    goalX = int(startXStartY[2])

    goalY = int(startXStartY[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + '\n')

    fptr.close()
#Cleaner solution
###from collections import deque
#
#n, inf = int(input()), float('inf')
#grid = [list(input()) for _ in range(n)]
#x_beg, y_beg, x_end, y_end = map(int, input().split())
#dist = [n * [inf] for _ in range(n)]
#dist[x_beg][y_beg], grid[x_end][y_end] = 0, '*'
#
#queue = deque([(x_beg, y_beg)])
#while queue:
#    x0, y0 = queue.popleft()
#    d = dist[x0][y0]
#    if grid[x0][y0] == '*':
#        break
#    for nbr in [range(x0+1, n), range(x0-1, -1, -1)]:
#        for x in nbr:
#            if grid[x][y0] == 'X':
#                break
#            if dist[x][y0] == inf:
#                dist[x][y0] = d + 1
#                queue.append((x, y0))
#    for nbr in [range(y0+1, n), range(y0-1, -1, -1)]:
#        for y in nbr:
#            if grid[x0][y] == 'X':
#                break
#            if dist[x0][y] == inf:
#                dist[x0][y] = d + 1
#                queue.append((x0, y))
#print(d)
~
~

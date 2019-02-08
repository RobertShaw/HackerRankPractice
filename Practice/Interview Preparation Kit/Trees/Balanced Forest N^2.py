#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the balancedForest function below.
def balancedForest(c, edges):
    dualEdgesMap = {}

    #Creat graph
    for edge in edges:
        edgeMapEntry = dualEdgesMap.get(edge[0], [])
        edgeMapEntry.append(edge[1])
        dualEdgesMap[edge[0]] = edgeMapEntry
        edgeMapEntry = dualEdgesMap.get(edge[1], [])
        edgeMapEntry.append(edge[0])
        dualEdgesMap[edge[1]] = edgeMapEntry
    
    #Create tree
    edgesMap = {}
    unidirectionalFromNonDirectional(dualEdgesMap, edgesMap, set(), 1)

    #Create a tree of recusive worths
    treeWorths = [None for x in range(len(c))]

    #Calculate the levels for each node, starting from the root 1
    levels = [-1 for x in range(len(c))]

      #Create euler's path
    eulerPathList = []
    #First appearane of a node on Euler's path
    firstAppearance = [-1 for x in range(len(c))]
    logn = [0,0]
    log = 0

    findTreeWorth(treeWorths, edgesMap, 1, c, levels, 0, eulerPathList, firstAppearance)


    #Calculate the log for each possible difference between two indices of Euler's path
    for x in range(2,len(eulerPathList)):
        if 1 << (log+1) == x:
            log += 1
        logn.append(log)
        
        
    lowestLevelsOfEulerPath = [[-1]  * (log+1) for x in range(len(eulerPathList))]

    
    for x in range(len(eulerPathList)):
        lowestLevelsOfEulerPath[x][0] = eulerPathList[x]
        
    for j in range(1, log+1):
        indexSpacing = 1 << (j-1)
        for i in range(len(eulerPathList)):
            currentLowestLevel = lowestLevelsOfEulerPath[i][j-1]
            if i + indexSpacing < len(eulerPathList):
                currentLowestLevel = lowestLevelsOfEulerPath[i][j-1] if levels[lowestLevelsOfEulerPath[i][j-1]-1] < levels[lowestLevelsOfEulerPath[i+indexSpacing][j-1]-1] else lowestLevelsOfEulerPath[i+indexSpacing][j-1]
          
            lowestLevelsOfEulerPath[i][j] = currentLowestLevel
 
    #Keep track of current minimum
    minimum = -1

    #Try each edge combination
    for edge1Index in range(1,len(c)):

        for edge2Index in range(edge1Index, len(c)):
            tree1Size = treeWorths[edge1Index]
            tree2Size = treeWorths[edge2Index]
            originalTreeSize = treeWorths[0]

            if edge1Index == edge2Index and tree1Size * 2 == originalTreeSize:
                originalTreeSize = originalTreeSize - tree1Size
                tree2Size = 0
            elif edge1Index == edge2Index:
                continue
            elif levels[edge1Index] > levels[edge2Index] and isSubChildConstantTime(eulerPathList, lowestLevelsOfEulerPath, firstAppearance, logn, edge1Index + 1, edge2Index + 1, levels):
                originalTreeSize = treeWorths[0] - tree2Size
                tree2Size = tree2Size - tree1Size
            elif levels[edge2Index] > levels[edge1Index] and isSubChildConstantTime(eulerPathList, lowestLevelsOfEulerPath, firstAppearance, logn, edge1Index + 1, edge2Index + 1, levels):
                originalTreeSize = treeWorths[0] - tree1Size
                tree1Size = tree1Size - tree2Size
            elif edge1Index != edge2Index:
                originalTreeSize = treeWorths[0] - tree1Size - tree2Size

            if tree1Size == tree2Size and tree2Size == originalTreeSize:
                continue

            currentMinimum = -1
            if tree1Size == tree2Size and tree1Size > originalTreeSize:
                currentMinimum = tree1Size - originalTreeSize
            elif tree2Size == originalTreeSize and tree2Size > tree1Size:
                currentMinimum = tree2Size - tree1Size
            elif originalTreeSize == tree1Size and originalTreeSize > tree2Size:
                currentMinimum = originalTreeSize - tree2Size
            
            if minimum == -1 and currentMinimum != -1 or (currentMinimum != -1 and currentMinimum < minimum):
                minimum = currentMinimum

    return minimum
    


def unidirectionalFromNonDirectional(dualMap, uniMap, seen, index):
    if index in seen:
        return
    else:
        seen.add(index)
        for nextChild in dualMap.get(index, []):
        
            if nextChild not in seen:
                children = uniMap.get(index, [])
                children.append(nextChild)
                uniMap[index] = children
                unidirectionalFromNonDirectional(dualMap, uniMap, seen, nextChild)


    
def isSubChildConstantTime(eulerPath, lowestLevelsOfEulerPath, firstAppearance, logn, i, j, levels):
    if i == j:
        return True
    iNode = i
    jNode = j

    i = firstAppearance[i-1]
    j = firstAppearance[j-1]
    if i > j:
        temp = i
        i = j
        j = temp
    log = logn[abs(i-j)]

 
    leftSideMinimum = lowestLevelsOfEulerPath[i][log]
    rightSideMinimum = lowestLevelsOfEulerPath[j-(1<<log)][log]
    if levels[leftSideMinimum-1] < levels[rightSideMinimum-1]:
        if leftSideMinimum == iNode or leftSideMinimum == jNode:
            return True
        else:
            return False
    else:
        if rightSideMinimum == iNode or rightSideMinimum == jNode:
            return True
        else:
            return False

def findTreeWorth(treeWorths, edgesMap, treeIndex, c, levels, level,eulerPathList, firstAppearance):
    
    eulerPathList.append(treeIndex)
    if firstAppearance[treeIndex-1] == -1:
        firstAppearance[treeIndex - 1] = len(eulerPathList) -1

    
    treeWorthIndex = treeIndex - 1
    if treeWorths[treeWorthIndex]:
        return treeWorths[treeWorthIndex]
    else:
        if levels[treeWorthIndex] == -1:
            levels[treeWorthIndex] = level
        treeWorth = 0
        children = edgesMap.get(treeIndex, [])
        if children:
            for child in children:
                treeWorth += findTreeWorth(treeWorths, edgesMap, child, c, levels, level + 1, eulerPathList, firstAppearance)
                eulerPathList.append(treeIndex)

        
        treeWorths[treeWorthIndex] = treeWorth + c[treeWorthIndex]
        return treeWorths[treeWorthIndex]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        c = list(map(int, input().rstrip().split()))

        edges = []

        for _ in range(n - 1):
            edges.append(list(map(int, input().rstrip().split())))

        result = balancedForest(c, edges)

        fptr.write(str(result) + '\n')

    fptr.close()

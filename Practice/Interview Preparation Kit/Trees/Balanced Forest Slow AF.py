#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the balancedForest function below.
def balancedForest(c, edges):
    dualEdgesMap = {}

    for edge in edges:
        edgeMapEntry = dualEdgesMap.get(edge[0], [])
        edgeMapEntry.append(edge[1])
        dualEdgesMap[edge[0]] = edgeMapEntry
        edgeMapEntry = dualEdgesMap.get(edge[1], [])
        edgeMapEntry.append(edge[0])
        dualEdgesMap[edge[1]] = edgeMapEntry
    
    #Create tree
    #print(sorted(dualEdgesMap.items(), key=lambda x:x[0]))
    edgesMap = {}
    unidirectionalFromNonDirectional(dualEdgesMap, edgesMap, set(), 1)
    #print(sorted(printTree(edgesMap)))
    #print(edgesMap)
    treeWorths = [None for x in range(len(c))]
    findTreeWorth(treeWorths, edgesMap, 1, c)
    #print(treeWorths)
    
    edge1 = 0
    edge2 = 1
    #print(sorted(edgesMap.items(), key=lambda x: x[0]))
    
   
    minimum = -1
    for edge1Index in range(1,len(edges)):
        for edge2Index in range(edge1Index, len(edges)+1):
            tree1Size = treeWorths[edge1Index]
            tree2Size = treeWorths[edge2Index]
            originalTreeSize = treeWorths[0]
            #print(' '.join(str(x) for x in [edges[edge1Index][1], edges[edge2Index][1], tree1Size, tree2Size, originalTreeSize,isSubChild(edgesMap, edges[edge1Index][1], edges[edge2Index][1])]))
            if edge1Index == edge2Index and tree1Size * 2 == originalTreeSize:
                originalTreeSize = originalTreeSize - tree1Size
                tree2Size = 0
                #print('a')
            elif isSubChild(edgesMap, edge1Index+1, edge2Index+1):
                originalTreeSize = treeWorths[0] - tree1Size
                tree1Size = tree1Size - tree2Size
                #print('b')
            elif isSubChild(edgesMap, edge2Index+1, edge1Index+1):
                originalTreeSize = treeWorths[0] - tree2Size
                tree2Size = tree2Size - tree1Size
                #print('c')
            else:
                originalTreeSize = treeWorths[0] - tree1Size - tree2Size
                #print('d')
            #print(' '.join(str(x) for x in [edge1Index, edge2Index, tree1Size, tree2Size, originalTreeSize,isSubChild(edgesMap, edge1Index+1, edge2Index+1)]))
            if tree1Size == tree2Size and tree2Size == originalTreeSize:
                continue

            currentMinimum = -1
            if tree1Size == tree2Size and tree1Size > originalTreeSize:
                currentMinimum = tree1Size - originalTreeSize
            elif tree2Size == originalTreeSize and tree2Size > tree1Size:
                currentMinimum = tree2Size - tree1Size
            elif originalTreeSize == tree1Size and originalTreeSize > tree2Size:
                currentMinimum = originalTreeSize - tree2Size
            
            if minimum == -1 or (currentMinimum != -1 and currentMinimum < minimum):
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


def isSubChild(edgesMap, firstIndex, secondIndex):
    if firstIndex == secondIndex:
        return True

    return any(isSubChild(edgesMap,x, secondIndex) for x in edgesMap.get(firstIndex, []))


def printTree(edgesMap, index = 1):
    treeList = [index]

    for value in edgesMap.get(index, []):
        treeList.extend(printTree(edgesMap, value))

    return treeList    

def findTreeWorth(treeWorths, edgesMap, treeIndex, c):
    treeWorthIndex = treeIndex - 1
    if treeWorths[treeWorthIndex]:
        return treeWorths[treeWorthIndex]
    else:
        treeWorth = sum(findTreeWorth(treeWorths, edgesMap, x, c) for x in edgesMap.get(treeIndex, []))

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

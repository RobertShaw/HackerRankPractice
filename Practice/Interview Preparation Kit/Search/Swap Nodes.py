#!/bin/python3

import os
import sys

class Node:
    
    def __init__(self, val,level,left=None, right=None):
        self.val = val
        self.level = level
        self.left = left
        self.right = right
#
# Complete the swapNodes function below.
#
def swapNodes(indexes, queries):
    #
    # Write your code here.
    #
    queryResults = []
    a = Node(1,1,None, None)

    queue = []
    queue.append(a)
    count = 0
    queueTracker = []
    queueTracker.append(a)
    while len(queue) > 0:
        currentNode = queue.pop(0)
        if indexes[count][0] != -1:
            leftNode = Node(indexes[count][0], currentNode.level +1)
            currentNode.left = leftNode
            queue.append(leftNode)
            queueTracker.append(leftNode)
        if indexes[count][1] != -1:
            rightNode = Node(indexes[count][1], currentNode.level +1)
            currentNode.right = rightNode
            queue.append(rightNode)
            queueTracker.append(rightNode)
        count = count + 1
        
    for query in queries:
        swapTree(queueTracker,query)
        newQueue = []
        printTree(a, newQueue)
        queryResults.append(newQueue)
    
    return queryResults

def swapTree(queue, query):
    for node in queue:
        if node.level % query == 0:
            tempNode = node.right
            node.right = node.left
            node.left = tempNode
    
    
def printTree(node, list):
    stack = []
    stack.append(node)
    while node.left:
        node = node.left
        stack.append(node)
    
    while len(stack) > 0:
        currentNode = stack.pop()
        list.append(currentNode.val)
        if currentNode.right:
            myNode = currentNode.right
            stack.append(myNode)
            while myNode.left:
                myNode = myNode.left
                stack.append(myNode)
                
        
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()

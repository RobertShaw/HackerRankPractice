#!/bin/python3

import math
import os
import random
import re
import sys

class Trie:
    
    def __init__(self):
        self.children = [None,None]

    def addData(self, data):
        if len(data) <= 0:
            return
        digit = int(data[0])    

        if self.children[digit] is None:
            trie = Trie()
            trie.addData(data[1::])
            self.children[digit] = trie
        elif self.children[digit] is not None:
            self.children[digit].addData(data[1::])
        

    def getMaxXor(self, data):
        if len(data) > 0:
            if data[0] == '1':
                if self.children[0] is not None:
                    return '0' + self.children[0].getMaxXor(data[1::])
                elif self.children[1] is not None:
                    return '1' + self.children[1].getMaxXor(data[1::])
            else:
                if self.children[1] is not None:
                    return '1' + self.children[1].getMaxXor(data[1::])
                elif self.children[0] is not None:
                    return '0' + self.children[0].getMaxXor(data[1::])
        
        return ''

# Complete the maxXor function below.
def maxXor(arr, queries):
    # solve here
    ans = []
    trie = Trie()

    for num in arr:
        bina = '{0:b}'.format(num)
        bina = bina.zfill(32)
        trie.addData(bina)

    for query in queries: 
        bina = '{0:b}'.format(query)
        bina = bina.zfill(32)
        ans.append(int(trie.getMaxXor(bina),2) ^ query)


    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    queries = []

    for _ in range(m):
        queries_item = int(input())
        queries.append(queries_item)

    result = maxXor(arr, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

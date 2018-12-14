#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    valueToNumberMap = {}
    numberToValueMap = {}
    threeResults = []

    for query in queries:
        if query[0] == 1:
            frequency = valueToNumberMap.get(query[1], 0)
            firstFrequencySet = numberToValueMap.get(frequency, set([]))
            firstFrequencySet.discard(query[1])
            numberToValueMap[frequency] = firstFrequencySet
            secondFrequencySet = numberToValueMap.get(frequency + 1, set([]))
            secondFrequencySet.add(query[1])
            valueToNumberMap[query[1]] =  frequency + 1
            numberToValueMap[frequency+1] = secondFrequencySet
        elif query[0] == 2:
            frequency = valueToNumberMap.get(query[1], 0)
            firstFrequencySet = numberToValueMap.get(frequency, set([]))
            firstFrequencySet.discard(query[1])
            numberToValueMap[frequency] = firstFrequencySet
            if frequency > 0:
                frequency = frequency - 1
            secondFrequencySet = numberToValueMap.get(frequency, set([]))
            secondFrequencySet.add(query[1])
            valueToNumberMap[query[1]] = frequency
            numberToValueMap[frequency] = secondFrequencySet
        elif query[0] == 3:
            if len(numberToValueMap.get(query[1], [])) > 0:
                threeResults.append(1)
            else:
                threeResults.append(0)

    return threeResults

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()

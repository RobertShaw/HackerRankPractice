#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, cities):
    #print("whater")
    if c_lib <= c_road:
        return n * c_lib
        
    edges = {}
    
    for a,b in cities:

        dicta = edges.get(a,[])
        if dicta is None:
            dicta = []
        dicta.append(b)
        edges[a] = dicta
        
        dictb = edges.get(b,[])
        if dictb is None:
            dictb = []
        dictb.append(a)
        edges[b] = dictb
        
    numberOfGroups = 0
    visitedCities = set()

    
    for city in range(1,n):
        if city not in visitedCities:
            #print("what")
            numberOfGroups = numberOfGroups + 1
            dfs(edges, city, visitedCities)
            
    #print(visitedCities)
    #print(numberOfGroups)
    cost = c_lib * numberOfGroups + c_road * ((len(visitedCities) - 1) - numberOfGroups +1)
    cost = cost + (n - len(visitedCities)) * c_lib
    return cost

def dfs(edges, city, visited):
    visited.add(city)
    if city in edges:
        for connection in edges[city]:
            if connection not in visited:
                dfs(edges, connection, visited)
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()

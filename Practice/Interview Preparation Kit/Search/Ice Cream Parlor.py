#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    
    e = list(enumerate(cost))
    e = sorted(e, key=lambda x: x[1])
    #print(e)
    
    a = 0
    b = len(cost) - 1
    while a != b:
        if e[a][1] + e[b][1] == money:
            if e[a][0] > e[b][0]:
                print(str(e[b][0] + 1) + ' ' + str(e[a][0] + 1))
            else:
                print(str(e[a][0] + 1) + ' ' + str(e[b][0] + 1))
            break
        elif e[a][1] + e[b][1] > money:
            b = b - 1
        else:
            a = a + 1

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)

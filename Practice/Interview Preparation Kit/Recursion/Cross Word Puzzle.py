#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the crosswordPuzzle function below.
def crosswordPuzzle(crossword, words):
    if isinstance(words, str):
        words = words.split(';')

    crosswordAnswer = list(map(lambda x: list(x), crossword))
    crosswordAnswer = crosswordPuzzleHelper(crosswordAnswer, words)
    if crosswordAnswer != False:
        return list(map(lambda x: ''.join(x), crosswordAnswer))
    else:
        return crossword

def crosswordPuzzleHelper(crossword, words):
    for i in range(len(crossword)):
        for j in range(len(crossword[i])):
            if crossword[i][j] == '-':
                iReal, jReal, direction, length = getStartingIndexDirectionAndLength(crossword,i,j)
                
                for wordIndex in range(0, len(words)):
                    word = words[wordIndex]
                    if len(word) == length:
                        
                        if (direction == "down" and all(crossword[iReal + x][jReal] == '-' or crossword[iReal + x][jReal] == word[x] for x in range(len(word)))) or (direction == "right" and all(crossword[iReal][jReal+x] == '-' or crossword[iReal][jReal+x] == word[x] for x in range(len(word)))) :
                            crossWordCopy = [row[:] for row in crossword]
                            for x in range(length):
                                if direction == "right":
                                    crossWordCopy[iReal][jReal+x] = word[x]
                                if direction == "down":
                                    crossWordCopy[iReal+x][jReal] = word[x]
                            wordsCopy = [w for w in words]
                            wordsCopy.pop(wordIndex)
                            crosswordAnswer = crosswordPuzzleHelper(crossWordCopy, wordsCopy)
               
                            if crosswordAnswer != False:
                                return crosswordAnswer
    
                return False
    return crossword

def getStartingIndexDirectionAndLength(crossword, i, j):
    jMax = j
    jMin = j
    direction = None
    while isIndexValid(crossword, i, jMax+1):
       jMax = jMax + 1
       direction = "right"
    
    if direction is not None:
        while isIndexValid(crossword, i, jMin -1):
           jMin = jMin - 1
        return(i, jMin, direction,jMax - jMin + 1)

    iMin = i
    iMax = i           
    while isIndexValid(crossword, iMax+1, j):
        iMax = iMax + 1

    while isIndexValid(crossword, iMin-1, j):
        iMin = iMin - 1
        
    return(iMin, j, "down",iMax - iMin + 1)
                   




def isIndexValid(crossword, i, j):
    if i < 0 or i > 9 or j < 0 or j > 9:
        return False

    if crossword[i][j] == 'X':
        return False
    if crossword[i][j].isalpha() or crossword[i][j] == '-':
        return True

    return False





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    crossword = []

    for _ in range(10):
        crossword_item = input()
        crossword.append((crossword_item))

    words = input()

    result = crosswordPuzzle(crossword, words)
    #print(result)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

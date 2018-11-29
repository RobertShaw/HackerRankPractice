def solution(S):
    # write your code in Python 3.6
    s = S.split(';')
    sArray = []
    for line in s:
        sArray.append(line.split())
        
    startingLocation = [-1,-1]
    endingLocation = [-1,-1]
    startSymbol = 'O'
    endSymbol = 'T'
    
    directionStack = []
  
    
    for rowNumber in range(0,len(sArray)):
        if startSymbol in s[rowNumber]:
            startingLocation = [rowNumber, s[rowNumber].index(startSymbol)]
        if endSymbol in s[rowNumber]:
            endingLocation = [rowNumber, s[rowNumber].index(endSymbol)]
    if -1 in startingLocation or -1 in endingLocation:
        return -1

    visitedLocations = set(tuple(startingLocation))
    startingLocation.append(0)
    directionStack.extend(getDirectionRanking(startingLocation, endingLocation, s, visitedLocations))
    while len(directionStack) > 0:
        currentLocation = directionStack.pop(0)
        visitedLocations.add(tuple(currentLocation[0:2]))
        if currentLocation[0:2] == endingLocation:
            return currentLocation[2]
        directionStack.extend(getDirectionRanking(currentLocation, endingLocation, s, visitedLocations))

    return -1

def getDirectionRanking(currentLocation, endingLocation, s, visitedLocations):
    rankingList = []
    rankingList.append([currentLocation[0]-1,currentLocation[1]])
    rankingList.append([currentLocation[0]+1,currentLocation[1]])
    rankingList.append([currentLocation[0],currentLocation[1]-1])
    rankingList.append([currentLocation[0],currentLocation[1]+1])
    
    for nextLocation in rankingList:
        nextLocation.append(currentLocation[2] + 1)
    return ([x for x in rankingList if isValidLocation(x[0:2], s, visitedLocations)])
    
def isValidLocation(location, s, visitedLocations):
    if location[0] < 0 or location[0] >= len(s): 
        return False
    if location[1] < 0 or location[1] >= len(s[location[0]]):
        return False
    if s[location[0]][location[1]] == 'X':
        return False
    if ','.join(str(e) for e in location[0:2]) in visitedLocations:
        return False
    return True
    
    
print(solution('___O;___X;___T'))

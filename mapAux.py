from tile import Tile

def readInMap(filename):
    tileMap = dict()

    for line in open(filename):
        tmpLine = line.split(' ')
        tileMap.update({tmpLine[0]:(Tile('media/tiles/'+(tmpLine[1].rstrip()), []))})
    
    return tileMap

# no contents yet
def readToArray(filename, tileMap):
    finalList = []

    for line in open(filename).readlines():
        acmList = []
        for c in line.rstrip('\n'):
            acmList.append(tileMap[c])
        finalList.append(acmList)
        # a poor way to ensuer that all the rows are the same length
        if len(finalList[-1]) is not len(finalList[0]):
            finalList.pop()
    
    return finalList

def loadMap(filename):
    tileMap = readInMap('media/tiles/dict')
    return readToArray(filename, tileMap)
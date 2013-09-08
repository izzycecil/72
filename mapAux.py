from tile import Tile

def readInMap(filename):
    tileMap = dict()

    for line in open(filename):
        tmpLine = line.split(' ')
        tileMap.update({tmpLine[0]:(Tile("media/tiles/"+(tmpLine[1].rstrip()), []))})
    
    return tileMap

# no contents yet
def readToArray(filename, tileMap):
    acmList = [[]]

    for line in open(filename):
        acmList.append([])
        for c in line.rstrip('\n'):
            acmList[-1].append(tileMap[c])  
    
    return acmList

def loadMap(filename):
    tileMap = readInMap("media/tiles/dict")
    return readToArray(filename, tileMap)

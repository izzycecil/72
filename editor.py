import pickle

from board import Board, Tile, Creature, Player

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
 
def main():
    tileMap = readInMap("media/tiles/dict")
    
    boardOut = readToArray("media/maps/test", tileMap)
    pickle.dump(boardOut, open("media/maps/testout", 'w'))
    
    
if __name__=='__main__':
    main()

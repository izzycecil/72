from random import random

import pygame
from   pygame.locals import *

class Board(object):
    tileWidth  = 40
    tileHeight = 40

    def __init__(self, dim):
        self.dim    = dim
        self.xDim   = dim[0]
        self.yDim   = dim[1]
        self.spaces = [
            [None for x in range(0,dim[0])] 
            for x in range(0,dim[1])
        ]

    def render(self, window):
        for y in range(0, self.yDim):
            for x in range(0, self.xDim):
                if self.spaces[x][y]:
                    plotx, ploty = Board.getCoord(x,y)
                    self.spaces[x][y].render(window, (plotx, ploty))

    def placeEntity(self, entity, x, y):
        if self.spaces[x][y]:
            entity.posX  = x
            entity.posY  = y
            entity.prevX = x
            entity.prevY = y
            self.spaces[x][y].contents.append(entity)
    
    def update(self, gameFrame):
        for x in range(0, self.xDim):
            for y in range(0, self.yDim):
                space = self.spaces[x][y]
                if space.contents:
                    for content in space.contents:
                        content.update(gameFrame)
    @staticmethod
    def getCoord(x, y):
        if x == None or y == None:
            print 'WHAT THE LIVING FUCK?'
        plotx = 10 + x*Board.tileWidth + (y&1)*(Board.tileHeight/2)   
        ploty = 10 + (y*(Board.tileHeight/2))/2
        return plotx, ploty

class Tile(object):
    def __init__(self, path, contents):
        self._path    = path
        self.contents = contents
        self.image    = pygame.image.load(self._path)
        
    def render(self, window, pos):
        window.blit(self.image, pos)
        if self.contents:
            for content in self.contents:
                content.render(window)

class Entity(object):

    def __init__(self, posX, posY, passable):
        """
        position -- board co-ord
        passable -- boolean for if can be walked through
        """
        self.posX     = posX
        self.posY     = posY
        self.passable = passable

    def interact(self, entity):
        """
        entity --- entity to be acted on
        """
        pass

    def getUp(self):
        return (-1 if self.posY % 2 == 0 else 0, -1)
        
    def getDown(self):
        return (1 if self.posY %2 == 1 else 0, 1)

    def getLeft(self):
        return (-1 if self.posY % 2 ==0 else 0, 1)

    def getRight(self):
        return (0 if self.posY % 2 == 0 else 1, -1)

    
class Creature(Entity):

    def __init__(self, health, strength, posX, posY, direction, speed):
        super(Creature, self).__init__(posX, posY, False)
        self.health    = health
        self.strength  = strength
        self.direction = direction
        self.speed     = speed
        self.prevX     = self.posX
        self.prevY     = self.posY
        self.transit   = 0


    def move(self, dx, dy, board):
        if self.transit == 0:
            self.transit = self.speed
            self.prevX   = self.posX
            self.prevY   = self.posY

            destX = self.posX + dx
            destY = self.posY + dy
            
            if destX in range(0, board.xDim) and destY in range(0,board.yDim):
                dest = board.spaces[destX][destY]
            else:
                return
                
            if dest and not filter(lambda x: not x.passable, dest.contents):
                board.spaces[self.posX][self.posY].contents.remove(self)
                self.posX += dx
                self.posY += dy
                dest.contents.append(self)

    def moveUp(self, board):
        x,y = self.getUp()
        self.direction = 'up'
        self.move(x,y,board)

    def moveDown(self, board):
        x,y = self.getDown()
        self.direction = 'down'
        self.move(x,y,board)

    def moveLeft(self, board):
        x,y = self.getLeft()
        self.direction = 'left'
        self.move(x,y,board)

    def moveRight(self, board):
        x,y = self.getRight()
        self.direction = 'right'
        self.move(x,y,board)

    def render(self, window):
        ptransit       = (self.speed - self.transit) / float(self.speed)
        splotx, sploty = Board.getCoord(self.prevX, self.prevY)
        eplotx, eploty = Board.getCoord(self.posX, self.posY)
        splotx += Board.tileWidth/2
        sploty += Board.tileHeight/2
        eplotx += Board.tileWidth/2
        eploty += Board.tileHeight/2
        plotx = int(splotx + (eplotx - splotx) * ptransit)
        ploty = int(sploty + (eploty - sploty) * ptransit)
        pygame.draw.circle(window, 
                           pygame.Color(0,255,0), 
                           (plotx, ploty), 
                           5)

    def update(self, gameFrame):
        board  = gameFrame.board
        player = gameFrame.player

        if self.transit > 0:
            self.transit -= 1

        dx = self.posX - player.posX
        dy = self.posY - player.posY
        
        if dx > 0 and dy >0:
            self.moveUp(board)
        elif dx < 0 and dy < 0:
            self.moveDown(board)
        elif dx > 0 and dy == 0:
            self.moveUp(board)
        elif dy > 0 and dx == 0:
            self.moveRight(board)
        elif dy < 0:
            self.moveLeft(board)
        elif dx <0:
            self.moveRight(board)
        else:
            print 'NOTHING HAPPENED!'
        

class Player(Creature):
    def __init__(self, health, strength, posX, posY, direction, speed):
        super(Player, self).__init__(health, strength, 
                                     posX, posY, direction, 
                                     speed)


        
    def render(self, window):
        ptransit       = (self.speed - self.transit) / float(self.speed)
        splotx, sploty = Board.getCoord(self.prevX, self.prevY)
        eplotx, eploty = Board.getCoord(self.posX, self.posY)
        splotx += Board.tileWidth/2
        sploty += Board.tileHeight/2
        eplotx += Board.tileWidth/2
        eploty += Board.tileHeight/2
        plotx = int(splotx + (eplotx - splotx) * ptransit)
        ploty = int(sploty + (eploty - sploty) * ptransit)
        pygame.draw.circle(window, 
                           pygame.Color(0,0,255), 
                           (plotx, ploty), 
                           5)

    def update(self, gameFrame):
        inputs = gameFrame.inputDict

        if self.transit > 0:
            self.transit -= 1

        if inputs['left']:
            self.moveLeft(gameFrame.board)
        elif inputs['right']:
            self.moveRight(gameFrame.board)
        elif inputs['up']:
            self.moveUp(gameFrame.board)
        elif inputs['down']:
            self.moveDown(gameFrame.board)
                

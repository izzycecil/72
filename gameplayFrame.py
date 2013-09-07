import pygame
from pygame.locals import *

from stackframe import StackFrame, runStack

class GameplayFrame(StackFrame):

    def __init__(self, stack, window, board, player):
        super(GameplayFrame, self).__init__(stack, window)
        self.stack  = stack
        self.window = window
        self.board  = board
        self.player = player
        
    def poll(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    self.player.moveLeft(self.board)
                if event.key == K_RIGHT:
                    self.player.moveRight(self.board)
                if event.key == K_UP:
                    self.player.moveUp(self.board)
                if event.key == K_DOWN:
                    self.player.moveDown(self.board)
        
    def render(self):
        self.board.render(window)

    def paint(self):
        pass

    def update(self):
        pass


class Entity(object):

    def __init__(self, posX, posY, passable):
        """
        position -- board co-ord
        passable -- boolean for if can be walked through
        """
        self.posX     = posX
        self.posY     = posY
        self.passable = passable

    
class Creature(Entity):

    def __init__(self, health, strength, posX, posY, direction):
        super(Creature, self).__init__(posX, posY, False)
        self.health    = health
        self.strength  = strength
        self.direction = direction

    def move(self, dx, dy, board):
        dest = board.spaces[self.posX][self.posY]
        if not filter(lambda x: x.passable, dest.contents):
            board.spaces[self.posX][self.posY].contents.remove(self)
            self.posX += dx
            self.posY += dy
            board.spaces[self.posX][self.posY].contents.append(self)

    def moveUp(self, board):
        self.move(
            -1 if self.posY % 2 == 0  else 0, 
            -1, board)

    def moveDown(self, board):
        self.move(
            1 if self.posY % 2 == 1  else 0, 
            1, board)

    def moveLeft(self, board):
        self.move(
            -1 if self.posY % 2 == 0  else 0, 
            1, board)

    def moveRight(self, board):
        self.move(
            0 if self.posY % 2 == 0  else 1, 
            -1, board)


class Player(Creature):
    def __init__(self, health, strength, posX, posY, direction):
        super(Player, self).__init__(health, strength, posX, posY, direction)
        
    def render(self, window, pos):
        pygame.draw.circle(window, 
                           pygame.Color(0,0,255), 
                           (pos[0] + Board.tileWidth/2, pos[1] + Board.tileHeight/2), 
                           5)


class Tile(object):
    def __init__(self, path, contents):
        self._path    = path
        self.contents = contents
        self.image    = pygame.image.load(self._path)
        
    def render(self, window, pos):
        window.blit(self.image, pos)
        if self.contents:
            for content in self.contents:
                content.render(window, pos)

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
        for x in range(0, self.xDim):
            for y in range(0, self.yDim):
                if self.spaces[x][y]:
                    plotx = 10 + x*Board.tileWidth + (y&1)*(Board.tileHeight/2)
                    ploty = 10 + (y*(Board.tileHeight/2))/2
                    self.spaces[x][y].render(window, (plotx, ploty))


if __name__=='__main__':
    pygame.init()
    fpsClock = pygame.time.Clock()
    window = pygame.display.set_mode((600,600))
    pygame.display.set_caption('72 --- gameTest')

    b = Board((10,10))

    for x in range(0,10):
        for y in range(0,10):
            b.spaces[x][y] = Tile('media/rhombus.png', [])

    p = Player(None, None, 3,4, None)
    b.spaces[3][4].contents.append(p)

    g = GameplayFrame(None, window, b, p)
    
    while True:
        window.fill(pygame.Color(255,255,255))
        if not runStack([g]):
            break
        pygame.display.update()
        fpsClock.tick(30)
        

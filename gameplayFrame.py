import pygame

from stackframe import StackFrame

class GameplayFrame(StackFrame):

    def __init__(self, stack, window):
        super(GameplayFrame, self).__init__(stack, window)
        self.window = window
        
    def poll(self):
        """ Pole with
        for event in pygame.event.get()...
        """
        pass
        
    def render(self):
        pass

    def paint(self):
        pass

    def update(self):
        pass


class Entity(object):

    def __init__(self, position, passable):
        """
        position -- board co-ord
        passable -- boolean for if can be walked through
        """
        self.position = position
        self.passable = passable

    
class Creature(Entity):

    def __init__(self, health, strength, position):
        super(Creature, self).__init__(position, False)
        self.health   = health
        self.strength = strength


class Player(Creature):
    def __init__(self, health, strength, position):
        super(Player, self).__init__(health, strength, position)


class Tile(object):
    def __init__(self, path, contents):
        self._path    = path
        self.contents = contents
        self.image    = pygame.image.load(self._path)
        
    def render(self, window, pos):
        window.blit(self.image, pos)

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

    def renderBoard(self, window):
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

    while True:
        window.fill(pygame.Color(255,255,255))
        b.renderBoard(window)
        pygame.display.update()
        fpsClock.tick(30)
        

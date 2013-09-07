import pygame

from stackframe import StackFrame, runStack

class GameplayFrame(StackFrame):

    def __init__(self, stack, window, board):
        super(GameplayFrame, self).__init__(stack, window)
        self.stack  = stack
        self.window = window
        self.board  = board
        
    def poll(self):
        """ Pole with
        for event in pygame.event.get()...
        """
        pass
        
    def render(self):
        self.board.render(window)

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
            self.contents.render(window, pos)

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
            b.spaces[x][y] = Tile('media/rhombus.png', None)

    b.spaces[3][4].contents = Player(None, None, None)

    g = GameplayFrame(None, window, b)
    
    while True:
        window.fill(pygame.Color(255,255,255))
        if not runStack([g]):
            break
        pygame.display.update()
        fpsClock.tick(30)
        

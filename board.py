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

    def render(self, window, pos):
        pygame.draw.circle(window, 
                           pygame.Color(0,255,0), 
                           (pos[0] + Board.tileWidth/2, pos[1] + Board.tileHeight/2), 
                           5)

class Player(Creature):
    def __init__(self, health, strength, posX, posY, direction):
        super(Player, self).__init__(health, strength, posX, posY, direction)
        
    def render(self, window, pos):
        pygame.draw.circle(window, 
                           pygame.Color(0,0,255), 
                           (pos[0] + Board.tileWidth/2, pos[1] + Board.tileHeight/2), 
                           5)



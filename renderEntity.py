import pygame

from   animationRender  import Animation

"""
this takes the board directions and converts them
into the numerical directions used by the animations
"""
directionDict = {'up':, 'down':, 'left':, 'right':}

class Entity(object):

    def __init__(self, posX, posY, passable):
        """
        position -- board co-ord
        passable -- boolean for if can be walked through
        """
        self.posX     = posX
        self.posY     = posY
        self.passable = passable

    def getUp(self):
        return (-1 if self.posY % 2 == 0 else 0, -1)
        
    def getDown(self):
        return (1 if self.posY %2 == 1 else 0, 1)

    def getLeft(self):
        return (-1 if self.posY % 2 ==0 else 0, 1)

    def getRight(self):
        return (0 if self.posY % 2 == 0 else 1, -1)
        
class RenderEntity(Entity):

    def __init__(self, posX, posY, passable);
        super(RenderEntity, self).__init__(posX, posY, passable)
        
    def enableRender(self, path='media/animations/player/', positions=['idle', 'punch', 'walk']):
        self.animation = Animation(path, positions)
        
    def render(self, (xPos, yPos)):
        pass
    
    def update(self):
        if hasattr(self, 'animation'):
            self.animation.update()
        
class RenderCreature(RenderEntity):

    def __init__(self, health, strength, posX, posY, direction, speed):
        super(Creature, self).__init__(posX, posY, False)
        self.health    = health
        self.strength  = strength
        self.direction = direction
        self.speed     = speed
        self.prevX     = self.posX
        self.prevY     = self.posY
        self.transit   = 0
        self.interactTime = 0  

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

    """
    my idea is to not implement this in any of the classes
    this will let the RenderEntity base class handle all the rendering
    NOTE: this need the raw coordinates to draw on the window
    """ 
    # def render(self, window):
        # ptransit       = (self.speed - self.transit) / float(self.speed)
        # splotx, sploty = Board.getCoord(self.prevX, self.prevY)
        # eplotx, eploty = Board.getCoord(self.posX, self.posY)
        # splotx += Board.tileWidth/2
        # sploty += Board.tileHeight/2
        # eplotx += Board.tileWidth/2
        # eploty += Board.tileHeight/2
        # plotx = int(splotx + (eplotx - splotx) * ptransit)
        # ploty = int(sploty + (eploty - sploty) * ptransit)
        # pygame.draw.circle(window, 
                           # pygame.Color(0,255,0), 
                           # (plotx, ploty), 
                           # 5)

    def update(self, gameFrame):
        super(Creature, self).update()
    
        if self.transit > 0:
            self.transit -= 1
        if self.interactTime > 0:
            self.interactTime -= 1
            
    def interact(self, board):
        if self.direction == 'up':
            dx,dy = self.getUp()
        if self.direction == 'down':
            dx,dy = self.getDown()
        if self.direction == 'left':
            dx,dy = self.getLeft()
        if self.direction == 'right':
            dx,dy = self.getRight()

        destX = self.posX + dx
        destY = self.posY + dy

        if destX in range(0, board.xDim) and destY in range(0,board.yDim):
            return board.spaces[destX][destY]
        else:
            return None

    def attack(self, creature, board):
        dmg = int(random() * self.strength)
        creature.health -= dmg
        if creature.health <= 0:
            creature.die(board)

    def die(self, board):
        board.spaces[self.posX][self.posY].contents.remove(self)
    
    
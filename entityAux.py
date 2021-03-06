
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
        super(Player, self).update(gameFrame)
        inputs = gameFrame.inputDict

        if inputs['left']:
            self.moveLeft(gameFrame.board)
        elif inputs['right']:
            self.moveRight(gameFrame.board)
        elif inputs['up']:
            self.moveUp(gameFrame.board)
        elif inputs['down']:
            self.moveDown(gameFrame.board)
        
        
        if inputs['act'] and self.interactTime == 0:
            self.interact(gameFrame.board)

    def interact(self, board):
        self.interactTime = self.speed
        ispace = super(Player, self).interact(board)

        if ispace:
            for entity in ispace.contents:
                if isinstance(entity, Creature):
                    self.attack(entity, board)
                if isinstance(entity, Clerk):
                    clerkDialogManager = DialogManager(entity.conversation)
                    self.stack.append(dialogFrame(self.stack, self.window, clerkDialogManager, playerImage='media/avatars/prot_shitty.png', npcImage='media/avatars/never_use.png'))


class Enemy(Creature):

        def __init__(self, health, strength, posX, posY, direction, speed):
                super(Enemy, self).__init__(health, strength, posX, posY, direction, speed)

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
                

        def interact(self, board):
                if self.direction == 'up':
                        dx,dy = self.getUp()
                if self.direction == 'down':
                        dx,dy = self.getDown()
                if self.direction == 'left':
                        dx,dy = self.getLeft()
                if self.direction == 'right':
                        dx,dy = self.getRight()

class Clerk(Creature):
        
	def __init__(self, posX, posY, direction, conversation):
                super(Clerk, self).__init__(400, 0, posX, posY, direction, 1)
                self.conversation = conversation

	def converse(self):
                pass

	def update(self, board):
                pass
                
		


from board import Creature

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
                
		


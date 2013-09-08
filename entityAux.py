from board import Creature

class Enemy(Creature):

	def __init__(self, health, strength, posX, posY, direction, speed):
		super(Enemy, self).__init__(health, strength, posX, posY, direction, speed)

	def interact(self, board):
		if self.direction == 'up':
			dx,dy = self.getUp()
		if self.direction == 'down'
			dx,dy = self.getDown()
		if self.direction == 'left'
			dx,dy = self.getLeft()
		if self.direction == 'right'
			dx,dy = self.getRight()

class Clerk(Creature):
	
	def __init__(self, posX, posY, conversation):
		super(Clerk, self).__init__(400, 0, posX, posY, direction, 1)
		self.conversation = conversation

	def converse(self):
		pass

	def update(self, board):
		pass
		
		


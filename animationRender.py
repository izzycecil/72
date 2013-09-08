import pygame

from animations import GameSprite

class Animation(object):

    def __init__(self, path, positions):
        self.sprite = GameSprite(path, positions)
        
        #default starting position
        self.doing = self.sprite.getFrames('idle', 4)
        self.nextDirection = 4
        self.doingRect = self.doing[0].get_rect()
        self.currentFrame = 0
        self.next = self.doing
    
    #if this works only due to incedental desing of GameSprite
    def doNext(self, position, direction):
        self.nextDirection = direction
        self.next = self.sprite.getFrames(position, direction)
    
    def update(self):
        #check this
        if self.next is not self.doing and self.currentFrame == 0:
            self.doing = self.next
            self.next = self.sprite.getFrames('idle', self.nextDirection)

        try:
            self.currentFrame = (self.currentFrame + 1) % len(self.doing)
        except:
            self.currentFrame = 0
            self.next = self.sprite.getFrames('idle', self.nextDirection)
        
    def render(self, buffer, (xPos, yPos)):
        tempRect = self.doingRect.move((xPos - self.doingRect.width / 2, yPos - self.doingRect.height / 2))
        buffer.blit(self.doing[self.currentFrame], tempRect)

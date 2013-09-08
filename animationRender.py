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
        self.doNext = self.doing
    
    #if this works only due to incedental desing of GameSprite
    def doNext(self, position, direction):
        self.nextDirection = direction
        self.doNext = self.sprite.getFrames(position, direction)
    
    def update(self):
        #check this
        if self.doNext is not self.doing and self.currentFrame == 0:
            self.doing = self.doNext
            self.doNext = self.sprite.getFrames('idle', self.nextDirection)

        self.currentFrame = (self.currentFrame + 1) % len(self.doing)

    def render(self, buffer, (xPos, yPos)):
        self.doingRect.move_ip((xPos - self.doingRect.width / 2, yPos - self.doingRect.height / 2))
        buffer.blit(self.doing[self.currentFrame], self.doingRect)
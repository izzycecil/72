import pygame, time

from animations import GameSprite
from board      import Entity

animationSpeed = 1

class Animation(object):

    def __init__(self, window, positions=['idle', 'punch', 'walk']):
        self.sprite = GameSprite('media/animations/player/', positions)
        self.window = window
        
        self.doing = self.sprite.getFrames('idle', 4)
        self.doingRect = self.doing[0].get_rect()
        self.currentFrame = 0
        self.doNext = self.doing
        
        self.next = time.time() * 1000
    
    #if this works only due to incedental desing of GameSprite
    def doNext(self, position, direction):
        self.doNext = self.sprite.getFrames(position, direction)
    
    def update(self):
        #check this
        if self.doNext is not self.doing and self.currentFrame == 0:
            self.doing = self.doNext
            
        if time.time() * 1000 > self.next:
            self.currentFrame = (self.currentFrame + 1) % len(self.doing)
            self.next = time.time() * 1000 + 200 * animationSpeed

    #center to render at ceneter
    def render(self, (xPos, yPos)):
        #consider optimizing
        self.doingRect.move_ip((xPos - self.doingRect.width / 2, yPos - self.doingRect.height / 2))
        
    #uses direct drawing
    def paint(self):
        self.window.blit(self.doing[self.currentFrame], self.doingRect)
        
    def paintTo(self, window):
        window.blit(self.doing[self.currentFrame], self.doingRect)
        
class RenderEntity():
    
    


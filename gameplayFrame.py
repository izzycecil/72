#!/usr/bin/env python

import pygame
from pygame.locals import *

from board      import Board, Creature, Tile, Player
from stackframe import StackFrame, runStack

class GameplayFrame(StackFrame):

    updateMod = 8

    def __init__(self, stack, window, board, player):
        super(GameplayFrame, self).__init__(stack, window)
        self.stack         = stack
        self.window        = window
        self.board         = board
        self.player        = player
        self.updateCounter = 0
        self.inputDict     = {'up'   :False, 
                              'down' :False, 
                              'left' :False, 
                              'right':False,
                              'act'  :False,
                              'pause':False,}
        
    def poll(self):
        super(GameplayFrame, self).poll()
    
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key in (K_UP, K_w):
                    self.inputDict['up']    = True
                    self.inputDict['down']  = False
                    self.inputDict['left']  = False
                    self.inputDict['right'] = False
                if event.key in (K_DOWN, K_s):
                    self.inputDict['up']    = False
                    self.inputDict['down']  = True
                    self.inputDict['left']  = False
                    self.inputDict['right'] = False
                if event.key in (K_LEFT, K_a):
                    self.inputDict['up']    = False
                    self.inputDict['down']  = False
                    self.inputDict['left']  = True
                    self.inputDict['right'] = False
                if event.key in (K_RIGHT, K_d):
                    self.inputDict['up']    = False
                    self.inputDict['down']  = False
                    self.inputDict['left']  = False
                    self.inputDict['right'] = True

            if event.type == KEYUP:
                if event.key in (K_UP, K_w):
                    self.inputDict['up']    = False
                if event.key in (K_DOWN, K_s):
                    self.inputDict['down']  = False
                if event.key in (K_LEFT, K_a):
                    self.inputDict['left']  = False
                if event.key in (K_RIGHT, K_d):
                    self.inputDict['right'] = False
                                            
        
    def render(self):
        self.board.render(self.window)

    def update(self):
        if not self.updateCounter:
            self.board.update(self)
            self.updateCounter += 1
        else:
            self.player.update(self)
            self.updateCounter = (self.updateCounter+1)%GameplayFrame.updateMod


if __name__=='__main__':
    pygame.init()
    fpsClock = pygame.time.Clock()
    window = pygame.display.set_mode((600,600))
    pygame.display.set_caption('72 --- gameTest')

    b = Board((10,10))

    for x in range(0,10):
        for y in range(0,10):
            b.spaces[x][y] = Tile('media/rhombus.png', [])

    p = Player(None, None, None, None, None, 4)
    b.placeEntity(p, 3, 4)
    #b.placeEntity(Creature(None, None, None, None, None), 5,5)

    g = GameplayFrame(None, window, b, p)
    
    while True:
        window.fill(pygame.Color(255,255,255))
        if not runStack([g]):
            break
        pygame.display.update()
        fpsClock.tick(30)
        

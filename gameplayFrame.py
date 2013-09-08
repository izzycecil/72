#!/usr/bin/env python

import pygame
from pygame.locals import *

from board      import Board, Tile, Enemy, Creature, Player
from stackframe import StackFrame, runStack
from menus      import gameMenuTree

class GameplayFrame(StackFrame):

    updateMod  = 8
    camBoxTrim = 60
    camSpeed   = 10

    def __init__(self, stack, window, board, player):
        super(GameplayFrame, self).__init__(stack, window)
        self.stack         = stack
        self.window        = window
        self.board         = board
        self.player        = player
        self.inputDict     = {'up'   :False, 
                              'down' :False, 
                              'left' :False, 
                              'right':False,
                              'act'  :False,
                              'pause':False,}

        self.buffer = pygame.Surface(
            (board.xDim*Board.tileHeight+20, board.yDim*Board.tileHeight),
            flags = SRCALPHA)

        self.cameraX = 0
        self.cameraY = 0
        self.dxMin   = GameplayFrame.camBoxTrim
        self.dyMin   = GameplayFrame.camBoxTrim
        self.dxMax   = window.get_width() - GameplayFrame.camBoxTrim - 60
        self.dyMax   = window.get_height() - GameplayFrame.camBoxTrim
        
    def updateCam(self):
        px, py = Board.getCoord(self.player.posX, self.player.posY)
        dx = px + self.cameraX
        dy = py + self.cameraY
        
        if dx < self.dxMin:
            self.cameraX += GameplayFrame.camSpeed
        elif dx > self.dxMax:
            self.cameraX -= GameplayFrame.camSpeed

        if dy < self.dyMin:
            self.cameraY += GameplayFrame.camSpeed
        elif dy > self.dyMax:
            self.cameraY -= GameplayFrame.camSpeed

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
                if event.key in (K_ESCAPE, K_PAUSE):
                    self.inputDict['pause'] = True
                if event.key in (K_SPACE,):
                    self.inputDict['act']  = True

            if event.type == KEYUP:
                if event.key in (K_UP, K_w):
                    self.inputDict['up']    = False
                if event.key in (K_DOWN, K_s):
                    self.inputDict['down']  = False
                if event.key in (K_LEFT, K_a):
                    self.inputDict['left']  = False
                if event.key in (K_RIGHT, K_d):
                    self.inputDict['right'] = False
                if event.key in (K_ESCAPE, K_PAUSE):
                    self.inputDict['pause'] = False
                if event.key in (K_SPACE,):
                    self.inputDict['act']   = False

                                            
        
    def render(self):
        self.board.render(self.buffer)

    def update(self):
        self.board.update(self)

    def paint(self):
        self.updateCam()
        self.window.blit(self.buffer, (self.cameraX, self.cameraY))


if __name__=='__main__':
    pygame.init()
    fpsClock = pygame.time.Clock()
    window = pygame.display.set_mode((600,600))
    pygame.display.set_caption('72 --- gameTest')

    b = Board((20,20))

    for x in range(0,20):
        for y in range(0,20):
            b.spaces[x][y] = Tile('media/tileproto1.png', [])

    p = Player(20, 10, None, None, None, 4)
    b.placeEntity(p, 3, 4)
    b.placeEntity(Enemy(20, 10, None, None, None, 10), 5,5)

    g = GameplayFrame(None, window, b, p)
    
    while True:
        window.fill(pygame.Color(255,255,255))
        if not runStack([g]):
            break
        pygame.display.update()
        fpsClock.tick(30)
        

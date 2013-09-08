#!/usr/bin/env python

import pygame, sys
from pygame.locals import *

from stackframe     import StackFrame, runStack
from board          import Board, Tile, Enemy, Clerk, Creature, Player
from gameplayFrame  import GameplayFrame
from menuFrame      import MenuTree
from menus          import gameMenuTree, mainMenuTree
from dialogue       import DialogManager
from dialogFrame    import DialogFrame

def initGraphics():
    pygame.init()
    window = pygame.display.set_mode((600,600), pygame.DOUBLEBUF, 32)
    pygame.display.set_caption('72 --- Death of One, Death of Many')
    return window
    
def initSound():
    pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)

def gameFrame(window, stack):
    clerkDialogManager = DialogManager('redneck')
    diag = DialogFrame(stack, window, clerkDialogManager, playerImage='media/avatars/protag.png', npcImage='media/avatars/notnigel.png')
    b = Board((20,20))

    for x in range(0,20):
        for y in range(0,20):
            b.spaces[x][y] = Tile('media/tiles/basic.png', [])

    p = Player(20, 10, None, None, None, 4)
    p.enableRender()
    b.placeEntity(p, 3, 4)
    b.placeEntity(Clerk(20, 10, None, diag), 5,5)

    return GameplayFrame(stack, window, b, p)
    
def main():
    stack  = []

    initSound()
    
    window   = initGraphics()
    fpsClock = pygame.time.Clock()
    
    stack.append(mainMenuTree(stack, window, gameFrame(window, stack)));
    
    while True:
        window.fill(pygame.Color(255,255,255))
        if not runStack(stack):
            break
        pygame.display.update()
        fpsClock.tick(30)

    return

if __name__=='__main__':
    main()

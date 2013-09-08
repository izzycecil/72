import pygame, sys
from pygame.locals import *

from stackframe     import StackFrame, runStack
from board          import Board, Creature, Player, Tile
from gameplayFrame  import GameplayFrame
from menuFrame      import MenuTree
from menus          import mainMenuTree, mainMenuTree

def initGraphics():
    pygame.init()
    window = pygame.display.set_mode((600,600), pygame.DOUBLEBUF, 32)
    pygame.display.set_caption('72 --- Death of One, Death of Many')
    return window
    
def initSound():
    pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)

def gameFrame(window, stack):
    # b = Board(None, filename='media/maps/test')
    b = Board((10, 10))
    
    for x in range(0,10):
        for y in range(0,10):
            b.spaces[x][y] = Tile('media/shittytesttile.png', [])

    p = Player(None, None, None, None, None, 4)
    b.placeEntity(p, 3, 4)
    
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

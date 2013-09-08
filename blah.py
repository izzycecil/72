import pygame, sys
from pygame.locals import *

from stackframe     import StackFrame, runStack
from menu           import MenuTree
from gameplayFrame  import GameplayFrame 
from board          import Board, Creature, Tile, Player
from stackframe     import StackFrame, runStack

def initGraphics():
    pygame.init()
    fpsClock = pygame.time.Clock()
    window = pygame.display.set_mode((600,600))
    pygame.display.set_caption('72 --- Death of One, Death of Many')
    return (window, fpsClock)
    
def initSound():
    pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)

def prepGameframe():
    b = Board((10,10))

    for x in range(0,10):
        for y in range(0,10):
            b.spaces[x][y] = Tile('media/rhombus.png', [])

    p = Player(None, None, 3,4, None)
    c = Creature(None, None, 5, 5, None)
    b.spaces[5][5].contents.append(c)
    b.spaces[3][4].contents.append(p)

    g = GameplayFrame(None, window, b, p)
    
    while True:
        window.fill(pygame.Color(255,255,255))
        if not runStack([g]):
            break
        pygame.display.update()
        fpsClock.tick(30)
    
def main():
    stack  = []

    (window, fpsClock) = initGraphics()

    initSound()
    
    prepGameFrame()
    
    
    stack.append(MenuTree(stack, window, [["Play", sys.exit], ["Options", [["Quit", sys.exit], ["Done", sys.exit]]]], pygame.Rect((0, 0), (600, 600)), highlighting=(250, 100, 100), background="media/bg.png", music="media/music.wav"))
    
    while True:
        window.fill(pygame.Color(255,255,255))
        if not runStack(stack):
            break
        pygame.display.update()
        fpsClock.tick(30)

    return

if __name__=='__main__':
    main()
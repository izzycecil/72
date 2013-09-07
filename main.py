import pygame, sys
from pygame.locals import *

from stackframe     import StackFrame, runStack
from board          import Board, Creature, Player, Tile
from gameplayFrame  import GameplayFrame
from menu           import MenuTree

def initGraphics():
    pygame.init()
    window = pygame.display.set_mode((600,600))
    pygame.display.set_caption('72 --- Death of One, Death of Many')
    return window
    
def initSound():
    pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)

def gameFrame(window, stack):
    b = Board((10,10))
    
    for x in range(0,10):
        for y in range(0,10):
            b.spaces[x][y] = Tile('media/rhombus.png', [])

    p = Player(None, None, None, None, None, 4)
    b.placeEntity(p, 3, 4)
    
    return GameplayFrame(None, window, b, p)
    
def mainMenuTree(window, stack, playFrame):
    mainMenu = MenuTree(stack, window, [["Play", playFrame], ["Options", [["Quit", sys.exit], ["Done", sys.exit]]]], \
                        pygame.Rect((0, 0), (600, 600)), highlighting=(250, 100, 100),                          \
                        background="media/bg.png", music="media/music.wav")
                            
    return mainMenu
    
def main():
    stack  = []

    initSound()
    
    window   = initGraphics()
    fpsClock = pygame.time.Clock()
    
    stack.append(mainMenuTree(window, stack, gameFrame(window, stack)));
    
    while True:
        window.fill(pygame.Color(255,255,255))
        if not runStack(stack):
            break
        pygame.display.update()
        fpsClock.tick(30)

    return

if __name__=='__main__':
    main()

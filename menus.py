import pygame, sys

from stackframe import StackFrame, runStack
from menuFrame  import MenuTree

def mainMenuTree(stack, window, playFrame):
    # mainMenu = MenuTree(stack, window, [["Play", playFrame], ["Options", [["Quit", sys.exit], ["Done", sys.exit]]]], \
                        # pygame.Rect((0, 0), (600, 600)), highlighting=(250, 100, 100),                          \
                        # background="media/bg.png", music="media/music.wav")
                        
    mainMenu = MenuTree(stack, window, [["Play", playFrame], ["Options", [["Quit", sys.exit], ["Done", sys.exit]]]], \
                        pygame.Rect((0, 0), (600, 600)), highlighting=(250, 100, 100),                          \
                        background="media/bg.png")
                        
    return mainMenu
                        
def gameMenuTree(stack, window):
    gameMenu = MenuTree(stack, window, [["Quit", sys.exit], ["Return", None]], \
                        pygame.Rect((50, 50), (500, 500)), highlighting=(250, 100, 100),                          \
                        color=(100, 100, 100, 100), renderOver=(len(stack) - 1))
                        
    return gameMenu
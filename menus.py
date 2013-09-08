import pygame, sys

from stackframe import StackFrame, runStack
from menuFrame  import MenuTree
from dialogue       import DialogManager
from dialogFrame    import DialogFrame

def mainMenuTree(stack, window, playFrame):
    mainMenu = MenuTree(stack, window, [["Play", playFrame], ["Options", [["Quit", sys.exit], ["Done", sys.exit]]]], \
                        pygame.Rect((0, 0), (600, 600)), highlighting=(250, 100, 100),                          \
                        background="media/titlescrn.png", music="media/bg.wav")

    return mainMenu
                        
def gameMenuTree(stack, window):
    clerkDialogManager = DialogManager('redneck')
    diag = DialogFrame(stack, window, clerkDialogManager, playerImage='media/avatars/protag.png', npcImage='media/avatars/notnigel.png')

    gameMenu = MenuTree(stack, window, [["Quit", sys.exit], ["Dialog", diag], ["Return", None]], \
                        pygame.Rect((50, 50), (500, 500)), highlighting=(250, 100, 100),                          \
                        color=(100, 100, 100, 100), renderOver=(len(stack) - 1))
                        
    return gameMenu
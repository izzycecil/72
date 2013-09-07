import pygame
from pygame.locals import *

from stackframe import StackFrame, runStack

def initGraphics():
    pygame.init()
    fpsClock = pygame.time.Clock()

    window = pygame.display.set_mod((600,600))
    pygame.display.set_caption('72 --- Death of One, Death of Many')
    
    return window
    
def main():
    stack = []
    
    while runStack(stack):
        pass

    return

if __name__=='__main__':
    main()

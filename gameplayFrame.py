import pygame
from pygame.locals import *

from board      import Board, Creature, Tile
from stackframe import StackFrame, runStack

class GameplayFrame(StackFrame):

    def __init__(self, stack, window, board, player):
        super(GameplayFrame, self).__init__(stack, window)
        self.stack  = stack
        self.window = window
        self.board  = board
        self.player = player
        
    def poll(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    self.player.moveLeft(self.board)
                if event.key == K_RIGHT:
                    self.player.moveRight(self.board)
                if event.key == K_UP:
                    self.player.moveUp(self.board)
                if event.key == K_DOWN:
                    self.player.moveDown(self.board)
        
    def render(self):
        self.board.render(window)

    def paint(self):
        pass

    def update(self):
        pass


if __name__=='__main__':
    pygame.init()
    fpsClock = pygame.time.Clock()
    window = pygame.display.set_mode((600,600))
    pygame.display.set_caption('72 --- gameTest')

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
        

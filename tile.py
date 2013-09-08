import pygame

class Tile(object):
    def __init__(self, path, contents):
        self._path    = path
        self.contents = contents
        self.image    = pygame.image.load(self._path)
        
    def render(self, window, pos):
        window.blit(self.image, pos)
        if self.contents:
            return self.contents
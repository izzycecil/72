import pygame

from stackframe import StackFrame, runStack
from dialogue import DialogManager

class DialogFrame(StackFrame):

    def __init__(self, stack, window, manager):
        super(DialogFrame, self).__init__(stack, window)
        self.stack  = stack
        self.window = window
        self.surface = pygame.Surface((400,400))
        self.manager = manager
        self.position = (40,40)
        self.lines = []
        
    def poll(self):
        """ Poll with
        for event in pygame.event.get()...
        """
        pass
        
    def render(self):
        fontSize = 36
        fontSpace = 4
        # use the default font
        font = pygame.font.Font(None, fontSize)

        text = font.render("TEST", 1, (250, 250, 250))
        textPos = text.get_rect(centerx = self.surface.get_width() / 2, centery = 30)
        self.surface.blit(text, textPos)

    def paint(self):
        self.window.blit(self.surface, self.position)

    def update(self):
        pass


if __name__=='__main__':
    pygame.init()
    fpsClock = pygame.time.Clock()
    window = pygame.display.set_mode((600,600))
    pygame.display.set_caption('72 --- gameTest')

    manager = DialogManager('testtree')

    frame = DialogFrame(None, window, manager)
    
    while True:
        window.fill(pygame.Color(255,255,255))
        if not runStack([frame]):
            break
        pygame.display.update()
        fpsClock.tick(30)
        

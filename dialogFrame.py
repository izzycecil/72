import pygame

from stackframe import StackFrame, runStack
from dialogue import DialogManager

class DialogFrame(StackFrame):

    def __init__(self, stack, window, manager):
        super(DialogFrame, self).__init__(stack, window)
        self.stack  = stack
        self.window = window
        self.manager = manager
        self.responsePosition = (40,40)
        self.responseSize = (350,100)
        self.promptPosition = (150,300)
        self.promptSize = (350, 100)
        self.responseSurface = pygame.Surface(self.responseSize)
        self.promptSurface = pygame.Surface(self.promptSize)
        self.boxes = []
        
    def poll(self):
        """ Poll with
        for event in pygame.event.get()...
        """
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                xPos = event.pos[0] - self.promptPosition[0] # move these coordinates in to our canvas
                yPos = event.pos[1] - self.promptPosition[1]
                for i, box in enumerate(self.boxes):
                    if xPos > box.left and xPos < box.right and yPos > box.top and yPos < box.bottom:
                        self.manager.followOption(i)
        
    def render(self):
        self.responseSurface = pygame.Surface(self.responseSize)
        self.promptSurface = pygame.Surface(self.promptSize)

        fontSize = 20
        fontSpace = 4
        # use the default font
        font = pygame.font.Font(None, fontSize)

        # text = font.render("TEST", 1, (250, 250, 250))
        # textPos = text.get_rect(centerx = self.surface.get_width() / 2, centery = 30)
        # self.surface.blit(text, textPos)

        # Get the current dialog line
        response = self.manager.getCurrentResponse()
        # Get the options
        options = self.manager.getCurrentOptions()

        # Draw the current response
        rtext = font.render(response, 1, (245,245,245))
        rtextPos = rtext.get_rect().move(10,10)
        self.responseSurface.blit(rtext, rtextPos)

        # Draw the dialog options
        self.boxes = []
        vertPos = 10
        for i,option in enumerate(options):
            otext = font.render(option, 1, (200,200,255))
            otextPos = otext.get_rect().move(10,vertPos)
            self.promptSurface.blit(otext, otextPos)
            vertPos += 20
            self.boxes.append(otextPos)




    def paint(self):
        self.window.blit(self.responseSurface, self.responsePosition)
        self.window.blit(self.promptSurface, self.promptPosition)

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
        

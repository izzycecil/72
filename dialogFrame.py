import pygame
import string

from stackframe import StackFrame, runStack
from dialogue import DialogManager

class DialogFrame(StackFrame):

    def __init__(self, stack, window, manager, npcImage=None, playerImage=None):
        super(DialogFrame, self).__init__(stack, window)
        self.stack  = stack
        self.window = window
        self.manager = manager

        # Surface setup for dialog components
        self.responsePosition = (40,40)
        self.responseSize = (350,160)
        self.promptPosition = (210,300)
        self.promptSize = (350, 160)
        self.responseSurface = pygame.Surface(self.responseSize, flags=pygame.SRCALPHA)
        self.promptSurface = pygame.Surface(self.promptSize, flags=pygame.SRCALPHA)

        # Surface setup for zoomed avaters
        self.npcPosition = (40, 300)
        self.npcSize = (160,160)
        self.playerPosition = (400, 40)
        self.playerSize = (160, 160)

        if npcImage != None:
            self.npcImage = pygame.image.load(npcImage)
        else:
            self.npcImage = None

        if playerImage != None:
            self.playerImage = pygame.image.load(playerImage)
        else:
            self.playerImage = None

        self.boxes = []
        
    def poll(self):
        """ Poll with
        for event in pygame.event.get()...
        """
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                xPos = event.pos[0] - self.promptPosition[0] # move these coordinates in to our canvas
                yPos = event.pos[1] - self.promptPosition[1]
                for box in self.boxes:
                    if xPos > box[1].left and xPos < box[1].right and yPos > box[1].top and yPos < box[1].bottom:
                        self.manager.followOption(box[0])
        
    def wrap(this, input):
        linelen = 45
        i = 0;
        lines = []
        while i < len(input):
            # find wrap point
            if i + linelen < len(input):
                point = i + linelen
                opoint = point
                # find a space to go back to
                c = input[point]
                while c != ' ':
                    point -= 1
                    c = input[point]
                    if point < 0:
                        point = opoint
                        break
                lines.append(input[i:point])
                i = point + 1
            else:
                lines.append(input[i:len(input)])
                break
        return lines

    def render(self):
        self.responseSurface = pygame.Surface(self.responseSize)
        self.promptSurface = pygame.Surface(self.promptSize)
        self.responseSurface.fill((0,0,0,200))
        self.promptSurface.fill((0,0,0,200))

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
        vposition = 10
        for line in self.wrap(response):
            rtext = font.render(line, 1, (245,245,245))
            rtextPos = rtext.get_rect().move(10,vposition)
            vposition += 16
            self.responseSurface.blit(rtext, rtextPos)

        # Draw the dialog options
        self.boxes = []
        vertPos = 10
        for i,option in enumerate(options):
            for line in self.wrap(option):
                otext = font.render(line, 1, (200,200,255))
                otextPos = otext.get_rect().move(10,vertPos)
                self.promptSurface.blit(otext, otextPos)
                vertPos += 16
                self.boxes.append((i, otextPos))
            vertPos += 6

    def paint(self):
        self.window.blit(self.responseSurface, self.responsePosition)
        self.window.blit(self.promptSurface, self.promptPosition)

        if self.npcImage != None:
            self.window.blit(self.npcImage, self.npcPosition)

        if self.playerImage != None:
            self.window.blit(self.playerImage, self.playerPosition)

    def update(self):
        pass


if __name__=='__main__':
    pygame.init()
    fpsClock = pygame.time.Clock()
    window = pygame.display.set_mode((600,600))
    pygame.display.set_caption('72 --- dialogTest')

    manager = DialogManager('countergirl')

    frame = DialogFrame(None, window, manager, npcImage='media/avatars/prot_shitty.png', playerImage='media/avatars/never_use.png')
    
    while True:
        window.fill(pygame.Color(255,255,255))
        if not runStack([frame]):
            break
        pygame.display.update()
        fpsClock.tick(30)
        

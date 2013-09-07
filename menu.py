import pygame

from stackframe import StackFrame, runStack

# class MenuItem(pygame.font.Font):

class Menu(StackFrame):

    def __init__(self, stack, window, (xPosition, yPosition), (xSize, ySize), items):
        super(Menu, self).__init__(stack, window)
        self.surface = pygame.Surface((xSize, ySize))
        self.items = items
        self.position = (xPosition, yPosition)
        
    def poll(self):
        event = pygame.event.poll()
        if event.type == pygame.MOUSEBUTTONDOWN:
            xPos = event.pos[0]
            yPos = event.pos[1]
            for entry in self.boxes.keys():
                item = self.boxes[entry][0]
                if xPos > item.left and xPos < item.right and yPos > item.top and yPos < item.bottom:
                    self.boxes[entry][1]()
        
    def update(self):
        pass
    
    def render(self):
        fontSize = 36
        fontSpace = 4
        # use the default font
        font = pygame.font.Font(None, fontSize)
        
        subHeight = (fontSize + fontSpace) * len(self.items.keys())
        subHeightStart = self.surface.get_height() / 2 - subHeight / 2
        
        self.boxes = dict()
        
        for entry in self.items.keys():
            self.items[entry]
            text = font.render(entry, 1, (250, 250, 250))
            textPos = text.get_rect(centerx = self.surface.get_width() / 2, centery = subHeightStart + fontSize + fontSpace)
            self.boxes.update(entry=(textPos,self.items[entry]))
            subHeightStart = subHeightStart + fontSize + fontSpace
            self.surface.blit(text, textPos)
        
    def paint(self):
        self.window.blit(self.surface, self.position)
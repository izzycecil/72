import pygame, sys

def runStack(stack):
    if stack:
        stack[-1].poll()
        stack[-1].update()
    else:
        return False
    if stack:
        stack[-1].render()
        stack[-1].paint()
    else:
        return False

    return True


class StackFrame(object):
    def __init__(self, stack, window, music=None):
        self.stack  = stack
        self.window = window
        if music is not None:
            self.music = pygame.mixer.Sound(music)


    def poll(self):
        for event in pygame.event.get(pygame.QUIT):
            sys.exit()
        
    
    def render(self):
        pass

    def paint(self):
        pass

    def update(self):
        if hasattr(self, 'music'):
            try:
                if not self.channel.get_busy():
                    self.channel = self.music.play()
            except AttributeError:
                self.channel = self.music.play()
        
    def kill(self):
        self.stack.remove(self)

    def quit(self):
        del self.stack[:]

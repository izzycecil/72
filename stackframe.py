

class StackFrame(object):

    def __init__(self, stack):
        self.stack = stack
    
    def render(self):
        pass

    def paint(self):
        pass

    def update(self):
        pass
        
    def kill(self):
        self.stack.remove(self)

    def quit(self):
        del self.stack[:]


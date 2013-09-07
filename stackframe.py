def runStack(stack):
    if stack:
        stack[-1].pole()
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
    def __init__(self, stack, window):
        self.stack  = stack
        self.window = window

    def poll(self):
        pass
    
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

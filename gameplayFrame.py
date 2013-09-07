
from stackframe import StackFrame

class GameplayFrame(StackFrame):

    def __init__(self, stack, window):
        super(GameplayFrame, self).__init__(stack, window)
        self.window = window
        
    def poll(self):
        """ Pole with
        for event in pygame.event.get()...
        """
        pass
        
    def render(self):
        pass

    def paint(self):
        pass

    def update(self):
        pass


class Entity(object):

    def __init__(self, position, passable):
        """
        position -- board co-ord
        passable -- boolean for if can be walked through
        """
        self.position = position
        self.passable = passable

    
class Creature(Entity):

    def __init__(self, health, strength, position):
        super(Creature, self).__init__(position, False)
        self.health   = health
        self.strength = strength


class Player(Creature):
    def __init__(self, health, strength, position):
        super(Player, self).__init__(health, strength, position)


class Board(object):
    def __init__(self, dim):
        self.spaces = [
            [False for x in range(0,dim[0])] for x in range(0,dim[1])
        ]



if __name__=='__main__':
    b = Board((10,10))
    

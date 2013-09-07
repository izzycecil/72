import pickle

class Dialogue(object):
    """
    Represents a position in the dialogue tree. Can have a 'prompt' which is a
    line of dialogue said by the player that initiates this node. Always has a
    'response' which is a line said by the NPC being interacted with in
    response. Then has 'options' which are descendent nodes.
    """

    def __init__(self, response, prompt="(none)"):
        self.prompt = prompt
        self.response = response
        self.options = []
        self.registry = {}
        self.event = None

    """
    Loads a tree from file, starting with this node as root.
    """
    @classmethod
    def load(cls,f):
        return pickle.load(f)

    """
    Saves the tree, with this node as root, to file
    """
    def save(self, f):
        pickle.dump(self,f,2)
        f.close()

class DialogManager(object):
    """
    Wraps a Dialogue tree with convenience functionality intended for use by
    the actual game product.
    """

    def __init__(self, treename):
        with open(treename + '.72d', 'rb') as f:
            root = Dialogue.load(f)
        self.position = root
        self.history = []

    def getCurrentDialog(self):
        return self.position.response

    def getCurrentOptions(self):
        currentOptions = []
        for option in self.position.options:
            currentOptions.append(option.prompt)

    def followOption(self, index):
        self.history.append(current)
        self.current = self.current.options[index]

        if self.event != None:
            self.event()

        return self.current.response

    def backUp(self):
        self.current = self.history.pop()

        if self.event != None:
            self.event()

        return self.current.response

    def registerEvent(self, handle, callback):
        self.root.registry[handle].event = callback
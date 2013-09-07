import pickle

class Dialogue:
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
        self.registrations = {}

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
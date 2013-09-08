import pygame, glob

animationDirections = ['UP', 'BACKLEFT', 'LEFT', 'FRONTLEFT', 'FRONT', 'FRONTRIGHT', 'RIGHT', 'BACKRIGHT']

#do not touch!!! (ask me why)
class GameSprite(object):

    def __init__(self, path, positions):
        self.frameDict = {}
    
        for pos in positions:
            for dir in animationDirections:
                self.frameDict.update({pos+'_'+dir:self.getImages(path, pos+'_'+dir)})
    
    def getImages(self, path, subPath):
        surfaces = []
        
        for f in glob.glob(path+subPath+"/*.png"):
            # print f
            surfaces.append(pygame.image.load(f))
            surfaces[-1].convert_alpha()
        
        temp = list(surfaces)
        
        if len(temp):
            temp.pop()
            temp.reverse()
            temp.pop()
        
        return surfaces+temp
    
    def getFrames(self,  position, direction):
        return self.frameDict[position+'_'+animationDirections[direction]]
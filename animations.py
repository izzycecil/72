import pygame, glob

animationDirections = ['UP', 'BACKLEFT', 'LEFT', 'FRONTLEFT', 'FRONT', 'FRONTRIGHT', 'RIGHT', 'BACKRIGHT']

class GameSprite(object):
    
    # path like media/mainimations/png/
    def __init__(self, path, positions=['idle', 'punch', 'walk']):
        self.frameDict = {}
    
        for pos in positions:
            for dir in animationDirections:
                self.frameDict.update({pos+'_'+dir:self.getImages(path, pos+'_'+dir)})
    
    def getImages(self, path, subPath):
        surfaces = []
        
        for f in glob.glob(path+subPath+"./*.png"):
            surfaces.append(pygame.image.load(f))
        
        temp = surfaces
        
        if len(temp):
            temp.pop()
            temp.reverse()
            temp.pop()
        
        return surfaces+temp
    
    def getFrames(self,  position='idle', direction=4):
        return self.frameDict[position+'_'+animationDirections[direction]]
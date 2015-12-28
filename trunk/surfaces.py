import sys, os, pygame

#todo: make a children merging routine
# make a naming system, Surface can also be a dictionary of children 

class SurfaceConfig(dict):
    """ position    - position of sprite relative to parent
        image       - surface containing the full image
        size        - size (w,h) of the actual surface
        framePos    - position of the upper left corner of the viewable image
        visible     - if it is to be shown
        name        - some distingushable name(to be used later in development
    """
    def __init__(self, position = (0,0), size = (0,0), image = pygame.Surface((0,0)), framePos = (0,0), name = "unnamed", visible = True):
        self["position"] = position
        self["image"] = image
        self["framePos"] = framePos
        self["name"] = name
        self["visible"] = visible

        if size == (0,0):
            self["size"] = image.get_size()

class Surface(object):
    """Children are a set of surfaces blitted to this, parentless surfaces"""
    def __init__(self, cfg = SurfaceConfig(), parent = None, children = []):
        self.cfg = cfg.copy()
        self.children = children
        self.parent = parent

        if not self.parent:
            #open in new window
            if not pygame.display.get_init():
                pygame.display.init()

            self._surface = pygame.display.set_mode(self.cfg["size"])
        else:
            self.parent.children.append(self)
            self._surface = pygame.Surface(self.cfg["size"])
        
        #draw initials[]
        self._surface.blit(self.cfg["image"],self.cfg["framePos"])
    
    def addSurface(self, child):
        self.children.append(child)
        self._surface.blit(self.children[-1]._surface(),child.cfg["position"])

    def update(self):
        self._surface.blit(self.cfg["image"], self.cfg["framePos"])
        for i in self.childreni[:]:
            if i.visible:
                try:
                    i.update()
                except:
                    print "Couldnt update child,",i.cfg["name"],"...it is useless if it cant be shown...deleting"
                    self.children.remove(i)

    def remove(self, child):
        children.remove(child)

    def setToWindow(self):
        #open in new window
        if not pygame.display.get_init():
            pygame.display.init()

        self._surface = pygame.display.set_mode(self.cfg["size"])

if __name__ == "__main__":
    window = Surface()

        


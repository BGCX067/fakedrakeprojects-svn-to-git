import pygame
import surfaces


#at this point what you have to do 
# is create a configuration for surface
# create the surface(configuration can be reused)
# create


class SpritePlane(object):
    """ 
        SpritePlane is a wrapper for Surface but it also contains sprites
        for collision detection , it is intended to be a frontend to Surface
        and to be used instead. It can be treated as a surface normally
    """
    def __init__(self, surface):
        self.surface = surface

        self.sprites = set()

    def update(self):
        se

class SpriteConfig(dict):
    def __init__(self, surfacecfg = surfaces.SurfaceConfig(), collidable = True):
        self["surface"] = surfacecfg
        self["collidable"] = collidable

class Sprite(object):
    #WARNING: self.cfg["surface"] should not be altered and is there for setup purposes ONLY, alter self.surface.cfg instead
    def __init__(self, cfg, surface=None, parent = None):
        self.cfg = cfg.copy()
        if not surface:
            self.surface = surfaces.Surface(cfg["surface"])
        else:
            self.surface = surface

        #parent surface

    def update(self):
        self.surface.update()

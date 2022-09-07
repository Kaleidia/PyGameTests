import pygame
from Utils import loadImages

class Tile(pygame.sprite.Sprite):
    def __init__(self,tileSize,x,y,index=0):
        super(Tile, self).__init__()
        image: self.surf = loadImages("pix/GroundTiles")[index]
        self.surf = pygame.transform.scale(image,(tileSize,tileSize))
        self.pos = (x * tileSize, y * tileSize)





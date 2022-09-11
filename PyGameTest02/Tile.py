import pygame
from Utils import loadImages


class Tile(pygame.sprite.Sprite):
    def __init__(self, tileSize, x, y, index=0, xOffset=0, yOffset=0):
        super(Tile, self).__init__()
        self.surf = loadImages("pix/GroundTiles")[index]
        self.surf = pygame.transform.scale(self.surf, (tileSize, tileSize))
        self.pos = (x * tileSize + xOffset, y * tileSize + yOffset)

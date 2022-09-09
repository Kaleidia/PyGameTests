import pygame
from Tile import Tile
from TileMap import TileMap
from Utils import *

class TileManager(object):
    def __init__(self,tileCount,tileSize):
        self.tileCount = tileCount
        self.tileSize = tileSize
        self.currentTileMap = TileMap(tileCount,"Maps","Map01.txt")
        print(self.currentTileMap)

        self.tiles = []
        #for x in range(0,self.tileCount):
        #    for y in range(0,self.tileCount):
        #        tile = Tile(self.tileSize,x,y,self.currentTileMap.tileMap[x][y])
        #        self.tiles.append(tile)
        self.fillTileMap()

    def update(self,screen):
        for tile in self.tiles:
            screen.blit(tile.surf,tile.pos)

    def loadNewTileMap(self):
        name=self.currentTileMap.currentTransitionMap
        self.currentTileMap= TileMap(self.tileCount,"Maps",f"Map{name}.txt")
        #for x in range(0,self.tileCount):
        #    for y in range(0,self.tileCount):
        #        tile = Tile(self.tileSize,x,y,self.currentTileMap.tileMap[x][y])
        #        self.tiles.append(tile)
        self.fillTileMap()

    def fillTileMap(self):
        for x in range(0,self.tileCount):
            for y in range(0,self.tileCount):
                tile = Tile(self.tileSize,x,y,self.currentTileMap.tileMap[x][y])
                self.tiles.append(tile)


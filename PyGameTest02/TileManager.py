import pygame
from Tile import Tile
from TileMap import TileMap
from Utils import *


class TileManager(object):
    def __init__(self, tileCount, tileSize):
        self.tileCount = tileCount
        self.tileSize = tileSize
        mapsList = ["Map01.txt", "Map02.txt", "Map03.txt"]
        #print(self.currentTileMap)
        #self.tileMaps = []
        self.tileMaps = [TileMap(tileCount, "Maps", mapFile) for mapFile in mapsList]
        #self.tileMaps.append(self.currentTileMap)
        #self.tileMaps.append(TileMap(tileCount, "Maps", "Map02.txt"))
        #self.tileMaps.append(TileMap(tileCount, "Maps", "Map03.txt"))
        self.currentTileMap = self.tileMaps[0]
        self.tiles = self.fillTileMap()

    def update(self, screen):
        [screen.blit(tile.surf, tile.pos) for tile in self.tiles]
            

    def loadNewTileMap(self):
        name = self.currentTileMap.currentTransitionMap
        self.currentTileMap = self.tileMaps[name - 1]
        self.tiles = self.fillTileMap()

    def fillTileMap(self):
        return [Tile(self.tileSize, x, y, self.currentTileMap.tileMap[x][y]) for x in range(self.tileCount) for y in range(self.tileCount)]
        #self.tiles=[]
        #for x in range(0, self.tileCount):
        #    for y in range(0, self.tileCount):
        #        tile = Tile(self.tileSize, x, y, self.currentTileMap.tileMap[x][y])
        #        self.tiles.append(tile)
                #print(len(self.tiles))
                #yield tile
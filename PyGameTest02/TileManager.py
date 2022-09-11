import pygame
from Tile import Tile
from TileMap import TileMap
from Utils import *


class TileManager(object):
    def __init__(self, tileCount, tileSize):
        self.tileCount = tileCount
        self.tileSize = tileSize
        mapsList = ["Map01.txt", "Map02.txt", "Map03.txt"]
        self.tileMaps = [TileMap(tileCount, "Maps", mapFile) for mapFile in mapsList]
        self.xOffset = 0
        self.yOffset = 0
        self.currentMapIndex = 0
        self.currentTileMap = self.tileMaps[self.currentMapIndex]
        self.tiles = self.fillTileMap(0, 0, 0)
        self.tiles.extend(self.fillTileMap(1, -tileCount * tileSize, 0))
        self.tiles.extend(
            self.fillTileMap(2, -tileCount * tileSize, -tileCount * tileSize)
        )

    def update(self, screen):
        #print(f"{(self.tiles[0].pos[0]+(self.xOffset),self.tiles[0].pos[1]+(self.yOffset))}")
        [
            screen.blit(
                tile.surf, (tile.pos[0] + self.xOffset, tile.pos[1] + self.yOffset)
            )
            for tile in self.tiles
        ]

    # def loadNewTileMap(self):
    #    name = self.currentTileMap.currentTransitionMap
    #    self.currentTileMap = self.tileMaps[name - 1]
    #    self.tiles = self.fillTileMap()

    def moveTileMap(self, xOffset, yOffset):
        self.xOffset = xOffset * self.tileCount * self.tileSize + self.xOffset
        self.yOffset = yOffset * self.tileCount * self.tileSize + self.yOffset
        print(f"from map {self.currentMapIndex} to {self.tileMaps[self.currentMapIndex].currentTransitionMap - 1 }")
        self.currentMapIndex = (
            self.tileMaps[self.currentMapIndex].currentTransitionMap - 1
        )
        self.currentTileMap = self.tileMaps[self.currentMapIndex]

    def fillTileMap(self, index, xOffset, yOffset):
        # self.currentMapIndex = index
        return [
            Tile(
                self.tileSize,
                x,
                y,
                self.tileMaps[index].tileMap[x][y],
                xOffset,
                yOffset,
            )
            for x in range(self.tileCount)
            for y in range(self.tileCount)
        ]

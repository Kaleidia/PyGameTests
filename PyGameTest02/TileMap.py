import pygame
#from Tile import Tile
from Utils import *

class TileMap(object):
    def __init__(self,tileCount,path,name):
        self.tileCount = tileCount
        self.transitions = []
        self.transitionMaps = []
        self.currentTransitionMap = 0
        self.tileMap = self.getTileMap(path,name)

    def getTileMap(self,path,name):
        tileMap = [[0 for x in range(self.tileCount)] for y in range(self.tileCount)]
        index=0
        temp=""
        with open(path+os.sep+name) as file:
            lines = [line for line in file.readlines() if len(line) != 0 ]

        self.transitions=lines[0].split(",")
        self.transitionMaps=lines[1].split(",")
        lines.pop(0)
        lines.pop(0)
        for line in lines:
            temp = line.split(",")
            for x in range(0,len(temp)):
                if(temp[x]!="\n"):
                    tileMap[x][index]=int(temp[x])-1
            index+=1

        self.transitions = [line.strip() for line in self.transitions]
        self.transitionMaps = [int(line.strip()) for line in self.transitionMaps]
        return tileMap

    def checkTransition(self, direction):
        #print(f"{direction}?")
        #print(self.transitions[0])
        check = False
        for transition in self.transitions:
            #print(f"{transition} == {direction}?")
            if transition == direction:
                self.currentTransitionMap = self.transitionMaps[self.transitions.index(direction)]
                check = True

        return check
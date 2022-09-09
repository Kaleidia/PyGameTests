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
        f = open(path+os.sep+name)
        index=0
        lines=[]
        temp=""
        while True:
            line = f.readline()
            if len(line) == 0:
                break
            lines.append(line)
        f.close()

        self.transitions=lines[0].split(",")
        self.transitionMaps=lines[1].split(",")
        lines.remove(lines[0])
        lines.remove(lines[0])
        for line in lines:
            temp = line.split(",")
            for y in range(0,len(temp)):
                if(temp[y]!="\n"):
                    tileMap[index][y]=int(temp[y])
            index+=1

        self.transitions = [line.strip() for line in self.transitions]
        self.transitionMaps = [line.strip() for line in self.transitionMaps]
        return tileMap

    def checkTransition(self, direction):
        print(f"{direction}?")
        print(self.transitions[0])
        for transition in self.transitions:
            print(f"{transition} == {direction}?")
            if transition == direction:
                self.currentTransitionMap = self.transitionMaps[self.transitions.index(direction)]
                return True
                break
            else:
                return False
                break

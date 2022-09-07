from asyncio.windows_events import NULL
import os
import pygame

def loadImages(path):
    images = []
    for file_name in os.listdir(path):
        image = pygame.image.load(path+os.sep+file_name).convert_alpha()
        images.append(image)
    return images

def getTileMap(tileCount,path,name):
    tileMap = [[0 for x in range(tileCount)] for y in range(tileCount)]
    f = open(path+os.sep+name)
    index=0
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line)
        temp = line.split(",")
        for y in range(0,len(temp)):
            if(temp[y]!="\n"):
                tileMap[index][y]=int(temp[y])

        index+=1
    f.close()
    print(tileMap)
    return tileMap



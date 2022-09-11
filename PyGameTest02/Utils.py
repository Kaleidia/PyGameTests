import os
import pygame
from pygame.locals import *


def loadImages(path):
    # images =
    # for file_name in os.listdir(path):
    #    image = pygame.image.load(path+os.sep+file_name).convert_alpha()
    #    images.append(image)
    return [
        pygame.image.load(path + os.sep + file_name).convert_alpha()
        for file_name in os.listdir(path)
    ]  # images


def checkKey(event, keyName):
    if keyName == "up":
        if event.key == pygame.K_UP:
            return True
        elif event.key == pygame.K_w:
            return True
        else:
            return False
    elif keyName == "down":
        if event.key == pygame.K_DOWN:
            return True
        elif event.key == pygame.K_s:
            return True
        else:
            return False
    elif keyName == "left":
        if event.key == pygame.K_LEFT:
            return True
        elif event.key == pygame.K_a:
            return True
        else:
            return False
    elif keyName == "right":
        if event.key == pygame.K_RIGHT:
            return True
        elif event.key == pygame.K_d:
            return True
        else:
            return False
    else:
        return False

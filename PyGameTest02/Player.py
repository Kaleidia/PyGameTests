import pygame
from AnimatedSprite import AnimatedSprite
from Utils import loadImages

class Player(AnimatedSprite):
    def __init__(self, spriteSize, position):
        super().__init__(spriteSize, position, loadImages("pix/Player/Right - Idle"), loadImages("pix/Player/Back - Walking"), loadImages("pix/Player/Front - Walking"), loadImages("pix/Player/Left - Walking"), loadImages("pix/Player/Right - Walking"))

    def update(self,dt):
        super().update(dt)




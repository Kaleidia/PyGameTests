import pygame
from AnimatedSprite import AnimatedSprite
from Utils import loadImages

class Player(AnimatedSprite):
    def __init__(self, spriteSize, position):
        super().__init__(spriteSize, position, loadImages("pix/Player/Right - Idle"), loadImages("pix/Player/Back - Walking"), loadImages("pix/Player/Front - Walking"), loadImages("pix/Player/Left - Walking"), loadImages("pix/Player/Right - Walking"), loadImages("pix/Player/Back - Idle"), loadImages("pix/Player/Front - Idle"), loadImages("pix/Player/Left - Idle"), loadImages("pix/Player/Right - Idle"))
        self.speed = 3
        self.animTime = .025

    def update(self,dt):
        super().update(dt)




import math
import pygame
from AnimatedSprite import AnimatedSprite
from Utils import loadImages

class Enemy(AnimatedSprite):
    def __init__(self, spriteSize, position):
        super().__init__(spriteSize, position, loadImages("pix/Enemy/Right - Idle"), loadImages("pix/Enemy/Back - Walking"), loadImages("pix/Enemy/Front - Walking"), loadImages("pix/Enemy/Left - Walking"), loadImages("pix/Enemy/Right - Walking"), loadImages("pix/Enemy/Back - Idle"), loadImages("pix/Enemy/Front - Idle"), loadImages("pix/Enemy/Left - Idle"), loadImages("pix/Enemy/Right - Idle"))
        self.speed = 5
        self.animTime = .025

    def update(self,dt):
        super().update(dt)

    def move(self,player):
        #find player position
        self.targetPos = player.rect
        #get closer to player
        # Find direction vector (dx, dy) between enemy and player.
        dirvect = pygame.math.Vector2(player.rect.x - self.rect.x,
                                      player.rect.y - self.rect.y)
        dirvect.normalize()
        # Move along this normalized vector towards the player at current speed.
        dirvect.scale_to_length(self.speed)

        self.velocity.x = dirvect[0]
        self.velocity.y = dirvect[1]
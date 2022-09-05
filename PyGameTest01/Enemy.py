import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self,screenWidth,screenHeight):
        super(Enemy, self).__init__()
        #self.screenWidth = screenWidth
        #self.screenHeight = screenHeight
        self.surf = pygame.Surface((20,10))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(screenWidth+20,screenWidth+100),
                random.randint(0,screenHeight)
                )
            )
        self.speed = random.randint(5,20)

    def update(self):
        self.rect.move_ip(-self.speed,0)
        if self.rect.right<0:
            self.kill()

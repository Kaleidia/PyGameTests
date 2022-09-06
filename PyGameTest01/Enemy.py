import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self,screen,screenWidth,screenHeight):
        super(Enemy, self).__init__()
        self.screen = screen
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight    
        self.size = .5
        image: self.surf = pygame.image.load("pix/Left - Idle_000.png").convert_alpha()
        self.surf = pygame.transform.scale(image,(image.get_size()[0] * self.size, image.get_size()[1] * self.size))
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

    def BlitMe(self):
        self.screen.blit(self.surf,self.rect)

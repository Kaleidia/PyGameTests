from pathlib import Path
import pygame
import os

from pygame.locals import(
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_a,
    K_s,
    K_d,
    K_w,
    K_ESCAPE,
    KEYDOWN,
    QUIT
    )

def loadImages(path):
    images = []
    for file_name in os.listdir(path):
        image = pygame.image.load(path+os.sep+file_name).convert_alpha()
        images.append(image)
    return images

class Player(pygame.sprite.Sprite):
    def __init__(self,screen,screenWidth,screenHeight):
        super(Player, self).__init__()
        self.screen = screen
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.imageSize = (660,512)

        self.size =.25
        self.changeDirection = False
        image: self.surf = loadImages("pix/Dragon")[0]
        #self.surf.set_colorkey((255,255,255),RLEACCEL)
        self.surf = pygame.transform.scale(image,(image.get_size()[0] * self.size, image.get_size()[1] * self.size))
        self.rect = self.surf.get_rect()

    def update(self,pressedKeys,screen):
        self.screen=screen
        if pressedKeys[K_UP] or pressedKeys[K_w]:
            self.rect.move_ip(0,-5)
        if pressedKeys[K_DOWN] or pressedKeys[K_s]:
            self.rect.move_ip(0,5)
        if pressedKeys[K_LEFT] or pressedKeys[K_a]:
            self.rect.move_ip(-5,0)
            self.changeDirection=True
        if pressedKeys[K_RIGHT] or pressedKeys[K_d]:
            self.rect.move_ip(5,0)
            self.changeDirection=False

        if self.rect.left<0:
            self.rect.left=0
        if self.rect.right>self.screenWidth:
            self.rect.right=self.screenWidth
        if self.rect.top <= 0:
            self.rect.top =0
        if self.rect.bottom>=self.screenHeight:
            self.rect.bottom=self.screenHeight

    def BlitMe(self):
        if self.changeDirection==False:
            self.screen.blit(self.surf,self.rect)
        elif self.changeDirection == True:
            self.screen.blit(pygame.transform.flip(self.surf,True,False),self.rect)

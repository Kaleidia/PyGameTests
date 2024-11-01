from turtle import speed
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
        self.speed = 10
        self.changeDirection = False
        self.allFrames = loadImages("pix/Dragon")
        self.rightImages = self.allFrames
        self.leftImages = [pygame.transform.flip(image, True, False) for image in self.allFrames]
        self.index = 0
        image: self.surf = self.allFrames[self.index]
        #self.surf.set_colorkey((255,255,255),RLEACCEL)
        self.surf = pygame.transform.scale(image,(image.get_size()[0] * self.size, image.get_size()[1] * self.size))
        self.rect = self.surf.get_rect()

        self.animTime = 1.5
        self.currentTime = 0
        self.animFrames = len(self.allFrames)
        self.currentFrame = 0

    def recalcSize(self):
        image: self.surf = self.allFrames[self.index]
        #self.surf.set_colorkey((255,255,255),RLEACCEL)
        posx = self.rect.left
        posy = self.rect.top
        self.surf = pygame.transform.scale(image,(image.get_size()[0] * self.size, image.get_size()[1] * self.size))
        self.rect = self.surf.get_rect()
        self.rect.left=posx
        self.rect.top=posy

    def update(self,pressedKeys,screen,speed, dt):
        self.screen=screen
        if pressedKeys[K_UP] or pressedKeys[K_w]:
            self.rect.move_ip(0,-speed)
        if pressedKeys[K_DOWN] or pressedKeys[K_s]:
            self.rect.move_ip(0,speed)
        if pressedKeys[K_LEFT] or pressedKeys[K_a]:
            self.rect.move_ip(-speed,0)
            self.changeDirection=True
        if pressedKeys[K_RIGHT] or pressedKeys[K_d]:
            self.rect.move_ip(speed,0)
            self.changeDirection=False

        if self.rect.left<0:
            self.rect.left=0
        if self.rect.right>self.screenWidth:
            self.rect.right=self.screenWidth
        if self.rect.top <= 0:
            self.rect.top =0
        if self.rect.bottom>=self.screenHeight:
            self.rect.bottom=self.screenHeight
            
        self.currentTime += dt
        if self.currentTime >= self.animTime:
            self.currentTime = 0
            self.index = (self.index + 1) % len(self.rightImages)
            self.image = self.rightImages[self.index]
            
        self.recalcSize()

    def BlitMe(self):
        if self.changeDirection==False:
            self.screen.blit(self.surf,self.rect)
        elif self.changeDirection == True:
            self.screen.blit(pygame.transform.flip(self.surf,True,False),self.rect)

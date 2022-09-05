import pygame
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

size =.25

class Player(pygame.sprite.Sprite):
    def __init__(self,screenWidth,screenHeight):
        super(Player, self).__init__()
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        image: self.surf = pygame.image.load("pix/Moving Forward_000.png").convert_alpha()
        #self.surf.set_colorkey((255,255,255),RLEACCEL)
        self.surf = pygame.transform.scale(image,(image.get_size()[0] * size, image.get_size()[1] * size))
        self.rect = self.surf.get_rect()

    def update(self,pressedKeys):
        if pressedKeys[K_UP] or pressedKeys[K_w]:
            self.rect.move_ip(0,-5)
        if pressedKeys[K_DOWN] or pressedKeys[K_s]:
            self.rect.move_ip(0,5)
        if pressedKeys[K_LEFT] or pressedKeys[K_a]:
            self.rect.move_ip(-5,0)
        if pressedKeys[K_RIGHT] or pressedKeys[K_d]:
            self.rect.move_ip(5,0)

        if self.rect.left<0:
            self.rect.left=0
        if self.rect.right>self.screenWidth:
            self.rect.right=self.screenWidth
        if self.rect.top <= 0:
            self.rect.top =0
        if self.rect.bottom>=self.screenHeight:
            self.rect.bottom=self.screenHeight





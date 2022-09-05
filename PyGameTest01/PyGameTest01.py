import pygame
import random

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

screenWidth = 800
screenHeight = 600

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("pix/Moving Forward_000.png").convert()
        self.surf.set_colorkey((255,255,255),RLEACCEL)
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
        if self.rect.right>screenWidth:
            self.rect.right=screenWidth
        if self.rect.top <= 0:
            self.rect.top =0
        if self.rect.bottom>=screenHeight:
            self.rect.bottom=screenHeight

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
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

pygame.init()


#create a window
screen = pygame.display.set_mode([screenWidth,screenHeight])

clock = pygame.time.Clock()

addEnemy = pygame.USEREVENT +1
pygame.time.set_timer(addEnemy,250)

player = Player()

enemies = pygame.sprite.Group()
allSprites=pygame.sprite.Group()
allSprites.add(player)

running = True
while running:

    #event loop
    for event in pygame.event.get():

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        #quit event (x) in window title bar
        elif event.type == pygame.QUIT:
            running = False

        elif event.type == addEnemy:
            enemy = Enemy()
            enemies.add(enemy)
            allSprites.add(enemy)

    pressedKeys =pygame.key.get_pressed()

    player.update(pressedKeys)
    enemies.update()

    screen.fill((0,0,0))

    for entity in allSprites:
        screen.blit(entity.surf,entity.rect)

    #update screen
    pygame.display.flip()

    #set framerate
    clock.tick(60)

pygame.quit()

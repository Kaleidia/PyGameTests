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
from Player import Player
from Enemy import Enemy

screenWidth = 800
screenHeight = 600

pygame.init()
pygame.font.init()

myFont = pygame.font.SysFont("Times New Roman",30)

#create a window
screen = pygame.display.set_mode([screenWidth,screenHeight])

clock = pygame.time.Clock()

addEnemy = pygame.USEREVENT +1
pygame.time.set_timer(addEnemy,250)

player = Player(screen,screenWidth,screenHeight)

enemies = pygame.sprite.Group()
allSprites=pygame.sprite.Group()
allSprites.add(player)

score = 0

class Background(pygame.sprite.Sprite):
    def __init__(self):
        super(Background, self).__init__()
        image: self.surf = pygame.image.load("pix/Background - 01.png").convert_alpha()
        self.surf = pygame.transform.scale(image,(screenWidth, screenHeight))
        self.rect = self.surf.get_rect()

bg = Background()
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
            enemy = Enemy(screen,screenWidth,screenHeight)
            enemies.add(enemy)
            allSprites.add(enemy)

    pressedKeys =pygame.key.get_pressed()

    player.update(pressedKeys,screen)
    enemies.update()

    screen.fill((0,0,0))

    screen.blit(bg.surf,bg.rect)
    for entity in allSprites:
        entity.BlitMe()

    hit = pygame.sprite.spritecollide(player,enemies, True)
    if hit:
        score+=1

    textSurface = myFont.render(f"Score: {score}", False,(0,0,0))

    screen.blit(textSurface,(0,0))
    #update screen
    pygame.display.flip()

    #set framerate
    clock.tick(60)

pygame.quit()

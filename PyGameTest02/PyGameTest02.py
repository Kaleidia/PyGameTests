from asyncio.windows_events import NULL
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
from Tile import Tile
from Utils import getTileMap
#from Player import Player
#from Enemy import Enemy

tileSize = 64
tileCount = 5
screenWidth = tileSize * tileCount
screenHeight = screenWidth

pygame.init()
pygame.font.init()

myFont = pygame.font.SysFont("Times New Roman",30)

#create a window
screen = pygame.display.set_mode([screenWidth,screenHeight])
clock = pygame.time.Clock()
tileMap = getTileMap(tileCount,"Maps","Map01.txt")

print(tileMap)

tiles = []
for x in range(0,tileCount):
    for y in range(0,tileCount):
        tile = Tile(tileSize,x,y,tileMap[x][y])
        tiles.append(tile)

#addEnemy = pygame.USEREVENT +1
#pygame.time.set_timer(addEnemy,250)

#player = Player(screen,screenWidth,screenHeight)

#enemies = pygame.sprite.Group()
#allSprites=pygame.sprite.Group()
#allSprites.add(player)

score = 0

#class Background(pygame.sprite.Sprite):
#    def __init__(self):
#        super(Background, self).__init__()
#        image: self.surf = pygame.image.load("pix/Background - 01.png").convert_alpha()
#        self.surf = pygame.transform.scale(image,(screenWidth, screenHeight))
#        self.rect = self.surf.get_rect()

#bg = Background()
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

        #elif event.type == addEnemy:
        #    enemy = Enemy(screen,screenWidth,screenHeight)
        #    enemies.add(enemy)
        #    allSprites.add(enemy)

    pressedKeys =pygame.key.get_pressed()

    #player.update(pressedKeys,screen)
    #enemies.update()

    screen.fill((0,0,0))

    for tile in tiles:
        screen.blit(tile.surf,tile.pos)
    #screen.blit(bg.surf,bg.rect)
    #for entity in allSprites:
    #    entity.BlitMe()

    #hit = pygame.sprite.spritecollide(player,enemies, True)
    #if hit:
    #    score+=1

    #textSurface = myFont.render(f"Score: {score}", False,(255,0,0))

    #screen.blit(textSurface,(0,0))
    #update screen
    pygame.display.flip()

    #set framerate
    clock.tick(60)

pygame.quit()

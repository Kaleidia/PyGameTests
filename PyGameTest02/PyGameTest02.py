import pygame
import random
from pygame.locals import *
from Utils import *

from TileManager import TileManager
from Player import Player
#from Enemy import Enemy

FPS = 60

tileSize = 64
tileCount = 10
screenWidth = tileSize * tileCount
screenHeight = screenWidth

pygame.init()
pygame.font.init()

myFont = pygame.font.SysFont("Times New Roman",30)

#create a window
screen = pygame.display.set_mode([screenWidth,screenHeight])
clock = pygame.time.Clock()

tileManager = TileManager(tileCount,tileSize)
#addEnemy = pygame.USEREVENT +1
#pygame.time.set_timer(addEnemy,250)
halfPlayerWidth = tileSize/2

player = Player(tileSize,(screenWidth/2-halfPlayerWidth,screenWidth/2-halfPlayerWidth))

#enemies = pygame.sprite.Group()
allSprites=pygame.sprite.Group()
allSprites.add(player)

score = 0

running = True
while running:

    dt=clock.tick(FPS) / 1000
    #event loop
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            if checkKey(event,"right"):
                player.velocity.x = player.speed
            elif checkKey(event,"left"):
                player.velocity.x = -player.speed
            elif checkKey(event,"down"):
                player.velocity.y = player.speed
            elif checkKey(event,"up"):
                player.velocity.y = -player.speed
        elif event.type == pygame.KEYUP:
            if checkKey(event,"right") or checkKey(event,"left"):
                player.velocity.x = 0
            elif checkKey(event,"down") or checkKey(event,"up"):
                player.velocity.y = 0
        #quit event (x) in window title bar
        elif event.type == pygame.QUIT:
            running = False

        #elif event.type == addEnemy:
        #    enemy = Enemy(screen,screenWidth,screenHeight)
        #    enemies.add(enemy)
        #    allSprites.add(enemy)

    allSprites.update(dt)
    #enemies.update()
    
    #map transition
    if player.rect[0] < -halfPlayerWidth:
        player.rect[0] = screenWidth-halfPlayerWidth
        #load map in worldmap[xpos][ypos-1]
        print("transition west")
        if tileManager.currentTileMap.checkTransition('west'):
            tileManager.loadNewTileMap()
            tileManager.update(screen)
    elif player.rect[0] > screenWidth-halfPlayerWidth:
        player.rect[0] = -halfPlayerWidth
        print("transition east")
        #load map in worldmap[xpos][ypos+1]
        if tileManager.currentTileMap.checkTransition('east'):
            tileManager.loadNewTileMap()
            tileManager.update(screen)
    elif player.rect[1] < -halfPlayerWidth:
        player.rect[1] = screenWidth-halfPlayerWidth
        print("transition north")
        #load map in worldmap[xpos-1][ypos]
        if tileManager.currentTileMap.checkTransition('north'):
            tileManager.loadNewTileMap()
            tileManager.update(screen)
    elif player.rect[1] > screenWidth-halfPlayerWidth:
        player.rect[1] = -halfPlayerWidth
        print("transition south")
        #load map in worldmap[xpos+1][ypos]
        if tileManager.currentTileMap.checkTransition('south'):
            tileManager.loadNewTileMap()
            tileManager.update(screen)
    screen.fill((0,0,0))

    tileManager.update(screen)
    #hit = pygame.sprite.spritecollide(player,enemies, True)
    #if hit:
    #    score+=1
    #textSurface = myFont.render(f"Score: {score}", False,(255,0,0))
    allSprites.draw(screen)

    #update screen
    pygame.display.update()

pygame.quit()

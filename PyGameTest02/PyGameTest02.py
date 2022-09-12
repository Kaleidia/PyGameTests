import pygame
import random
from pygame.locals import *
from Utils import *

from TileManager import TileManager
from Player import Player
from Enemy import Enemy

FPS = 60

tileSize = 64
tileCount = 10
screenWidth = tileSize * tileCount
screenHeight = screenWidth

pygame.init()
pygame.font.init()

myFont = pygame.font.SysFont("Times New Roman", 30)

# create a window
screen = pygame.display.set_mode([screenWidth, screenHeight])
clock = pygame.time.Clock()

tileManager = TileManager(tileCount, tileSize)
# addEnemy = pygame.USEREVENT +1
# pygame.time.set_timer(addEnemy,250)
halfPlayerWidth = tileSize / 2

player = Player(
    tileSize, (screenWidth / 2 - halfPlayerWidth, screenWidth / 2 - halfPlayerWidth)
)
enemy = Enemy(tileSize, (200, 200))
enemies = pygame.sprite.Group()
enemies.add(enemy)
allSprites = pygame.sprite.Group()
allSprites.add(player)
#allSprites.add(enemies)

score = 0

running = True
while running:

    dt = clock.tick(FPS) / 1000
    # event loop
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            #if event.key == K_q:
            #    tileSize //= 2
            if checkKey(event, "right"):
                player.velocity.x = player.speed
                enemy.move(player)
                #enemies.update(dt, tileManager.xOffset, tileManager.yOffset)
            elif checkKey(event, "left"):
                player.velocity.x = -player.speed
                enemy.move(player)
                #enemies.update(dt, tileManager.xOffset, tileManager.yOffset)
            elif checkKey(event, "down"):
                player.velocity.y = player.speed
                enemy.move(player)
                #enemies.update(dt, tileManager.xOffset, tileManager.yOffset)
            elif checkKey(event, "up"):
                player.velocity.y = -player.speed
                enemy.move(player)
                #enemies.update(dt, tileManager.xOffset, tileManager.yOffset)
        elif event.type == pygame.KEYUP:
            if checkKey(event, "right") or checkKey(event, "left"):
                player.velocity.x = 0
                enemy.move(player)
                #enemies.update(dt, tileManager.xOffset, tileManager.yOffset)
            elif checkKey(event, "down") or checkKey(event, "up"):
                player.velocity.y = 0
                enemy.move(player)
                #enemies.update(dt, tileManager.xOffset, tileManager.yOffset)
        # quit event (x) in window title bar
        elif event.type == pygame.QUIT:
            running = False

        # elif event.type == addEnemy:
        #    enemy = Enemy(screen,screenWidth,screenHeight)
        #    enemies.add(enemy)
        #    allSprites.add(enemy)

    allSprites.update(dt)
    enemy.move(player)
    print(tileManager.xOffset)

    # map transition
    if player.rect[0] < -halfPlayerWidth:
        player.rect[0] = screenWidth - halfPlayerWidth
        # load map in worldmap[xpos][ypos-1]
        print("check for transition west")
        if tileManager.currentTileMap.checkTransition("west"):
            tileManager.moveTileMap(1, 0)
            # tileManager.update(screen)
            print("transitioned west")
            enemies.update(dt, screenWidth, 0)
    elif player.rect[0] > screenWidth - halfPlayerWidth:
        player.rect[0] = -halfPlayerWidth
        print("transition east")
        # load map in worldmap[xpos][ypos+1]
        if tileManager.currentTileMap.checkTransition("east"):
            tileManager.moveTileMap(-1, 0)
            print("transitioned east")
            enemies.update(dt, -screenWidth, 0)
    elif player.rect[1] < -halfPlayerWidth:
        player.rect[1] = screenWidth - halfPlayerWidth
        print("transition north")
        # load map in worldmap[xpos-1][ypos]
        if tileManager.currentTileMap.checkTransition("north"):
            tileManager.moveTileMap(0, 1)
            print("transitioned north")
            enemies.update(dt, 0, screenWidth)
    elif player.rect[1] > screenWidth - halfPlayerWidth:
        player.rect[1] = -halfPlayerWidth
        print("transition south")
        # load map in worldmap[xpos+1][ypos]
        if tileManager.currentTileMap.checkTransition("south"):
            tileManager.moveTileMap(0, -1)
            print("transitioned south")
            enemies.update(dt, 0, -screenWidth)
    else:
        enemies.update(dt, 0, 0)
    screen.fill((0, 0, 0))

    # print(player.rect)
    tileManager.update(screen)

    hit = pygame.sprite.spritecollide(player, enemies, False)
    if hit:
        disvect = pygame.math.Vector2(
            player.rect.x - enemy.rect.x, player.rect.y - enemy.rect.y
        )
        if disvect.length() <= tileSize//2:
            print("i could attack")
            score += 1
            enemy.velocity.x = 0
            enemy.velocity.y = 0
            #running = False
    textSurface = myFont.render(f"Hits: {score}", False, (255, 0, 0))
    allSprites.draw(screen)
    enemies.draw(screen)
    screen.blit(textSurface, (0, 0))

    # update screen
    pygame.display.update()

pygame.quit()

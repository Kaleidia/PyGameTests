import pygame
import random
from pygame.locals import *
from Tile import Tile
from Utils import *
from Player import Player
#from Enemy import Enemy

FPS = 60

tileSize = 128
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

player = Player(tileSize,(100,100))

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
                player.velocity.x = 4
            elif checkKey(event,"left"):
                player.velocity.x = -4
            elif checkKey(event,"down"):
                player.velocity.y = 4
            elif checkKey(event,"up"):
                player.velocity.y = -4
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
    halfPlayerWidth = tileSize/2
    
    #map transition
    if player.rect[0] < -halfPlayerWidth:
        player.rect[0] = screenWidth-halfPlayerWidth
        print("transition west")
        #load map in worldmap[xpos][ypos-1]
    elif player.rect[0] > screenWidth-halfPlayerWidth:
        player.rect[0] = -halfPlayerWidth
        print("transition east")
        #load map in worldmap[xpos][ypos+1]
    elif player.rect[1] < -halfPlayerWidth:
        player.rect[1] = screenWidth-halfPlayerWidth
        print("transition north")
        #load map in worldmap[xpos-1][ypos]
    elif player.rect[1] > screenWidth-halfPlayerWidth:
        player.rect[1] = -halfPlayerWidth
        print("transition south")
        #load map in worldmap[xpos+1][ypos]
    screen.fill((0,0,0))

    for tile in tiles:
        screen.blit(tile.surf,tile.pos)

    #hit = pygame.sprite.spritecollide(player,enemies, True)
    #if hit:
    #    score+=1
    #textSurface = myFont.render(f"Score: {score}", False,(255,0,0))
    allSprites.draw(screen)

    #update screen
    pygame.display.update()

pygame.quit()

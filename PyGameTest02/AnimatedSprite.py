import pygame

class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self,spriteSize,position,images,imagesUp,imagesDown,imagesLeft,imagesRight):
        super(AnimatedSprite,self).__init__()

        size = (spriteSize,spriteSize)

        self.rect = pygame.Rect(position,size)
        self.images = [pygame.transform.scale(image,(spriteSize,spriteSize)) for image in images]
        self.idleImages = [pygame.transform.scale(image,(spriteSize,spriteSize)) for image in images]
        self.rightImages = [pygame.transform.scale(image,(spriteSize,spriteSize)) for image in imagesRight]
        self.leftImages = [pygame.transform.scale(image,(spriteSize,spriteSize)) for image in imagesLeft]
        self.upImages = [pygame.transform.scale(image,(spriteSize,spriteSize)) for image in imagesUp]
        self.downImages = [pygame.transform.scale(image,(spriteSize,spriteSize)) for image in imagesDown]
        self.index = 0
        self.image = images[self.index]

        self.velocity = pygame.math.Vector2(0,0)

        self.animTime = 0.1
        self.currentTime = 0

    def update(self, dt):
        if self.velocity.x > 0:
            self.images = self.rightImages
        elif self.velocity.x < 0:
            self.images = self.leftImages
        elif self.velocity.y > 0:
            self.images = self.downImages
        elif self.velocity.y < 0:
            self.images = self.upImages
        else:
            self.images = self.idleImages

        self.currentTime += dt
        if self.currentTime >= self.animTime:
            self.currentTime = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

        self.rect.move_ip(*self.velocity)

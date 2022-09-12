import pygame


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(
        self,
        spriteSize,
        position,
        images,
        imagesUp,
        imagesDown,
        imagesLeft,
        imagesRight,
        imagesIdleUp,
        imagesIdleDown,
        imagesIdleLeft,
        imagesIdleRight,
    ):
        super(AnimatedSprite, self).__init__()

        self.spriteSize = spriteSize

        size = (spriteSize, spriteSize)

        self.rect = pygame.Rect(position, size)
        self.images = self.iterateImages(images)
        self.idleImages = self.iterateImages(images)
        self.rightImages = self.iterateImages(imagesRight)
        self.leftImages = self.iterateImages(imagesLeft)
        self.upImages = self.iterateImages(imagesUp)
        self.downImages = self.iterateImages(imagesDown)
        self.rightIdleImages = self.iterateImages(imagesIdleRight)
        self.leftIdleImages = self.iterateImages(imagesIdleLeft)
        self.upIdleImages = self.iterateImages(imagesIdleUp)
        self.downIdleImages = self.iterateImages(imagesIdleDown)
        self.index = 0
        self.image = images[self.index]

        self.direction = "right"

        self.velocity = pygame.math.Vector2(0, 0)

        self.animTime = 0.1
        self.currentTime = 0

    def update(self, dt):
        if self.velocity.x > 0:
            self.images = self.rightImages
            self.direction = "right"
        elif self.velocity.x < 0:
            self.images = self.leftImages
            self.direction = "left"
        elif self.velocity.y > 0:
            self.images = self.downImages
            self.direction = "down"
        elif self.velocity.y < 0:
            self.images = self.upImages
            self.direction = "up"
        else:
            if self.direction == "right":
                self.images = self.rightIdleImages
            if self.direction == "left":
                self.images = self.leftIdleImages
            if self.direction == "down":
                self.images = self.downIdleImages
            if self.direction == "up":
                self.images = self.upIdleImages

        self.currentTime += dt
        if self.currentTime >= self.animTime:
            self.currentTime = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

        self.rect.move_ip(*self.velocity)

    def iterateImages(self, imageList):
        return [
            pygame.transform.scale(image, (self.spriteSize, self.spriteSize))
            for image in imageList
        ]

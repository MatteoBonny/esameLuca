from globale import*
import random


class Macchina:

    def __init__(self):
        self.img = pygame.transform.scale(pygame.image.load("v1.png"), (110, 260))
        self.rect = self.img.get_rect()
        self.x = random.randint(140, 540 - self.img.get_width())
        self.y = 0 - self.img.get_height()
        self.speed = 10


    def update(self):
        self.y += self.speed
        screen.blit(self.img, (self.x, self.y))










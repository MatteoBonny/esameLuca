from globale import*
import random


class Macchina:

    def __init__(self):
        self.img = pygame.transform.scale(pygame.image.load(random.choice(veicoli)), (90, 240))
        self.rect = self.img.get_rect()
        self.x = random.choice(random_macchina)
        self.y = 0 - self.img.get_height()
        self.rect.x = self.x
        self.rect.y = self.y
        self.speed = None
        self.aumentaVel(0)


    def update(self,score):
        self.rect.y += self.speed
        screen.blit(self.img, self.rect)
        self.aumentaVel(score)

    def checkCollide(self, elemento2):
        return pygame.Rect.colliderect(self.rect, elemento2)

    def aumentaVel(self, score):#privata uso solo in update
        if score == 0:
            self.speed = 10
        else:
            score >= 10
            self.speed = self.speed * 1.02
        if score >= 20:
            self.speed = self.speed * 1.04

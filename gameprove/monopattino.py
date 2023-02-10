from globale import *

class Monopattino:

    def __init__(self):
        self.img = monopattini[0]
            #pygame.transform.scale(pygame.image.load("mono1.png"), (60, 125))
        self.rect = self.img.get_rect()
        self.x = SCREEN_WIDTH/2 - self.img.get_width()/2
        self.y = SCREEN_HEIGHT - self.img.get_height()
        self.rect.x = self.x
        self.rect.y = self.y
        self.speed = 8.5


    def update(self, score):
        # Key per movimento
        keys = pygame.key.get_pressed()

        if score >= 0:#sblocca livello successivo
            self.img = monopattini[1]
        else:
            self.img = monopattini[0]
        if score == 0:
            screen.blit(mattia, (130, SCREEN_HEIGHT / 2 - 100))#mattia
        if score >= 1 and self.img == monopattini[1]:
            self.img = pygame.transform.scale(monopattini[2], (100, 50))

#devo mettere il rect della nuova immagine in quella vecchia


        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        elif keys[pygame.K_w] or keys[pygame.K_UP]:
            self.rect.y -= self.speed
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # personaggio che non esce
        if self.rect.x < 60:
            self.rect.x = 60
        if self.rect.x > SCREEN_WIDTH - 140:
            self.rect.x = SCREEN_WIDTH - 140
        if self.rect.y <= 50:
            self.rect.y = 50
        if self.rect.y >= SCREEN_HEIGHT - 150:
            self.rect.y = SCREEN_HEIGHT - 150

        screen.blit(self.img, self.rect) #print screnn


    def checkCollide(self, elemento2):
        return pygame.Rect.colliderect(self.rect, elemento2)
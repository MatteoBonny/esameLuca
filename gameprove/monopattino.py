from globale import*


class Monopattino:

    def __init__(self):
        self.img = pygame.transform.scale(pygame.image.load("mono.png"), (80, 145))
        self.rect = self.img.get_rect()
        self.x = SCREEN_WIDTH/2 - self.img.get_width()/2
        self.y = SCREEN_HEIGHT - self.img.get_height()
        self.rect.x = self.x
        self.rect.y = self.y
        self.speed = 8.5


    def update(self):
        # Key per movimento
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        elif keys[pygame.K_d]:
            self.rect.x += self.speed
        elif keys[pygame.K_w]:
            self.rect.y -= self.speed
        elif keys[pygame.K_s]:
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
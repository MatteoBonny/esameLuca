from globale import*


class Monopattino:

    def __init__(self):
        self.img = pygame.transform.scale(pygame.image.load("mono.png"), (80, 145))
        self.rect = self.img.get_rect()
        self.x = SCREEN_WIDTH/2 - self.img.get_width()/2
        self.y = SCREEN_HEIGHT - self.img.get_height()
        self.speed = 8.5


    def update(self):
        # Key per movimento
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x -= self.speed
        elif keys[pygame.K_d]:
            self.x += self.speed
        elif keys[pygame.K_w]:
            self.y -= self.speed
        elif keys[pygame.K_s]:
            self.y += self.speed

        # personaggio che non esce
        if self.x < 60:
            self.x = 60
        if self.x > SCREEN_WIDTH - 140:
            self.x = SCREEN_WIDTH - 140
        if self.y <= 400:
            self.y = 400
        if self.y >= SCREEN_HEIGHT - 150:
            self.y = SCREEN_HEIGHT - 150

        screen.blit(self.img, (self.x, self.y)) #print screnn


    def checkCollide(self, elemento2):
        return pygame.Rect.colliderect(self.rect, elemento2)
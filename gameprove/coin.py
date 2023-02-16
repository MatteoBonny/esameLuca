from globale import*


class Coin:

    def __init__(self):
        self.img = pygame.image.load("coin.png")
        self.rect = self.img.get_rect()
        self.x = random.randint(140, 540 - 84)
        self.y = 0 - SCREEN_WIDTH
        self.frame_width = 84
        self.frame_height = 84
        self.coin = pygame.sprite.Sprite()
        self.coin.frames = []

        for i in range(0, self.img.get_width(), self.frame_width):
            for j in range(0, self.img.get_height(), self.frame_height):
                self.coin.frames.append(pygame.transform.scale(self.img.subsurface(i, j, self.frame_width, self.frame_height), (50, 50)))

        # Creazione del giocatore
        self.coin.img = self.coin.frames[0]
        self.coin.frame_index = 0
        self.rect = self.coin.img.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.rect.y += 10
        self.coin.frame_index = (self.coin.frame_index + 1) % len(self.coin.frames)
        screen.blit(self.coin.frames[self.coin.frame_index], self.rect)#print screen

    def checkCollide(self, elemento2):
        return pygame.Rect.colliderect(self.rect, elemento2)

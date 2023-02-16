from globale import*


class Dia:

    def __init__(self):
        self.img = pygame.image.load("diam.png")
        self.rect = self.img.get_rect()
        self.x = random.randint(140, 540 - 84)
        self.y = 0 - SCREEN_WIDTH
        self.frame_width = 84
        self.frame_height = 84
        self.diamond = pygame.sprite.Sprite()
        self.diamond.frames = []

        for i in range(0, self.img.get_width(), self.frame_width):
            for j in range(0, self.img.get_height(), self.frame_height):
                self.diamond.frames.append(pygame.transform.scale(self.img.subsurface(i, j, self.frame_width, self.frame_height), (50, 50)))

        # Creazione del giocatore
        self.diamond.img = self.diamond.frames[0]
        self.diamond.frame_index = 0
        self.rect = self.diamond.img.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.rect.y += 10
        print(self.rect.y)
        self.diamond.frame_index = (self.diamond.frame_index + 1) % len(self.diamond.frames)
        screen.blit(self.diamond.frames[self.diamond.frame_index], self.rect)#print screen

    def checkCollide(self, elemento2):
        return pygame.Rect.colliderect(self.rect, elemento2)

import pygame, math
import random
from pygame import font

monopattini = []
for i in range(3):
    img = pygame.transform.scale(pygame.image.load("mono" + str(i + 1) + ".png"), (50, 105))
    monopattini.append(img)

veicoli = ("v1.png", "v2.png","v3.png","v4.png")

pygame.init()

clock = pygame.time.Clock()
FPS = 40

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

#create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("bonny's game")
#load image
bg = pygame.image.load("strada vuota.png").convert()
bg = pygame.transform.scale (bg,(600,800))
bg_height = bg.get_height()
bg_rect = bg.get_rect()



#define game variables
scroll = bg_height
tiles = math.ceil(SCREEN_WIDTH / bg_height) + 1

#text
sfstart = pygame.image.load("sfstart.png")

stile = pygame.font.Font("font4.ttf", 70)
RED = (255, 0, 0)
BLU = (0, 0, 230)
start = False
gameover = False
start1 = stile.render("'S'-START", True, RED)
game_over = stile.render("'R'-RESTART", True, RED)
game_over2 = stile.render("'Q'-QUIT", True, RED)

mattia = stile.render("MATTIA!", True, BLU)
cri = stile.render("CRI!", True, BLU)



scroll -= 4

MacchinaSpawnRate = 80
CoinSpawnRate = 50



random_macchina = [90, 200, 310, 420]#spwan x macchine

#suono
main = pygame.mixer.Sound('soundHome.wav').play()
main.set_volume(.5)
# main.stop()


# timeScroll =
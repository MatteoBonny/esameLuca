import pygame
import math
import random

from pygame import font

pygame.init()

clock = pygame.time.Clock()
FPS = 50
score = 0

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
RED = (255,0,0)
stile = pygame.font.Font("GAME_glm.ttf", 70)
race = stile.render("race", 10, True, RED)
gameover = stile.render("'Z' TO RESTAR", True, RED)

scroll -= 4

MacchinaSpawnRate = 100
CoinSpawnRate = 1


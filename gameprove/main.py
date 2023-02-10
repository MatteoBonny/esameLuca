from globale import *
from macchina import Macchina
from monopattino import Monopattino
from coin import Coin

#dichiaro classi
mp = Monopattino()

start = True
gameover = False
macchine = []#array macchine
coins = []#array coin
score = 0

def gameLoop(scroll, macchine, coins, score, gameover, start, screen_prova):
    #game loop
    run = True
    while run:
      # event handler
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              run = False


      clock.tick(FPS)
      # scroll background

      scroll -= 4

      # draw scrolling background
      for i in range(0, tiles):
          screen.blit(bg, (0, i * bg_height - scroll))
          bg_rect.x = i * bg_height - scroll

      # reset scroll
      if scroll < 0:
          scroll = bg_height

      if pygame.time.get_ticks()%MacchinaSpawnRate == 0 :#spawncar
        macchine.append(Macchina())
      if pygame.time.get_ticks()%CoinSpawnRate == 0 :#spawncoin
        coins.append(Coin())


      for i in macchine:
        i.update()
        if i.rect.y > SCREEN_HEIGHT:#rimuovi macchina dopo screen
          macchine.remove(i)
        if mp.checkCollide(i.rect):
            gameover = True



      for i in coins:
        i.update()
        if i.rect.y > SCREEN_HEIGHT:#rimuovi coin dopo screen
          coins.remove(i)
        if mp.checkCollide(i.rect):
          coins.remove(i)
          score += 1
        for j in macchine:#remove coin sovrapposto a macchina
          if i.checkCollide(j.rect):
            coins.remove(i)


      mp.update(score)#update screen monopattino

      scoreText = stile.render("score: " + str(score), True, RED)
      screen.blit(scoreText, (10, 10))

      if gameover:
          screen.fill((255, 255, 255))
          screen.blit(game_over, (SCREEN_WIDTH / 2 - game_over.get_width() / 2, SCREEN_HEIGHT / 2 - game_over.get_height() / 2))
          screen.blit(game_over2, (50, SCREEN_HEIGHT / 2 - 100))
          keys = pygame.key.get_pressed()
          score = 0
          monopattini = [0]

          if keys[pygame.K_r]:
              gameover = False
              macchine = []
              coins = []
              pygame.display.update()
          elif keys[pygame.K_q]:
              run = False

          else:
              gameover = True


      if start == True: #menu principale/perche senno sopra altro ...
          screen.fill((255, 255, 255))
          screen.blit(start1, (SCREEN_WIDTH / 2 - start1.get_width() / 2, SCREEN_HEIGHT / 2 - start1.get_height() / 2))
          score = 0
          monopattini = [0]
          keys = pygame.key.get_pressed()

          if keys[pygame.K_s]:
              start = False
              macchine = []
              coins = []

      pygame.display.update()
    pygame.quit()

gameLoop(scroll, macchine, coins, score, gameover, start, screen)



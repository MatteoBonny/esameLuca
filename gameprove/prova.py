from globale import*
from macchina import Macchina
from monopattino import Monopattino
from coin import Coin

#dichiaro classi
mp = Monopattino()

macchine = []#array macchine
coins = []#array coin


for i in range(3):
  coins.append(Coin())


#game loop
run = True
while run:
  # event handler
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          run = False




  clock.tick(FPS)

  #draw scrolling background
  for i in range(0, tiles):
    screen.blit(bg, (0, i * bg_height - scroll))
    bg_rect.x = i * bg_height - scroll

  #scroll background
  scroll -= 4

  #reset scroll
  if scroll < 0:
    scroll = bg_height


  if pygame.time.get_ticks()%MacchinaSpawnRate == 0 :
    macchine.append(Macchina())
  elif  pygame.time.get_ticks()%CoinSpawnRate == 0 :
    coins.append(Coin())

  mp.update()#update screen monopattino

  for i in macchine:
    i.update()
    if i.y > SCREEN_HEIGHT:#rimuovi macchina dopo screen
      macchine.remove(i)
    if mp.checkCollide(i.rect):
      run = False

  for i in coins:
    i.update()
    if i.y > SCREEN_HEIGHT:#rimuovi coin dopo screen
      coins.remove(i)
    if mp.checkCollide(i.rect):
      score += 1



  #     while (run == False):
  #         screen.fill((255, 255, 255))
  #         screen.blit(gameover,(SCREEN_WIDTH / 2 - gameover.get_width() / 2, SCREEN_HEIGHT / 2 - gameover.get_height() / 2))
  #         print("suca")
  #
  #         keys = pygame.key.get_pressed()
  #         if keys[pygame.K_z]:
  #           print("ciao")
  #           run = True
  #         pygame.display.update()

  screen.blit(scoreText, (10, 10))
  pygame.display.update()
pygame.quit()
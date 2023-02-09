from globale import*
from macchina import Macchina
from monopattino import Monopattino
from coin import Coin

#dichiaro classi
mp = Monopattino()

macchine = []#array macchine
coins = []#array coin


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


  if pygame.time.get_ticks()%MacchinaSpawnRate == 0 :#spawncar
    macchine.append(Macchina())
  if pygame.time.get_ticks()%CoinSpawnRate == 0 :#spawncoin
    coins.append(Coin())
    print("coin spawnato")


  for i in macchine:
    i.update()
    if i.rect.y > SCREEN_HEIGHT:#rimuovi macchina dopo screen
      macchine.remove(i)
    if mp.checkCollide(i.rect):
      run = False

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


  while (run == False) :#gameover
    screen.fill((255, 255, 255))
    screen.blit(gameover,(SCREEN_WIDTH / 2 - gameover.get_width() / 2, SCREEN_HEIGHT / 2 - gameover.get_height() / 2))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_z]:
     print("ciao")
     run = True
     pygame.display.update()

  mp.update()#update screen monopattino

  scoreText = stile.render("score: " + str(score), True, RED)
  screen.blit(scoreText, (10, 10))
  pygame.display.update()
pygame.quit()
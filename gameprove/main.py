from globale import*
from macchina import Macchina
from monopattino import Monopattino


#dichiaro classi
m1 = Macchina()
mp = Monopattino()


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

  mp.update()
  m1.update()#update screen macchine

  pygame.display.update()

pygame.quit()
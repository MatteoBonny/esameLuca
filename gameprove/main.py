from globale import *
from macchina import Macchina
from monopattino import Monopattino
from coin import Coin
from diamond import Dia

# dichiaro classi
mp = Monopattino()

start = True
gameover = False
macchine = []  # array macchine
coins = []  # array coin
dia = []
score = 0
scoreText = stile.render("score: " + str(score), True, RED)


def gameLoop(scroll, macchine, coins, gameover, start, screen, dia, DiaSpawnRate = 60, score=0):
    # game loop
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

        if pygame.time.get_ticks() % MacchinaSpawnRate == 0:  # spawncar (segna il resto della mia divisione)
            macchine.append(Macchina())
        if pygame.time.get_ticks() % CoinSpawnRate == 0:  # spawncoin
            coins.append(Coin())
        if pygame.time.get_ticks() % DiaSpawnRate == 0:  # spawn dia
            dia.append(Dia())

        print(DiaSpawnRate)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_e]:
            if keys[pygame.K_g]:
              DiaSpawnRate = 1



        for i in macchine:
            i.update(score)
            if i.rect.y > SCREEN_HEIGHT:  # rimuovi macchina dopo screen
                macchine.remove(i)
            if mp.checkCollide(i.rect):
                gameover = True

        for i in coins:
            i.update()
            if i.rect.y > SCREEN_HEIGHT:  # rimuovi coin dopo screen
                coins.remove(i)
            if mp.checkCollide(i.rect):
                coins.remove(i)
                score += 1

            for j in macchine:  # remove coin sovrapposto a macchina
                if i.checkCollide(j.rect):
                    coins.remove(i)

        # diamanti
        for r in dia:
            r.update()
            if r.rect.y > SCREEN_HEIGHT:  # rimuovi dia dopo screen
                dia.remove(r)
            if mp.checkCollide(r.rect):
                dia.remove(r)
                score += 5

            for j in macchine:  # remove dia sovrapposto a macchina
                if r.checkCollide(j.rect):
                    dia.remove(r)

        mp.update(score)  # update screen monopattino

        scoreText = stile.render("score: " + str(score), True, RED)
        screen.blit(scoreText, (10, 10))

        if gameover:
            screen.blit(sfstart, (0, 0))
            screen.blit(game_over, (SCREEN_WIDTH / 2 - game_over.get_width() / 2, SCREEN_HEIGHT / 2 - 370))
            screen.blit(game_over2, (50, SCREEN_HEIGHT / 2 - 300))
            keys = pygame.key.get_pressed()
            score = 0
            monopattini = [0]
            DiaSpawnRate = 60


            if keys[pygame.K_r]:
                gameover = False
                macchine = []
                coins = []
                dia = []
                pygame.display.update()
            elif keys[pygame.K_q]:
                run = False

            else:
                gameover = True

        if start == True:  # menu principale/perche senno sopra altro ...
            screen.blit(sfstart, (0, 0))
            screen.blit(start1, (SCREEN_WIDTH / 2 - start1.get_width() / 2, SCREEN_HEIGHT / 2 - 330))
            score = 0
            monopattini = [0]
            keys = pygame.key.get_pressed()

            if keys[pygame.K_s]: #start del gioco
                start = False
                macchine = []
                coins = []
                dia = []


        pygame.display.update()
    pygame.quit()


gameLoop(scroll, macchine, coins, gameover, start, screen, dia)

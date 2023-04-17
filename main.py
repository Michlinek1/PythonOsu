import pygame
from random import randint, choice
from time import sleep

WIDTH = 800
HEIGHT = 800
BIALY = (255,255,255)
SZARY = (128, 128, 128)
ZLOTY = (255, 215, 0)
KOLORKOLA = (randint(0,255), randint(0,255), randint(0,255))
RANDOMKOLORY = [ZLOTY,(randint(0,255), randint(0,255), randint(0,255))]

pygame.init()
pygame.font.init()

ekran = pygame.display.set_mode([WIDTH, HEIGHT])
ekran.fill(BIALY)

font = pygame.font.Font('C:/Windows/Fonts/arial.ttf', 32)

#bomba = pygame.image.load("bomba.png")
#bomba_rect = bomba.get_rect()

pygame.display.flip()

kolo_pozycja = (randint(10, WIDTH), randint(10, HEIGHT))

fps = pygame.time.Clock()

punkty = 0

game_working = True
kolo_namaluj = True
game_paused = False
circle_clickable = True

while game_working:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            game_working = False
            pygame.quit()
            exit()
        elif events.type == pygame.KEYDOWN:
            if events.key == pygame.K_SPACE:
                if ekran.get_at((0,0)) == SZARY:
                    ekran.fill(BIALY)
                    circle_clickable = True
                    game_paused = False
                else:
                    ekran.fill(SZARY)
                    circle_clickable = False
                    game_paused = True

        elif events.type == pygame.MOUSEBUTTONDOWN:
            #if bomba_rect.collidepoint(events.pos):
                #punkty = 0
                #pygame.display.update()
            if circle_clickable:
                click = ekran.get_at(pygame.mouse.get_pos()) == KOLORKOLA
                if click == 1 and kolo_namaluj:
                    if KOLORKOLA == ZLOTY:
                        punkty +=2
                    else:
                        punkty +=1
                    ekran.fill(BIALY, (kolo_pozycja[0]-10, kolo_pozycja[1]-10, 20, 20))
                    kolo_pozycja = (randint(0, WIDTH), randint(0, HEIGHT))
                    KOLORKOLA = choice([ZLOTY,(randint(0,255), randint(0,255), randint(0,255))])
                    kolo_namaluj = False
    if game_paused == False:
        #if(randint(1,10)) == 5:
            #bomba_rect = bomba.get_rect(center = (randint(10,WIDTH),randint(10,WIDTH)))
        if kolo_namaluj:
            #choice([pygame.draw.circle(ekran, KOLORKOLA, kolo_pozycja, 10), ekran.blit(bomba, bomba_rect)])
            pygame.draw.circle(ekran, KOLORKOLA, kolo_pozycja, 10)
        else:
            kolo_namaluj = True
    else:
        fontMniejszy = pygame.font.Font('C:/Windows/Fonts/arial.ttf', 20)
        napis = font.render("Gra zastopowana", True, BIALY)
        napisMniejszy = fontMniejszy.render("Kliknij 'spacja' aby kontunuowac", True, BIALY)
        ekran.blit(napis, (250, 390)) 
        ekran.blit(napisMniejszy, (250, 420))
        pygame.display.update()

    tekstPunkty = font.render(f"Punkty: {punkty}", True, (0,0,0), BIALY)
    ekran.blit(tekstPunkty, (10,10))

    pygame.display.update()
    fps.tick(60)
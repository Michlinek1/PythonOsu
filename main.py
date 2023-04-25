import pygame
from random import randint, choice
from time import sleep,perf_counter
WIDTH = 800
HEIGHT = 800
BIALY = (255,255,255)
SZARY = (128, 128, 128)
ZLOTY = (255, 215, 0)
KOLORKOLA = (randint(0,255), randint(0,255), randint(0,255))


pygame.init()
pygame.font.init()

ekran = pygame.display.set_mode([WIDTH, HEIGHT])
ekran.fill(BIALY)

font = pygame.font.Font('C:/Windows/Fonts/arial.ttf', 32)

pygame.display.flip()

kolo_pozycja = (randint(10, WIDTH), randint(10, HEIGHT))

fps = pygame.time.Clock()

punkty = 5
randRadius = randint(5,10)

game_working = True
kolo_namaluj = True
game_paused = False
circle_clickable = True
won = False
start = perf_counter()

imie = 'Michal'
nazwaPliku = f"czas{imie}.txt"
def zapiszCzas(Czas):
    with open(nazwaPliku, "a+", encoding="UTF-8") as plik:
        plik.seek(0)
        liczba_linii = sum(1 for line in plik) + 1
        plik.write(f"{liczba_linii}: Twój czas: {Czas:.2f} \n")
        

def zobaczCzas():
    czasy = []
    with open(nazwaPliku, "r+") as plik:
        for line in plik:
            slowa = line.split()
            czasy.append(slowa[3])
    
    return czasy
    

            

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
            elif events.key == pygame.K_ESCAPE:
                ekran.fill(SZARY)
                circle_clickable = False
                game_paused = True
                czas_str = "Twoje czasy:" + " " + str(zobaczCzas()).replace("[", "").replace("]", "").replace("'", "")
                czas = font.render(czas_str, True, BIALY)
                ekran.blit(czas, (100, 200))

        elif events.type == pygame.MOUSEBUTTONDOWN:
            if circle_clickable:
                click = ekran.get_at(pygame.mouse.get_pos()) == KOLORKOLA
                if click == 1 and kolo_namaluj:
                    if KOLORKOLA == ZLOTY:
                        punkty +=2
                    else:
                        punkty +=1
                    ekran.fill(BIALY, (kolo_pozycja[0]-randRadius, kolo_pozycja[1]-randRadius, randRadius + 20, randRadius + 20))
                    kolo_pozycja = (randint(0, WIDTH), randint(0, HEIGHT))
                    randRadius = randint(5,20)
                    print(randRadius)
                    KOLORKOLA = choice([ZLOTY,(randint(0,255), randint(0,255), randint(0,255))])
                    kolo_namaluj = False
                    
    if punkty >= 10 and not won:
        stop = perf_counter()
        won = True
        game_paused = True
        zapiszCzas(stop - start)                
        
    if game_paused == False:
        if kolo_namaluj:
            pygame.draw.circle(ekran, KOLORKOLA, kolo_pozycja, randRadius)
        else:
            kolo_namaluj = True
    else:
        if won:
            ekran.fill(SZARY)
            czas = stop - start
            text = font.render(f'Wygrałeś! Twój czas: {czas:.2f}', True, BIALY)
            ekran.blit(text, (WIDTH//2 - 200, HEIGHT//2))
            
            
        else:  
            fontMniejszy = pygame.font.Font('C:/Windows/Fonts/arial.ttf', 20)
            napis = font.render("Gra zastopowana", True, BIALY)
            napisMniejszy = fontMniejszy.render("Kliknij 'spacja' aby kontunuowac", True, BIALY)
            ekran.blit(napis, (250, 390)) 
            ekran.blit(napisMniejszy, (250, 420))
            pygame.display.update()
    if won == False:
        tekstPunkty = font.render(f"Punkty: {punkty}", True, (0,0,0), BIALY)
        ekran.blit(tekstPunkty, (10,10))
    else:
        pass

    pygame.display.update()
    fps.tick(60)

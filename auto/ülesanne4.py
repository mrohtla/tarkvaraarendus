import pygame, sys, random, time #impordib moodulid

pygame.init()#käivitab pygame mooduli
#ekraandi suurus
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])

pygame.display.set_caption("auto :)")#ekraani nimi

#aeg
clock = pygame.time.Clock()
start_time = time.time()
skoor = 0

#laeb vajalikud pildid
taust = pygame.image.load("bg_rally.jpg")
p_auto = pygame.image.load("f1_red.png")
s_auto1 = pygame.image.load("f1_blue.png")
s_auto2 = pygame.image.load("f1_blue.png")

#tausta asukohad
PosBGY1 = 0
PosBGY2 = -480

#pöörab sinised autod õiget pidi
s_auto1 = pygame.transform.rotate(s_auto1, 180)
s_auto2 = pygame.transform.rotate(s_auto2, 180)

#paigutab pildid
#screen.blit(taust, (0, 0))
screen.blit(p_auto, (300, 385))
screen.blit(s_auto1, (170, 150))
screen.blit(s_auto2, (420, 10))

#lisab kiiruse
BspeedY = 2

#auto asukohad ja kiirused
BposY = random.randint(0, 100)
B2posY = random.randint(0, 100)
RposX, RposY = 298, 390
RspeedY = 0
gameover = False
BposX = random.randint(450, 460)
B2posX = random.randint(450, 460)
while not gameover:
    #fps
    clock.tick(120)
    #ristist kinni panemiseks
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

#kiirus
    #screen.blit(taust, (0, 0))
    screen.blit(s_auto1, (BposX, BposY))
    screen.blit(s_auto2, (B2posX, B2posY))
    BposY += BspeedY
    B2posY += BspeedY+1
    screen.blit(p_auto, (RposX, RposY))
    RposY += RspeedY
    #skoor
    screen.blit(pygame.font.Font(None, 30).render(f"Skoor: {skoor}", True, [255, 255, 255]), [10, 460])

    if BposY >= 480:
        BposY = -120
        skoor+= 1
        BposX = random.randint(130, 280)

#nooltega liikumine
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        RposY -= 5
    if keys[pygame.K_DOWN]:
        RposY += 5
    if keys[pygame.K_LEFT]:
        RposX -= 5
    if keys[pygame.K_RIGHT]:
        RposX += 5

    if B2posY >= 480:
        B2posY = -120
        skoor += 1
        B2posX = random.randint(300, 480)

    if RposY >= 480:
        RposY = -120


    if B2posY <= RposY + 58 and B2posY >= RposY - 58:
        if B2posX <= RposX + 55 and B2posX >= RposX - 55:
            gameover = True

    if BposY <= RposY + 58 and BposY >= RposY - 58:
        if BposX <= RposX + 55 and BposX >= RposX - 55:
            gameover = True
    if time.time() % 10 == 0:
        BspeedY += 1

    pygame.display.flip()
    a = 1
    if a < 2:
        PosBGY1 += 3
        if PosBGY1 == 480:
            PosBGY1 -= 480
        PosBGY2 += 3
        if PosBGY2 == 0:
            PosBGY2 -= 480
    screen.blit(taust, [0, PosBGY1])
    screen.blit(taust, [0, PosBGY2])

    screen.blit(pygame.font.Font(None, 25).render(f"Aeg: {int(time.time() - start_time)}", True, [255, 255, 255]), [519, 40])

    #pygame.display.flip()
gameoverbg = pygame.image.load("gameover.png")
while True:

    if gameover == True:
        screen.blit(gameoverbg, (0, 0))
        screen.blit(pygame.font.Font(None, 50).render(f"Score: {skoor}", True, [255, 255, 255]), [250, 400])
        pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


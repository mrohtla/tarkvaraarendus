import pygame, random
pygame.init()

# ekraani seaded
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("PINGPONG!!!!!!!!!!!!!!!!!!!!!!")
screen.fill([153, 204, 255])
clock = pygame.time.Clock()
posX, posY = 0, 0
speedX, speedY = 3, 4
speedX2, speedY2 = 2, 2
#pall
pall = pygame.Rect(posX, posY, 20, 20)
pall = pygame.image.load("ball.png")

posX2, posY2 = 300, 350
palk = pygame.Rect(posX2, posY2, 120, 20)
palkImage = pygame.image.load("pad.png")
palkImage = pygame.transform.scale(palkImage, [palk.width, palk.height])



#palli liikumine
gameover = False
while not gameover:
    clock.tick(60)
    # mängu sulgemine ristist
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    # player liikumine
    player = pygame.Rect(posX, posY, 20, 20)
    screen.blit(pall, player)

    posX += speedX
    posY += speedY

    if posX > screenX - pall.get_rect().width or posX < 0:
        speedX = -speedX

    if posY > screenY - pall.get_rect().height or posY < 0:
        speedY = -speedY

    posX2, posY2 = 300, 350
    palk = pygame.Rect(posX2, posY2, 120, 20)
    palkImage = pygame.image.load("pad.png")
    palkImage = pygame.transform.scale(palkImage, [palk.width, palk.height])
    screen.blit(palkImage, palk)
    if player.colliderect(palk) and speedY > 0:
        print("aaa")
        speedY = -speedY
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            posX2 = 3
        elif event.key == pygame.K_LEFT:
            posX2 = -3
            print('ahsdadhb')

    pygame.display.flip()
    screen.fill([153, 204, 255])


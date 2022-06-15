import pygame, random, time, sys


pygame.init()
FPS = 15
BLACK = (0, 0, 0)
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
VELOCITY = 10
SNAKE_WIDTH = 15
APPLE_SIZE = 20
TOP_WIDTH = 40

#fondid
small_font = pygame.font.SysFont('Comic sans', 25)
medium_font = pygame.font.SysFont('Comic sans', 20, True)
large_font = pygame.font.SysFont('Comic sans', 40, True, True)

#värvid
valge = (255, 255, 255)
heleroosa = (255, 204, 238)
tumeroosa = (128, 0, 64)
erkroosa = (255, 26, 179)


dis_width = 600 #laius
dis_height = 600 #kõrgus

#teeb ekraani ja paneb sellele pealkirja
canvas = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Ussimäng :)')

#laeb pildid
snake_img = pygame.image.load('ussipea.png')
apple_img = pygame.image.load('apple.png')
#tail_img = pygame.image.load('pad.png')
apple_img_rect = apple_img.get_rect()


clock = pygame.time.Clock()
start_time = time.time()

snake_block = 10
snake_speed = 15

#teeb pildid paraja suurusega
apple_img = pygame.transform.scale(apple_img, [20, 20])
snake_img = pygame.transform.scale(snake_img, [15, 15])

#lisab muusika
pygame.mixer.music.load('naljakas.mp3')
pygame.mixer.music.play(-1)

#alsgus ekraan
def start_game():
    canvas.fill(BLACK)
    start_font1 = large_font.render("Teretulemast ussimängu !! :D", True, heleroosa)
    start_font2 = medium_font.render("Mängi", True, erkroosa, tumeroosa)
    start_font3 = medium_font.render("Juhised", True, erkroosa, tumeroosa)
    start_font4 = medium_font.render("Välju", True, erkroosa, tumeroosa)

    start_font1_rect = start_font1.get_rect()
    start_font2_rect = start_font2.get_rect()
    start_font3_rect = start_font3.get_rect()
    start_font4_rect = start_font4.get_rect()

    start_font1_rect.center = (dis_width/2, dis_height/2 - 100)
    start_font2_rect.center = (dis_width/2 + 100, dis_height/2 + 50)
    start_font3_rect.center = (dis_width/2 + 100, dis_height / 2 + 100)
    start_font4_rect.center = (dis_width/2 + 100, dis_height/2 + 150)

    canvas.blit(start_font1, start_font1_rect)
    canvas.blit(start_font2, start_font2_rect)
    canvas.blit(start_font3, start_font3_rect)
    canvas.blit(start_font4, start_font4_rect)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    gameloop()
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x > start_font3_rect.left and x < start_font3_rect.right:
                    if y > start_font3_rect.top and y < start_font3_rect.bottom:
                        start_inst(start_font1, start_font1_rect)
                if x > start_font2_rect.left and x < start_font2_rect.right:
                    if y > start_font2_rect.top and y < start_font2_rect.bottom:
                        gameloop()
                if x > start_font4_rect.left and x < start_font4_rect.right:
                    if y > start_font4_rect.top and y < start_font4_rect.bottom:
                        pygame.quit()
                        sys.exit()

        pygame.display.update()




    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


def start_inst(start_font1, start_font1_rect):
    canvas.fill(BLACK)
    canvas.blit(start_font1, start_font1_rect)
    start_inst1 = small_font.render("--> Do not cross the edges, else you will be dead", True, heleroosa)
    start_inst2 = small_font.render("--> Keep eating the red apples", True, heleroosa)
    start_inst3 = small_font.render("--> Do not cross over yourself", True, heleroosa)
    start_inst4 = small_font.render("--> Keep playing......", True, heleroosa)
    start_inst5 = medium_font.render("<<BACK", True, erkroosa, tumeroosa)
    start_inst5_rect = start_inst5.get_rect()
    start_inst5_rect.center = (dis_width-100, dis_height - 100)

    canvas.blit(start_inst1, (dis_width/8, dis_height/2))
    canvas.blit(start_inst2, (dis_width/8, dis_height/2 + 30))
    canvas.blit(start_inst3, (dis_width/8, dis_height/2 + 60))
    canvas.blit(start_inst4, (dis_width/8, dis_height/2 + 90))
    canvas.blit(start_inst5, start_inst5_rect)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x > start_inst5_rect.left and x < start_inst5_rect.right:
                    if y > start_inst5_rect.top and y < start_inst5_rect.bottom:
                        start_game()
        pygame.display.update()


def gameover():
    canvas.fill(BLACK)

    font_gameover1 = large_font.render('MÄNG LÄBI !! D:', True, heleroosa)
    font_gameover2 = medium_font.render("Mägi uuesti", True, erkroosa, tumeroosa)
    font_gameover3 = medium_font.render("Välju", True, erkroosa, tumeroosa)

    font_gameover1_rect = font_gameover1.get_rect()
    font_gameover2_rect = font_gameover2.get_rect()
    font_gameover3_rect = font_gameover3.get_rect()


    font_gameover1_rect.center = (dis_width/2, dis_height/2 - 100)
    font_gameover2_rect.center = (dis_width / 2 + 150, dis_height / 2 + 20)
    font_gameover3_rect.center = (dis_width / 2 + 150, dis_height/ 2 + 70)


    canvas.blit(font_gameover1, font_gameover1_rect)
    canvas.blit(font_gameover2, font_gameover2_rect)
    canvas.blit(font_gameover3, font_gameover3_rect)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x > font_gameover2_rect.left and x < font_gameover2_rect.right:
                    if y > font_gameover2_rect.top and y < font_gameover2_rect.bottom:
                        gameloop()
                if x > font_gameover3_rect.left and x < font_gameover3_rect.right:
                    if y > font_gameover3_rect.top and y < font_gameover3_rect.bottom:
                        pygame.quit()
                        sys.exit()


        pygame.display.update()


def snake(snakelist, direction):

    if direction == 'right':
        head = pygame.transform.rotate(snake_img, 270)
        #tail = pygame.transform.rotate(tail_img, 270)
    if direction == 'left':
        head = pygame.transform.rotate(snake_img, 90)
       # tail = pygame.transform.rotate(tail_img, 90)
    if direction == 'up':
        head = pygame.transform.rotate(snake_img, 0)
        #tail = pygame.transform.rotate(tail_img, 0)
    if direction == 'down':
        head = pygame.transform.rotate(snake_img, 180)
        #tail = pygame.transform.rotate(tail_img, 180)

    canvas.blit(head, snakelist[-1])
    #canvas.blit(tail, snakelist[0])

    for XnY in snakelist[1:-1]:
        pygame.draw.rect(canvas, erkroosa, (XnY[0], XnY[1], SNAKE_WIDTH, SNAKE_WIDTH))


def game_paused():
    canvas.fill(BLACK)
    paused_font1 = large_font.render("Mäng pausil", True, erkroosa)
    paused_font_rect1 = paused_font1.get_rect()
    paused_font_rect1.center = (dis_width/2, dis_height/2)
    canvas.blit(paused_font1, paused_font_rect1)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pause_xy = event.pos
                if pause_xy[0] > (WINDOW_WIDTH - 50) and pause_xy[0] < WINDOW_WIDTH:
                    if pause_xy[1] > 0 and pause_xy[1] < 50:
                        return
        pygame.display.update()


def gameloop():

    while True:

        LEAD_X = 0
        LEAD_Y = 100
        direction = 'right'
        score = small_font.render("Skoor:0", True, heleroosa)
        APPLE_X = random.randrange(0, dis_width - 10, 10)
        APPLE_Y = random.randrange(TOP_WIDTH, dis_height- 10, 10)
        snakelist = []
        snakelength = 3
        pause_font = medium_font.render('II', True, erkroosa)


        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if direction == 'right':
                            pass
                        else:
                            direction = 'left'
                    if event.key == pygame.K_RIGHT:
                        if direction == 'left':
                            pass
                        else:
                            direction = 'right'
                    if event.key == pygame.K_UP:
                        if direction == 'down':
                            pass
                        else:
                            direction = 'up'
                    if event.key == pygame.K_DOWN:
                        if direction == 'up':
                            pass
                        else:
                            direction = 'down'
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pause_xy = event.pos
                    if pause_xy[0] > (dis_width - 50) and pause_xy[0] < dis_width:
                        if pause_xy[1] > 0 and pause_xy[1] < 50:
                            game_paused()
            if direction == 'up':
                LEAD_Y -= VELOCITY
                if LEAD_Y < TOP_WIDTH:
                    gameover()
            if direction == 'down':
                LEAD_Y += VELOCITY
                if LEAD_Y > dis_height - SNAKE_WIDTH:
                    gameover()
            if direction == 'right':
                LEAD_X += VELOCITY
                if LEAD_X > dis_width - SNAKE_WIDTH:
                    gameover()
            if direction == 'left':
                LEAD_X -= VELOCITY
                if LEAD_X < 0:
                    gameover()

            snakehead = []
            snakehead.append(LEAD_X)
            snakehead.append(LEAD_Y)
            snakelist.append(snakehead)

            snake_head_rect = pygame.Rect(LEAD_X, LEAD_Y, SNAKE_WIDTH, SNAKE_WIDTH)
            apple_rect = pygame.Rect(APPLE_X, APPLE_Y, APPLE_SIZE, APPLE_SIZE)


            if len(snakelist) > snakelength:
                del snakelist[0]
            for point in snakelist[:-1]:
                if point == snakehead:
                    gameover()

            canvas.fill(BLACK)

            snake(snakelist, direction)
            if snake_head_rect.colliderect(apple_rect):
                APPLE_X = random.randrange(0, WINDOW_WIDTH - 10, 10)
                APPLE_Y = random.randrange(TOP_WIDTH, WINDOW_HEIGHT - 10, 10)
                snakelength += 1
                score = small_font.render("Skoor:" + str(snakelength - 3), True, heleroosa)

            canvas.blit(score, (10, 5))
            pygame.draw.line(canvas, erkroosa, (0, TOP_WIDTH), (WINDOW_WIDTH, TOP_WIDTH))
            pygame.draw.line(canvas, heleroosa, (WINDOW_WIDTH - 60, 0), (WINDOW_WIDTH - 60, TOP_WIDTH))
            pygame.draw.rect(canvas, heleroosa, (WINDOW_WIDTH - 60, 0, 60, TOP_WIDTH))
            canvas.blit(pause_font, (WINDOW_WIDTH - 45, 10))
            canvas.blit(apple_img, (APPLE_X, APPLE_Y))
            pygame.display.update()

            clock.tick(FPS)


start_game()
gameloop()

'''
def Your_score(score):
    value = score_font.render("Sinu punktid: " + str(score), True, valge)
    canvas.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(canvas, tumeroosa, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    canvas.blit(mesg, [dis_width / 6, dis_height / 3])


def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
'''
'''
    while not game_over:

        while game_close == True:
            canvas.fill(heleroosa)
            message("Sa kaotasid! C-Mängi uuesti või Q-välju", valge)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        canvas.fill(heleroosa)
        pygame.draw.rect(canvas, erkroosa, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
'''
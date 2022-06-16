from constants import *
from snake import *
import main

def drawBackgroundGrid(screen):
    draws = GAME_SIZE * 2
    for i in range(draws):
        pygame.draw.line(screen, GRID_COLOR, [0, i * STEP[0]], [SCREEN_SIZE[0], i * STEP[0]], 1)
        pygame.draw.line(screen, GRID_COLOR, [i * STEP[1], 0], [i * STEP[1], SCREEN_SIZE[1]], 1)

def menu(screen):
    buttonColor = (0, 180, 0)
    selectedButtonColor = (100, 100, 100)
    direction = "NORTH"
    selected = 0
    smallfont = pygame.font.SysFont('Corbel', 35)
    smallsmallfont = pygame.font.SysFont('Corbel', 25)
    bigfont = pygame.font.SysFont('Corbel', 80)
    leave = smallfont.render('QUIT' , True , (255, 255, 255))
    ranking = smallfont.render('RANKING' , True , (255, 255, 255))
    play = smallfont.render('SINGLE PLAY' , True , (255, 255, 255))
    autoPlay = smallfont.render('AUTO PLAY' , True , (255, 255, 255))
    dualPlay = smallfont.render('DUAL PLAY' , True , (255, 255, 255))
    load = smallfont.render('LOAD' , True , (255, 255, 255))
    menu = bigfont.render('MENU' , True , (255, 255, 255))

    while 1:
        idx = 0
        screen.fill(BACKGROUND_COLOR)
        drawBackgroundGrid(screen)
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
            #if the mouse is clicked on the button the game is terminated
                if SCREEN_SIZE[0]/2 - 90 <= mouse[0] <= SCREEN_SIZE[0]/2 + 70 and SCREEN_SIZE[1]/2 - 250 <= mouse[1] <= SCREEN_SIZE[1]/2 - 210:
                    game(screen, 0)
                elif SCREEN_SIZE[0]/2 - 90 <= mouse[0] <= SCREEN_SIZE[0]/2 + 70 and SCREEN_SIZE[1]/2 - 170 <= mouse[1] <= SCREEN_SIZE[1]/2 - 130:
                    dualPlayerGame(screen)
                elif SCREEN_SIZE[0]/2 - 90 <= mouse[0] <= SCREEN_SIZE[0]/2 + 70 and SCREEN_SIZE[1]/2 - 90 <= mouse[1] <= SCREEN_SIZE[1]/2 - 50:
                    autoPlayGame(screen)
                elif SCREEN_SIZE[0]/2 - 90 <= mouse[0] <= SCREEN_SIZE[0]/2 + 70 and SCREEN_SIZE[1]/2 <= mouse[1] <= SCREEN_SIZE[1]/2 + 40:
                    game(screen, 1)
                elif SCREEN_SIZE[0]/2 - 90 <= mouse[0] <= SCREEN_SIZE[0]/2 + 70 and SCREEN_SIZE[1]/2 + 100 <= mouse[1] <= SCREEN_SIZE[1]/2 + 140:
                    rankingMenu(screen)
                elif SCREEN_SIZE[0]/2 - 90 <= mouse[0] <= SCREEN_SIZE[0]/2 + 70 and SCREEN_SIZE[1]/2 + 200 <= mouse[1] <= SCREEN_SIZE[1]/2 + 240:
                    sys.exit(0)
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit(0)

        #MENU
        screen.blit(menu, (SCREEN_SIZE[0]/2 - 80, SCREEN_SIZE[1]/2 - 350))

        #SINGLE PLAY
        if SCREEN_SIZE[0]/2 - 90 <= mouse[0] <= SCREEN_SIZE[0]/2 + 70 and SCREEN_SIZE[1]/2 - 250 <= mouse[1] <= SCREEN_SIZE[1]/2 - 210:
            pygame.draw.rect(screen, selectedButtonColor,[SCREEN_SIZE[0]/2 - 90,SCREEN_SIZE[1]/2 - 250, 180, 40])
        else:
            pygame.draw.rect(screen, buttonColor,[SCREEN_SIZE[0]/2 - 90,SCREEN_SIZE[1]/2 - 250, 180, 40])
        screen.blit(play, (SCREEN_SIZE[0]/2 - 80, SCREEN_SIZE[1]/2 - 240))

        # DUAL PLAY
        if SCREEN_SIZE[0]/2 - 90 <= mouse[0] <= SCREEN_SIZE[0]/2 + 70 and SCREEN_SIZE[1]/2 - 170 <= mouse[1] <= SCREEN_SIZE[1]/2 - 130:
            pygame.draw.rect(screen, selectedButtonColor,[SCREEN_SIZE[0]/2 - 90,SCREEN_SIZE[1]/2 - 170, 180, 40])
        else:
            pygame.draw.rect(screen, buttonColor,[SCREEN_SIZE[0]/2 - 90,SCREEN_SIZE[1]/2 - 170, 180, 40])
        screen.blit(dualPlay, (SCREEN_SIZE[0]/2 - 70, SCREEN_SIZE[1]/2 - 160))

        #AUTO PLAY
        if SCREEN_SIZE[0]/2 - 90 <= mouse[0] <= SCREEN_SIZE[0]/2 + 70 and SCREEN_SIZE[1]/2 - 90 <= mouse[1] <= SCREEN_SIZE[1]/2 - 50:
            pygame.draw.rect(screen, selectedButtonColor,[SCREEN_SIZE[0]/2 - 90,SCREEN_SIZE[1]/2 - 90, 180, 40])
        else:
            pygame.draw.rect(screen, buttonColor,[SCREEN_SIZE[0]/2 - 90,SCREEN_SIZE[1]/2 - 90, 180, 40])
        screen.blit(autoPlay, (SCREEN_SIZE[0]/2 - 70, SCREEN_SIZE[1]/2 - 80))

        #LOAD
        if SCREEN_SIZE[0]/2 - 90 <= mouse[0] <= SCREEN_SIZE[0]/2 + 70 and SCREEN_SIZE[1]/2 <= mouse[1] <= SCREEN_SIZE[1]/2 +40:
            pygame.draw.rect(screen, selectedButtonColor,[SCREEN_SIZE[0]/2 - 90,SCREEN_SIZE[1]/2, 180, 40])
        else:
            pygame.draw.rect(screen, buttonColor,[SCREEN_SIZE[0]/2 - 90,SCREEN_SIZE[1]/2, 180, 40])
        screen.blit(load, (SCREEN_SIZE[0]/2 - 30, SCREEN_SIZE[1]/2 + 10))

        #RANKING
        if SCREEN_SIZE[0]/2 - 90 <= mouse[0] <= SCREEN_SIZE[0]/2 + 70 and SCREEN_SIZE[1]/2 + 100 <= mouse[1] <= SCREEN_SIZE[1]/2 + 140:
            pygame.draw.rect(screen, selectedButtonColor,[SCREEN_SIZE[0]/2 - 90,SCREEN_SIZE[1]/2 +100, 180, 40])
        else:
            pygame.draw.rect(screen, buttonColor, [SCREEN_SIZE[0]/2 - 90, SCREEN_SIZE[1]/2 + 100, 180, 40])
        screen.blit(ranking, (SCREEN_SIZE[0]/2 - 55, SCREEN_SIZE[1]/2 + 110))

        #QUIT
        if SCREEN_SIZE[0]/2 - 90 <= mouse[0] <= SCREEN_SIZE[0]/2 + 70 and SCREEN_SIZE[1]/2 + 200 <= mouse[1] <= SCREEN_SIZE[1]/2 + 240:
            pygame.draw.rect(screen, selectedButtonColor,[SCREEN_SIZE[0]/2 - 90,SCREEN_SIZE[1]/2 + 200, 180, 40])
        else:
            pygame.draw.rect(screen, buttonColor, [SCREEN_SIZE[0]/2 - 90, SCREEN_SIZE[1]/2 + 200, 180, 40])
        screen.blit(leave, (SCREEN_SIZE[0]/2 - 30, SCREEN_SIZE[1]/2 + 210))

        #IN GAME MENU
        menuText = smallsmallfont.render("You can use escape button to access in game menu", True, (255, 255, 255))
        screen.blit(menuText, (180, 770))


        pygame.display.flip()

def pause(screen, player, playerTwo, apple, direction, score):
    buttonColor = (0, 180, 0)
    selectedButtonColor = (100, 100, 100)
    selected = 0
    smallfont = pygame.font.SysFont('Corbel', 35)
    smallsmallfont = pygame.font.SysFont('Corbel', 25)
    leave = smallfont.render('QUIT' , True , (255, 255, 255))
    resume = smallfont.render('RESUME' , True , (255, 255, 255))
    save = smallfont.render('SAVE' , True , (255, 255, 255))
    restart = smallfont.render('RESTART' , True , (255, 255, 255))
    menuButton = smallfont.render('MENU' , True , (255, 255, 255))
    bigfont = pygame.font.SysFont('Corbel', 80)
    pause = bigfont.render('PAUSE' , True , (255, 255, 255))
    snakeColor = (0,80,0)
    snakeColorTwo = (0,80,80)
    appleColor = (80,0,0)

    while 1:
        idx = 0
        screen.fill(BACKGROUND_COLOR)
        drawBackgroundGrid(screen)
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:

            #if the mouse is clicked on the
            # button the game is terminated
                if SCREEN_SIZE[0]/2 - 70 <= mouse[0] <= SCREEN_SIZE[0]/2 + 70 and SCREEN_SIZE[1]/2 - 150 <= mouse[1] <= SCREEN_SIZE[1]/2 - 110:
                    return False
                elif SCREEN_SIZE[0]/2 - 70 <= mouse[0] <= SCREEN_SIZE[0]/2 + 70 and SCREEN_SIZE[1]/2 - 50 <= mouse[1] <= SCREEN_SIZE[1]/2 - 10:
                    return True
                elif SCREEN_SIZE[0]/2 - 70 <= mouse[0] <= SCREEN_SIZE[0]/2 + 70 and SCREEN_SIZE[1]/2 + 50 <= mouse[1] <= SCREEN_SIZE[1]/2 + 90:
                    sys.exit(0)
                elif SCREEN_SIZE[0]/2 - 70 <= mouse[0] <= SCREEN_SIZE[0]/2 + 70 and SCREEN_SIZE[1]/2 + 150 <= mouse[1] <= SCREEN_SIZE[1]/2 + 190:
                    menu(screen)
                elif SCREEN_SIZE[0]/2 - 70 <= mouse[0] <= SCREEN_SIZE[0]/2 + 70 and SCREEN_SIZE[1]/2+ 250 <= mouse[1] <= SCREEN_SIZE[1]/2 + 290 and score != -1:
                    main.saveFunc(player, apple, direction, score)
                    menu(screen)
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit(0)

        # DRAW APPLE
        pygame.draw.rect(screen, appleColor, pygame.Rect(apple.x, apple.y, STEP[0], STEP[1]))

        # DRAW SNAKE
        for i in player:
            pygame.draw.rect(screen, snakeColor, pygame.Rect(i.x, i.y, STEP[0], STEP[1]))
        for i in playerTwo:
            pygame.draw.rect(screen, snakeColorTwo, pygame.Rect(i.x, i.y, STEP[0], STEP[1]))

        #RESUME
        if SCREEN_SIZE[0]/2 - 70 <= mouse[0] <= SCREEN_SIZE[0]/2 + 70 and SCREEN_SIZE[1]/2 - 150 <= mouse[1] <= SCREEN_SIZE[1]/2 - 110:
            pygame.draw.rect(screen, selectedButtonColor,[SCREEN_SIZE[0]/2 - 70,SCREEN_SIZE[1]/2 - 150, 140, 40])
        else:
            pygame.draw.rect(screen, buttonColor,[SCREEN_SIZE[0]/2 - 70,SCREEN_SIZE[1]/2 - 150, 140, 40])
        screen.blit(resume, (SCREEN_SIZE[0]/2 -50, SCREEN_SIZE[1]/2 - 140))


        #RESTART
        if SCREEN_SIZE[0]/2 - 70 <= mouse[0] <= SCREEN_SIZE[0]/2 + 70 and SCREEN_SIZE[1]/2 - 50 <= mouse[1] <= SCREEN_SIZE[1]/2 - 10:
            pygame.draw.rect(screen, selectedButtonColor,[SCREEN_SIZE[0]/2 - 70,SCREEN_SIZE[1]/2 - 50, 140, 40])
        else:
            pygame.draw.rect(screen, buttonColor,[SCREEN_SIZE[0]/2 - 70,SCREEN_SIZE[1]/2 - 50, 140, 40])
        screen.blit(restart, (SCREEN_SIZE[0]/2 -55, SCREEN_SIZE[1]/2 - 40))

        #QUIT
        if SCREEN_SIZE[0]/2 - 70 <= mouse[0] <= SCREEN_SIZE[0]/2 + 70 and SCREEN_SIZE[1]/2 + 50 <= mouse[1] <= SCREEN_SIZE[1]/2 + 90:
            pygame.draw.rect(screen, selectedButtonColor,[SCREEN_SIZE[0]/2 - 70,SCREEN_SIZE[1]/2 + 50, 140, 40])
        else:
            pygame.draw.rect(screen, buttonColor, [SCREEN_SIZE[0]/2 - 70, SCREEN_SIZE[1]/2 + 50, 140, 40])
        screen.blit(leave, (SCREEN_SIZE[0]/2 - 30, SCREEN_SIZE[1]/2 + 60))

        #BACK TO MENU
        if SCREEN_SIZE[0]/2 - 70 <= mouse[0] <= SCREEN_SIZE[0]/2 + 70 and SCREEN_SIZE[1]/2 + 150 <= mouse[1] <= SCREEN_SIZE[1]/2 + 190:
            pygame.draw.rect(screen, selectedButtonColor,[SCREEN_SIZE[0]/2 - 70,SCREEN_SIZE[1]/2 + 150, 140, 40])
        else:
            pygame.draw.rect(screen, buttonColor, [SCREEN_SIZE[0]/2 - 70, SCREEN_SIZE[1]/2 + 150, 140, 40])
        screen.blit(menuButton, (SCREEN_SIZE[0]/2 - 30, SCREEN_SIZE[1]/2 + 160))

        #SAVE
        if score != -1:
            if SCREEN_SIZE[0]/2 - 70 <= mouse[0] <= SCREEN_SIZE[0]/2 + 70 and SCREEN_SIZE[1]/2+ 250 <= mouse[1] <= SCREEN_SIZE[1]/2 + 290:
                pygame.draw.rect(screen, selectedButtonColor,[SCREEN_SIZE[0]/2 - 70,SCREEN_SIZE[1]/2+ 250, 140, 40])
            else:
                pygame.draw.rect(screen, buttonColor,[SCREEN_SIZE[0]/2 - 70,SCREEN_SIZE[1]/2+ 250, 140, 40])
            screen.blit(save, (SCREEN_SIZE[0]/2 - 30, SCREEN_SIZE[1]/2 + 260))

        #IN GAME MENU
        menuText = smallsmallfont.render("You can use escape button to quit the game" , True , (255, 255, 255))
        screen.blit(menuText, (180, 770))

        #PAUSE
        screen.blit(pause, (SCREEN_SIZE[0]/2 - 90, SCREEN_SIZE[1]/2 - 250))

        pygame.display.flip()

def rankingMenu(screen):
    buttonColor = (0, 180, 0)
    selectedButtonColor = (100, 100, 100)
    selected = 0
    smallfont = pygame.font.SysFont('Corbel', 35)
    smallsmallfont = pygame.font.SysFont('Corbel', 25)
    back = smallfont.render('MENU' , True , (255, 255, 255))
    bigfont = pygame.font.SysFont('Corbel', 80)
    rankingText = bigfont.render('RANKING' , True , (255, 255, 255))
    rank = getRanking()

    rank.sort(key=lambda x: x.score, reverse=True)
    while 1:
        idx = 0
        screen.fill(BACKGROUND_COLOR)
        drawBackgroundGrid(screen)
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:

            #if the mouse is clicked on the
            # button the game is terminated
                if SCREEN_SIZE[0]/2 - 70 <= mouse[0] <= SCREEN_SIZE[0]/2 + 70 and SCREEN_SIZE[1]-120 <= mouse[1] <= SCREEN_SIZE[1]- 80:
                    return


        #MENU
        if SCREEN_SIZE[0]/2 - 70 <= mouse[0] <= SCREEN_SIZE[0]/2 + 70 and SCREEN_SIZE[1] - 120 <= mouse[1] <= SCREEN_SIZE[1] - 80:
            pygame.draw.rect(screen, selectedButtonColor,[SCREEN_SIZE[0]/2 - 70,SCREEN_SIZE[1] - 120, 140, 40])
        else:
            pygame.draw.rect(screen, buttonColor, [SCREEN_SIZE[0]/2 - 70, SCREEN_SIZE[1]- 120, 140, 40])
        screen.blit(back, (SCREEN_SIZE[0]/2 - 30, SCREEN_SIZE[1]-110))

        for i in rank[0:9]:
            nameText = smallfont.render(i.name, True , (255, 255, 255))
            scoreText = smallfont.render(str(i.score) , True , (255, 255, 255))
            screen.blit(nameText, (250, 200+ 50*rank.index(i)))
            screen.blit(scoreText, (SCREEN_SIZE[0] - 250, 200+ 50*rank.index(i)))

        #IN GAME MENU
        menuText = smallsmallfont.render("You can use escape button to access in game menu" , True , (255, 255, 255))
        screen.blit(menuText, (180, 770))

        screen.blit(rankingText, (SCREEN_SIZE[0]/2 - 130, 80))
        pygame.display.flip()

def getRanking():
    rank = []
    try:
        with open('save/ranking.txt', 'r') as f:
            buffer = f.read().split('\n')
            for i in buffer:
                tmp = Rank()
                buff2 = i.split(':')
                tmp.name = buff2[0]
                tmp.score = int(buff2[1])
                rank.append(tmp)
    except:
        print("file not found: save/ranking.txt")
    return rank
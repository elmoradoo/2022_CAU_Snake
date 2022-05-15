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
    leave = smallfont.render('QUIT' , True , (255, 255, 255))
    ranking = smallfont.render('RANKING' , True , (255, 255, 255))
    play = smallfont.render('PLAY' , True , (255, 255, 255))
    twoPlay = smallfont.render(' 2 PLAYERS' , True , (255, 255, 255))
    load = smallfont.render('LOAD' , True , (255, 255, 255))
    bigfont = pygame.font.SysFont('Corbel', 80)
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

            #if the mouse is clicked on the
            # button the game is terminated
                if SCREEN_SIZE[0]/2 - 70 <= mouse[0] <= SCREEN_SIZE[0]/2 + 70 and SCREEN_SIZE[1]/2 + 200 <= mouse[1] <= SCREEN_SIZE[1]/2 + 240:
                    sys.exit(0)
                elif SCREEN_SIZE[0]/2 - 70 <= mouse[0] <= SCREEN_SIZE[0]/2 + 70 and SCREEN_SIZE[1]/2 + 100 <= mouse[1] <= SCREEN_SIZE[1]/2 + 140:
                    rankingMenu(screen)
                elif SCREEN_SIZE[0]/2 - 70 <= mouse[0] <= SCREEN_SIZE[0]/2 + 70 and SCREEN_SIZE[1]/2 - 100 <= mouse[1] <= SCREEN_SIZE[1]/2 - 60:
                    game(screen)
                elif SCREEN_SIZE[0]/1.5 - 70 <= mouse[0] <= SCREEN_SIZE[0]/1.5 + 70 and SCREEN_SIZE[1]/2 - 100 <= mouse[1] <= SCREEN_SIZE[1]/2 - 60:
                    twoPlayerGame(screen)
                elif SCREEN_SIZE[0]/2 - 70 <= mouse[0] <= SCREEN_SIZE[0]/2 + 70 and SCREEN_SIZE[1]/2 <= mouse[1] <= SCREEN_SIZE[1]/2 + 40:
                    player, apple, direction, score = main.loadFunc()
                    game(screen, player, apple, direction, score)

        #QUIT
        if SCREEN_SIZE[0]/2 - 70 <= mouse[0] <= SCREEN_SIZE[0]/2 + 70 and SCREEN_SIZE[1]/2 + 200 <= mouse[1] <= SCREEN_SIZE[1]/2 + 240:
            pygame.draw.rect(screen, selectedButtonColor,[SCREEN_SIZE[0]/2 - 70,SCREEN_SIZE[1]/2 + 200, 140, 40])
        else:
            pygame.draw.rect(screen, buttonColor, [SCREEN_SIZE[0]/2 - 70, SCREEN_SIZE[1]/2 + 200, 140, 40])
        screen.blit(leave, (SCREEN_SIZE[0]/2 - 30, SCREEN_SIZE[1]/2 + 210))

        #RANKING
        if SCREEN_SIZE[0]/2 - 70 <= mouse[0] <= SCREEN_SIZE[0]/2 + 70 and SCREEN_SIZE[1]/2 + 100 <= mouse[1] <= SCREEN_SIZE[1]/2 + 140:
            pygame.draw.rect(screen, selectedButtonColor,[SCREEN_SIZE[0]/2 - 70,SCREEN_SIZE[1]/2 +100, 140, 40])
        else:
            pygame.draw.rect(screen, buttonColor, [SCREEN_SIZE[0]/2 - 70, SCREEN_SIZE[1]/2 + 100, 140, 40])
        screen.blit(ranking, (SCREEN_SIZE[0]/2 - 55, SCREEN_SIZE[1]/2 + 110))

        #PLAY
        if SCREEN_SIZE[0]/2 - 70 <= mouse[0] <= SCREEN_SIZE[0]/2 + 70 and SCREEN_SIZE[1]/2 - 100 <= mouse[1] <= SCREEN_SIZE[1]/2 - 60:
            pygame.draw.rect(screen, selectedButtonColor,[SCREEN_SIZE[0]/2 - 70,SCREEN_SIZE[1]/2 - 100, 140, 40])
        else:
            pygame.draw.rect(screen, buttonColor,[SCREEN_SIZE[0]/2 - 70,SCREEN_SIZE[1]/2 - 100, 140, 40])
        screen.blit(play, (SCREEN_SIZE[0]/2 - 30, SCREEN_SIZE[1]/2 - 90))

        # 2 PLAYERS
        if SCREEN_SIZE[0]/1.5<= mouse[0] <= SCREEN_SIZE[0]/1.5 + 140 and SCREEN_SIZE[1]/2 - 100 <= mouse[1] <= SCREEN_SIZE[1]/2 - 60:
            pygame.draw.rect(screen, selectedButtonColor,[SCREEN_SIZE[0]/1.5 ,SCREEN_SIZE[1]/2 - 100, 140, 40])
        else:
            pygame.draw.rect(screen, buttonColor,[SCREEN_SIZE[0]/1.5,SCREEN_SIZE[1]/2 - 100, 140, 40])
        screen.blit(twoPlay, (SCREEN_SIZE[0]/1.5, SCREEN_SIZE[1]/2 - 90))

        #LOAD
        if SCREEN_SIZE[0]/2 - 70 <= mouse[0] <= SCREEN_SIZE[0]/2 + 70 and SCREEN_SIZE[1]/2 <= mouse[1] <= SCREEN_SIZE[1]/2 +40:
            pygame.draw.rect(screen, selectedButtonColor,[SCREEN_SIZE[0]/2 - 70,SCREEN_SIZE[1]/2, 140, 40])
        else:
            pygame.draw.rect(screen, buttonColor,[SCREEN_SIZE[0]/2 - 70,SCREEN_SIZE[1]/2, 140, 40])
        screen.blit(load, (SCREEN_SIZE[0]/2 - 30, SCREEN_SIZE[1]/2 + 10))

        #IN GAME MENU
        menuText = smallsmallfont.render("You can use escape button to access in game menu" , True , (255, 255, 255))
        screen.blit(menuText, (180, 770))

        #MENU
        screen.blit(menu, (SCREEN_SIZE[0]/2 - 80, SCREEN_SIZE[1]/2 - 250))

        pygame.display.flip()

def pause(screen, player, apple, direction, score):
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
                if SCREEN_SIZE[0]/2 - 70 <= mouse[0] <= SCREEN_SIZE[0]/2 + 70 and SCREEN_SIZE[1]/2 + 150 <= mouse[1] <= SCREEN_SIZE[1]/2 + 190:
                    sys.exit(0)
                elif SCREEN_SIZE[0]/2 - 70 <= mouse[0] <= SCREEN_SIZE[0]/2 + 70 and SCREEN_SIZE[1]/2 + 250 <= mouse[1] <= SCREEN_SIZE[1]/2 + 290:
                    menu(screen)
                elif SCREEN_SIZE[0]/2 - 70 <= mouse[0] <= SCREEN_SIZE[0]/2 + 70 and SCREEN_SIZE[1]/2 - 150 <= mouse[1] <= SCREEN_SIZE[1]/2 - 110:
                    return player, apple, direction, score
                elif SCREEN_SIZE[0]/2 - 70 <= mouse[0] <= SCREEN_SIZE[0]/2 + 70 and SCREEN_SIZE[1]/2 - 50 <= mouse[1] <= SCREEN_SIZE[1]/2 - 10:
                    player = [Block() for i in range(INITIAL_NUMBER_OF_BLOCK)]
                    return player, randomApplePosition(player), "NORTH", 0
                elif SCREEN_SIZE[0]/2 - 70 <= mouse[0] <= SCREEN_SIZE[0]/2 + 70 and SCREEN_SIZE[1]/2+ 50 <= mouse[1] <= SCREEN_SIZE[1]/2 + 90:
                    main.saveFunc(player, apple, direction, score)
                    menu(screen)

        # DRAW APPLE
        pygame.draw.rect(screen, appleColor, pygame.Rect(apple.x, apple.y, STEP[0], STEP[1]))

        # DRAW SNAKE
        for i in player:
            pygame.draw.rect(screen, snakeColor, pygame.Rect(i.x, i.y, STEP[0], STEP[1]))

        #BACK TO MENU
        if SCREEN_SIZE[0]/2 - 70 <= mouse[0] <= SCREEN_SIZE[0]/2 + 70 and SCREEN_SIZE[1]/2 + 250 <= mouse[1] <= SCREEN_SIZE[1]/2 + 290:
            pygame.draw.rect(screen, selectedButtonColor,[SCREEN_SIZE[0]/2 - 70,SCREEN_SIZE[1]/2 + 250, 140, 40])
        else:
            pygame.draw.rect(screen, buttonColor, [SCREEN_SIZE[0]/2 - 70, SCREEN_SIZE[1]/2 + 250, 140, 40])
        screen.blit(menuButton, (SCREEN_SIZE[0]/2 - 30, SCREEN_SIZE[1]/2 + 260))

        #QUIT
        if SCREEN_SIZE[0]/2 - 70 <= mouse[0] <= SCREEN_SIZE[0]/2 + 70 and SCREEN_SIZE[1]/2 + 150 <= mouse[1] <= SCREEN_SIZE[1]/2 + 190:
            pygame.draw.rect(screen, selectedButtonColor,[SCREEN_SIZE[0]/2 - 70,SCREEN_SIZE[1]/2 + 150, 140, 40])
        else:
            pygame.draw.rect(screen, buttonColor, [SCREEN_SIZE[0]/2 - 70, SCREEN_SIZE[1]/2 + 150, 140, 40])
        screen.blit(leave, (SCREEN_SIZE[0]/2 - 30, SCREEN_SIZE[1]/2 + 160))

        #RESUME
        if SCREEN_SIZE[0]/2 - 70 <= mouse[0] <= SCREEN_SIZE[0]/2 + 70 and SCREEN_SIZE[1]/2 - 150 <= mouse[1] <= SCREEN_SIZE[1]/2 - 110:
            pygame.draw.rect(screen, selectedButtonColor,[SCREEN_SIZE[0]/2 - 70,SCREEN_SIZE[1]/2 - 150, 140, 40])
        else:
            pygame.draw.rect(screen, buttonColor,[SCREEN_SIZE[0]/2 - 70,SCREEN_SIZE[1]/2 - 150, 140, 40])
        screen.blit(resume, (SCREEN_SIZE[0]/2 -50, SCREEN_SIZE[1]/2 - 140))


        #SAVE
        if SCREEN_SIZE[0]/2 - 70 <= mouse[0] <= SCREEN_SIZE[0]/2 + 70 and SCREEN_SIZE[1]/2+ 50 <= mouse[1] <= SCREEN_SIZE[1]/2 + 90:
            pygame.draw.rect(screen, selectedButtonColor,[SCREEN_SIZE[0]/2 - 70,SCREEN_SIZE[1]/2+ 50, 140, 40])
        else:
            pygame.draw.rect(screen, buttonColor,[SCREEN_SIZE[0]/2 - 70,SCREEN_SIZE[1]/2+ 50, 140, 40])
        screen.blit(save, (SCREEN_SIZE[0]/2 - 30, SCREEN_SIZE[1]/2 + 60))

        #RESTART
        if SCREEN_SIZE[0]/2 - 70 <= mouse[0] <= SCREEN_SIZE[0]/2 + 70 and SCREEN_SIZE[1]/2 - 50 <= mouse[1] <= SCREEN_SIZE[1]/2 - 10:
            pygame.draw.rect(screen, selectedButtonColor,[SCREEN_SIZE[0]/2 - 70,SCREEN_SIZE[1]/2 - 50, 140, 40])
        else:
            pygame.draw.rect(screen, buttonColor,[SCREEN_SIZE[0]/2 - 70,SCREEN_SIZE[1]/2 - 50, 140, 40])
        screen.blit(restart, (SCREEN_SIZE[0]/2 -55, SCREEN_SIZE[1]/2 - 40))

        #IN GAME MENU
        menuText = smallsmallfont.render("You can use escape button to access in game menu" , True , (255, 255, 255))
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

        for i in rank[0:5]:
            nameText = bigfont.render(i.name, True , (255, 255, 255))
            scoreText = bigfont.render(str(i.score) , True , (255, 255, 255))
            screen.blit(nameText, (250, 200+ 100*rank.index(i)))
            screen.blit(scoreText, (SCREEN_SIZE[0] - 250, 200+ 100*rank.index(i)))

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
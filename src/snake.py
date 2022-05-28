from constants import *
import user_interface
import main

def drawBackgroundGrid(screen):
    draws = GAME_SIZE * 2
    for i in range(draws):
        pygame.draw.line(screen, GRID_COLOR, [0, i * STEP[0]], [SCREEN_SIZE[0], i * STEP[0]], 1)
        pygame.draw.line(screen, GRID_COLOR, [i * STEP[1], 0], [i * STEP[1], SCREEN_SIZE[1]], 1)

def setBlockPositions(snake, index, size, newx, newy):
    if (index == size):
        return
    xold = snake[index].x
    yold = snake[index].y
    snake[index].x = newx
    snake[index].y = newy
    setBlockPositions(snake, index + 1, size, xold, yold)

def game(screen, load):
    if (load == 1):
        player, apple, direction, score = main.loadFunc()
    else:
        player = [Block(60, 500) for i in range(INITIAL_NUMBER_OF_BLOCK)]
        apple = randomApplePosition(player)
        direction = "NORTH"
        score = 0
    snakeColor = (0,180,0)
    appleColor = (180,0,0)
    smallfont = pygame.font.SysFont('Corbel', 35)
    smallsmallfont = pygame.font.SysFont('Corbel', 25)
    while 1:
        screen.fill(BACKGROUND_COLOR)
        drawBackgroundGrid(screen)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    direction = "NORTH" if direction != "SOUTH" else direction
                if event.key == K_DOWN:
                    direction = "SOUTH" if direction != "NORTH" else direction
                if event.key == K_RIGHT:
                    direction = "EAST" if direction != "WEST" else direction
                if event.key == K_LEFT:
                    direction = "WEST" if direction != "EAST" else direction
                if event.key == K_ESCAPE:
                    player, apple, direction, score = user_interface.pause(screen, player, apple, direction, score)


        # DRAW APPLE
        pygame.draw.rect(screen, appleColor, pygame.Rect(apple.x, apple.y, STEP[0], STEP[1]))

        # DRAW SNAKE
        for i in player:
            pygame.draw.rect(screen, snakeColor, pygame.Rect(i.x, i.y, STEP[0], STEP[1]))

        # DRAW SCORE
        scoreText = smallfont.render("Score: " + str(score) , True , (255, 255, 255))
        screen.blit(scoreText, (10, 10))
        menuText = smallsmallfont.render("You can use escape button to access in game menu" , True , (255, 255, 255))
        screen.blit(menuText, (180, 770))

        pygame.display.flip()
        if (direction == "EAST"):
            setBlockPositions(player, 0, len(player), player[0].x + STEP[0], player[0].y)
        elif (direction == "NORTH"):
            setBlockPositions(player, 0, len(player), player[0].x, player[0].y - STEP[1])
        elif (direction == "SOUTH"):
            setBlockPositions(player, 0, len(player), player[0].x, player[0].y + STEP[1])
        elif (direction == "WEST"):
            setBlockPositions(player, 0, len(player), player[0].x - STEP[0], player[0].y)

        # Gestion apple
        if (player[0].x == apple.x and player[1].y == apple.y):
            score += 1
            pos = Block(60, 500)
            pos.x = player[len(player) - 1].x
            pos.y= player[len(player) - 1].y
            player.append(pos)
            apple = randomApplePosition(player)

        # Gestion game_over edge
        if (player[0].x < 0 or player[0].x > SCREEN_SIZE[0] or player[0].y < 0 or player[0].y > SCREEN_SIZE[1]):
            return game_over(screen, score, player, apple)

        # Gestion game_over snake
        for i in player[1:]:
            if (player[0].x == i.x and player[0].y == i.y):
                return game_over(screen, score, player, apple)
        pygame.time.wait(100)

def twoPlayerGame(screen):
    p1Alive = True
    p2Alive = True
    player = [Block(60, 500) for i in range(INITIAL_NUMBER_OF_BLOCK)]
    playerTwo = [Block(120, 500) for i in range(INITIAL_NUMBER_OF_BLOCK)]
    apple = randomApplePosition(player)
    snakeColorTwo = (0,180,180)
    direction = "NORTH"
    directionTwo = "SOUTH"
    score = 0
    snakeColor = (0,180,0)
    appleColor = (180,0,0)
    smallfont = pygame.font.SysFont('Corbel', 35)
    smallsmallfont = pygame.font.SysFont('Corbel', 25)
    while 1:
        screen.fill(BACKGROUND_COLOR)
        drawBackgroundGrid(screen)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    direction = "NORTH" if direction != "SOUTH" else direction
                if event.key == K_DOWN:
                    direction = "SOUTH" if direction != "NORTH" else direction
                if event.key == K_RIGHT:
                    direction = "EAST" if direction != "WEST" else direction
                if event.key == K_LEFT:
                    direction = "WEST" if direction != "EAST" else direction
                if event.key == K_ESCAPE:
                    player, apple, direction, score = user_interface.pause(screen, player, apple, direction, score)

                if event.key == K_w:
                    directionTwo = "NORTH" if directionTwo != "SOUTH" else directionTwo
                if event.key == K_s:
                    directionTwo = "SOUTH" if directionTwo != "NORTH" else directionTwo
                if event.key == K_d:
                    directionTwo = "EAST" if directionTwo != "WEST" else directionTwo
                if event.key == K_a:
                    directionTwo = "WEST" if directionTwo != "EAST" else directionTwo

        # DRAW APPLE
        pygame.draw.rect(screen, appleColor, pygame.Rect(apple.x, apple.y, STEP[0], STEP[1]))

        # DRAW SNAKE
        for i in player:
                pygame.draw.rect(screen, snakeColor, pygame.Rect(i.x, i.y, STEP[0], STEP[1]))
        for i in playerTwo:
                pygame.draw.rect(screen, snakeColorTwo, pygame.Rect(i.x, i.y, STEP[0], STEP[1]))

        # DRAW SCORE
        scoreText = smallfont.render("Score: " + str(score) , True , (255, 255, 255))
        screen.blit(scoreText, (10, 10))
        menuText = smallsmallfont.render("You can use escape button to access in game menu" , True , (255, 255, 255))
        screen.blit(menuText, (180, 770))

        pygame.display.flip()
        if (direction == "EAST"):
            setBlockPositions(player, 0, len(player), player[0].x + STEP[0], player[0].y)
        elif (direction == "NORTH"):
            setBlockPositions(player, 0, len(player), player[0].x, player[0].y - STEP[1])
        elif (direction == "SOUTH"):
            setBlockPositions(player, 0, len(player), player[0].x, player[0].y + STEP[1])
        elif (direction == "WEST"):
            setBlockPositions(player, 0, len(player), player[0].x - STEP[0], player[0].y)

        if (directionTwo == "EAST"):
            setBlockPositions(playerTwo, 0, len(playerTwo), playerTwo[0].x + STEP[0], playerTwo[0].y)
        elif (directionTwo == "NORTH"):
            setBlockPositions(playerTwo, 0, len(playerTwo), playerTwo[0].x, playerTwo[0].y - STEP[1])
        elif (directionTwo == "SOUTH"):
            setBlockPositions(playerTwo, 0, len(playerTwo), playerTwo[0].x, playerTwo[0].y + STEP[1])
        elif (directionTwo == "WEST"):
            setBlockPositions(playerTwo, 0, len(playerTwo), playerTwo[0].x - STEP[0], playerTwo[0].y)

        # Gestion apple
        if (player[0].x == apple.x and player[1].y == apple.y):
            score += 1
            pos = Block(60, 500)
            pos.x = player[len(player) - 1].x
            pos.y= player[len(player) - 1].y
            player.append(pos)
            apple = randomApplePosition(player)
        
        if (playerTwo[0].x == apple.x and playerTwo[1].y == apple.y):
            score += 1
            pos = Block(60, 500)
            pos.x = playerTwo[len(playerTwo) - 1].x
            pos.y= playerTwo[len(playerTwo) - 1].y
            playerTwo.append(pos)
            apple = randomApplePosition(playerTwo)

        # Gestion game_over edge
        if (player[0].x < 0 or player[0].x > SCREEN_SIZE[0] or player[0].y < 0 or player[0].y > SCREEN_SIZE[1]):
            p1Alive = False
        if (playerTwo[0].x < 0 or playerTwo[0].x > SCREEN_SIZE[0] or playerTwo[0].y < 0 or playerTwo[0].y > SCREEN_SIZE[1]):
            p2Alive = False

        # Gestion game_over snake
        for i in player[1:]:
            if (player[0].x == i.x and player[0].y == i.y):
                p1Alive = False
            if (playerTwo[0].x == i.x and playerTwo[0].y == i.y):
                p2Alive = False
        for i in playerTwo[1:]:
            if (playerTwo[0].x == i.x and playerTwo[0].y == i.y):
                p2Alive = False
            if (player[0].x == i.x and player[0].y == i.y):
                p1Alive = False
        if (p1Alive == False or p2Alive == False):
            return game_over(screen, score, player, apple)

        pygame.time.wait(100)

def game_over(screen, score, player, apple):
    buttonColor = (0, 180, 0)
    selectedButtonColor = (100, 100, 100)
    selected = 0
    smallfont = pygame.font.SysFont('Corbel', 35)
    smallsmallfont = pygame.font.SysFont('Corbel', 25)
    leave = smallfont.render('MENU' , True , (255, 255, 255))
    bigfont = pygame.font.SysFont('Corbel', 80)
    scoreText = bigfont.render('Score: ' + str(score) , True , (255, 255, 255))
    snakeColor = (0,80,0)
    appleColor = (80,0,0)

    updateRanking(score)
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
                if SCREEN_SIZE[0]/2 - 70 <= mouse[0] <= SCREEN_SIZE[0]/2 + 70 and SCREEN_SIZE[1]/2 <= mouse[1] <= SCREEN_SIZE[1]/2+40:
                    return


        # DRAW APPLE
        pygame.draw.rect(screen, appleColor, pygame.Rect(apple.x, apple.y, STEP[0], STEP[1]))

        # DRAW SNAKE
        for i in player:
            pygame.draw.rect(screen, snakeColor, pygame.Rect(i.x, i.y, STEP[0], STEP[1]))

        #QUIT
        if SCREEN_SIZE[0]/2 - 70 <= mouse[0] <= SCREEN_SIZE[0]/2 + 70 and SCREEN_SIZE[1]/2 <= mouse[1] <= SCREEN_SIZE[1]/2+40:
            pygame.draw.rect(screen, selectedButtonColor,[SCREEN_SIZE[0]/2 - 70,SCREEN_SIZE[1]/2, 140, 40])
        else:
            pygame.draw.rect(screen, buttonColor, [SCREEN_SIZE[0]/2 - 70, SCREEN_SIZE[1]/2, 140, 40])
        screen.blit(leave, (SCREEN_SIZE[0]/2 - 30, SCREEN_SIZE[1]/2 + 10))

        #SCORE
        screen.blit(scoreText, (SCREEN_SIZE[0]/2 - 110, SCREEN_SIZE[1]/2 - 100))

        #IN GAME MENU
        menuText = smallsmallfont.render("You can use escape button to access in game menu" , True , (255, 255, 255))
        screen.blit(menuText, (180, 770))

        pygame.display.flip()

def randomApplePosition(player):
    pos = Block(60, 500)
    test = False

    while test == False:
        test = True
        pos.x = random.randrange(0, GAME_SIZE, 2) * 10
        pos.y = random.randrange(0, GAME_SIZE, 2) * 10
        for i in player:
            if (i.x == pos.x and i.y == pos.y):
                test = False
    return pos

def updateRanking(score):
    if (len(sys.argv) >= 2):
        name = sys.argv[1]
    else:
        name = "???"

    try:
        with open('save/ranking.txt', 'a') as f:
            f.write("\n" + name + ":" + str(score))
    except:
        print("file not found: save/ranking.txt")

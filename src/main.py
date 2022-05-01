import pygame
import sys
from pygame.locals import *
from snake import Block, Rank
import random

# SYSTEM
SCREEN_SIZE = [800, 800]
GAME_SIZE = 40

# COLORS
BACKGROUND_COLOR = [0, 0, 0]
GRID_COLOR = [20, 30, 20]
INITIAL_NUMBER_OF_BLOCK = 3
STEP = [SCREEN_SIZE[0] / GAME_SIZE, SCREEN_SIZE[1] / GAME_SIZE]

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


def saveFunc(player, apple, direction, score):
    try:
        with open('save/apple.txt', 'w') as f:
            f.write(str(apple.x) + "," + str(apple.y))
    except:
        print("file not found: save/apple.txt")
    try:
        with open('save/player.txt', 'w') as f:
            f.write(direction + "\n")
            f.write(str(score) + "\n")
            for i in player:
                f.write(str(int(i.x)) + "," + str(int(i.y)))
                if player.index(i) != len(player) - 1:
                    f.write("\n")
    except:
        print("file not found: save/player.txt")


def loadFunc():
    apple = Block()
    player = []
    try:
        with open('save/apple.txt', 'r') as f:
            buffer = f.read().split(',')
            apple.x = int(buffer[0])
            apple.y = int(buffer[1])
    except:
        print("file not found: save/apple.txt")
    try:
        with open('save/player.txt', 'r') as f:
            buffer = f.read().split('\n')
            direction = buffer[0]
            score = int(buffer[1])
            for i in buffer[2:]:
                tmp = Block()
                buff2 = i.split(',')
                tmp.x = int(buff2[0])
                tmp.y = int(buff2[1])
                player.append(tmp)
    except:
        print("file not found: save/player.txt")
    return player, apple, direction, score

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
                    player = [Block() for i in range(INITIAL_NUMBER_OF_BLOCK)]
                    game(screen, player, randomApplePosition(player), "NORTH", 0)
                elif SCREEN_SIZE[0]/2 - 70 <= mouse[0] <= SCREEN_SIZE[0]/2 + 70 and SCREEN_SIZE[1]/2 <= mouse[1] <= SCREEN_SIZE[1]/2 + 40:
                    player, apple, direction, score = loadFunc()
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
                    saveFunc(player, apple, direction, score)
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


def randomApplePosition(player):
    pos = Block()
    test = False

    while test == False:
        test = True
        pos.x = random.randrange(0, GAME_SIZE, 2) * 10
        pos.y = random.randrange(0, GAME_SIZE, 2) * 10
        for i in player:
            if (i.x == pos.x and i.y == pos.y):
                test = False
    return pos


def game(screen, player, apple, direction, score):
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
                    player, apple, direction, score = pause(screen, player, apple, direction, score)


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
            pos = Block()
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


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption('CAU Snake')
    menu(screen)


if __name__ == '__main__': main()

import pygame
import sys
from pygame.locals import *
from snake import Block
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


def menu(screen):
    player = [Block() for i in range(INITIAL_NUMBER_OF_BLOCK)]
    buttonColor = (0, 180, 0)
    selectedButtonColor = (100, 100, 100)
    direction = "NORTH"
    selected = 0
    smallfont = pygame.font.SysFont('Corbel', 35)
    leave = smallfont.render('QUIT' , True , (255, 255, 255))
    play = smallfont.render('PLAY' , True , (255, 255, 255))
    load = smallfont.render('LOAD' , True , (255, 255, 255))

    while 1:
        idx = 0
        screen.fill(BACKGROUND_COLOR)
        #drawBackgroundGrid(screen)
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:

            #if the mouse is clicked on the
            # button the game is terminated
                if SCREEN_SIZE[0]/2 - 70 <= mouse[0] <= SCREEN_SIZE[0]/2+70 and SCREEN_SIZE[1]/2+100 <= mouse[1] <= SCREEN_SIZE[1]/2+140:
                    sys.exit(0)
                elif SCREEN_SIZE[0]/2 - 70 <= mouse[0] <= SCREEN_SIZE[0]/2+70 and SCREEN_SIZE[1]/2 - 100 <= mouse[1] <= SCREEN_SIZE[1]/2 - 60:
                    game(screen)

            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    direction = "NORTH"
                if event.key == K_DOWN:
                    direction = "SOUTH"
        #QUIT
        if SCREEN_SIZE[0]/2- 70 <= mouse[0] <= SCREEN_SIZE[0]/2+70 and SCREEN_SIZE[1]/2 + 100 <= mouse[1] <= SCREEN_SIZE[1]/2+140:
            pygame.draw.rect(screen, selectedButtonColor,[SCREEN_SIZE[0]/2 - 70,SCREEN_SIZE[1]/2 +100, 140, 40])
        else:
            pygame.draw.rect(screen, buttonColor, [SCREEN_SIZE[0]/2 - 70, SCREEN_SIZE[1]/2+100, 140, 40])
        screen.blit(leave, (SCREEN_SIZE[0]/2- 30, SCREEN_SIZE[1]/2+110))

        #PLAY
        if SCREEN_SIZE[0]/2- 70 <= mouse[0] <= SCREEN_SIZE[0]/2+70 and SCREEN_SIZE[1]/2 - 100 <= mouse[1] <= SCREEN_SIZE[1]/2 - 60:
            pygame.draw.rect(screen, selectedButtonColor,[SCREEN_SIZE[0]/2- 70,SCREEN_SIZE[1]/2 - 100,140,40])
        else:
            pygame.draw.rect(screen, buttonColor,[SCREEN_SIZE[0]/2- 70,SCREEN_SIZE[1]/2 - 100,140,40])
        screen.blit(play, (SCREEN_SIZE[0]/2-30, SCREEN_SIZE[1]/2 - 90))

        #LOAD
        if SCREEN_SIZE[0]/2- 70 <= mouse[0] <= SCREEN_SIZE[0]/2+70 and SCREEN_SIZE[1]/2 <= mouse[1] <= SCREEN_SIZE[1]/2 +40:
            pygame.draw.rect(screen, selectedButtonColor,[SCREEN_SIZE[0]/2- 70,SCREEN_SIZE[1]/2,140,40])
        else:
            pygame.draw.rect(screen, buttonColor,[SCREEN_SIZE[0]/2- 70,SCREEN_SIZE[1]/2,140,40])
        screen.blit(load, (SCREEN_SIZE[0]/2-30, SCREEN_SIZE[1]/2 + 10))

        pygame.display.flip()


def pause(screen):
    buttonColor = (0, 180, 0)
    selectedButtonColor = (100, 100, 100)
    selected = 0
    smallfont = pygame.font.SysFont('Corbel', 35)
    leave = smallfont.render('QUIT' , True , (255, 255, 255))
    resume = smallfont.render('RESUME' , True , (255, 255, 255))
    save = smallfont.render('SAVE' , True , (255, 255, 255))

    while 1:
        idx = 0
        screen.fill(BACKGROUND_COLOR)
        #drawBackgroundGrid(screen)
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:

            #if the mouse is clicked on the
            # button the game is terminated
                if SCREEN_SIZE[0]/2 - 70 <= mouse[0] <= SCREEN_SIZE[0]/2+70 and SCREEN_SIZE[1]/2+100 <= mouse[1] <= SCREEN_SIZE[1]/2+140:
                    sys.exit(0)
                elif SCREEN_SIZE[0]/2 - 70 <= mouse[0] <= SCREEN_SIZE[0]/2+70 and SCREEN_SIZE[1]/2 - 100 <= mouse[1] <= SCREEN_SIZE[1]/2 - 60:
                    return

        #QUIT
        if SCREEN_SIZE[0]/2- 70 <= mouse[0] <= SCREEN_SIZE[0]/2+70 and SCREEN_SIZE[1]/2 + 100 <= mouse[1] <= SCREEN_SIZE[1]/2+140:
            pygame.draw.rect(screen, selectedButtonColor,[SCREEN_SIZE[0]/2 - 70,SCREEN_SIZE[1]/2 +100, 140, 40])
        else:
            pygame.draw.rect(screen, buttonColor, [SCREEN_SIZE[0]/2 - 70, SCREEN_SIZE[1]/2+100, 140, 40])
        screen.blit(leave, (SCREEN_SIZE[0]/2- 30, SCREEN_SIZE[1]/2+110))

        #RESUME
        if SCREEN_SIZE[0]/2- 70 <= mouse[0] <= SCREEN_SIZE[0]/2+70 and SCREEN_SIZE[1]/2 - 100 <= mouse[1] <= SCREEN_SIZE[1]/2 - 60:
            pygame.draw.rect(screen, selectedButtonColor,[SCREEN_SIZE[0]/2- 70,SCREEN_SIZE[1]/2 - 100,140,40])
        else:
            pygame.draw.rect(screen, buttonColor,[SCREEN_SIZE[0]/2- 70,SCREEN_SIZE[1]/2 - 100,140,40])
        screen.blit(resume, (SCREEN_SIZE[0]/2-50, SCREEN_SIZE[1]/2 - 90))


        #SAVE
        if SCREEN_SIZE[0]/2- 70 <= mouse[0] <= SCREEN_SIZE[0]/2+70 and SCREEN_SIZE[1]/2 <= mouse[1] <= SCREEN_SIZE[1]/2 +40:
            pygame.draw.rect(screen, selectedButtonColor,[SCREEN_SIZE[0]/2- 70,SCREEN_SIZE[1]/2,140,40])
        else:
            pygame.draw.rect(screen, buttonColor,[SCREEN_SIZE[0]/2- 70,SCREEN_SIZE[1]/2,140,40])
        screen.blit(save, (SCREEN_SIZE[0]/2-30, SCREEN_SIZE[1]/2 + 10))

        pygame.display.flip()


def game_over(screen):
    buttonColor = (0, 180, 0)
    selectedButtonColor = (100, 100, 100)
    selected = 0
    smallfont = pygame.font.SysFont('Corbel', 35)
    leave = smallfont.render('QUIT' , True , (255, 255, 255))

    while 1:
        idx = 0
        screen.fill(BACKGROUND_COLOR)
        #drawBackgroundGrid(screen)
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:

            #if the mouse is clicked on the
            # button the game is terminated
                if SCREEN_SIZE[0]/2 - 70 <= mouse[0] <= SCREEN_SIZE[0]/2+70 and SCREEN_SIZE[1]/2+100 <= mouse[1] <= SCREEN_SIZE[1]/2+140:
                    sys.exit(0)

        #QUIT
        if SCREEN_SIZE[0]/2- 70 <= mouse[0] <= SCREEN_SIZE[0]/2+70 and SCREEN_SIZE[1]/2 + 100 <= mouse[1] <= SCREEN_SIZE[1]/2+140:
            pygame.draw.rect(screen, selectedButtonColor,[SCREEN_SIZE[0]/2 - 70,SCREEN_SIZE[1]/2 +100, 140, 40])
        else:
            pygame.draw.rect(screen, buttonColor, [SCREEN_SIZE[0]/2 - 70, SCREEN_SIZE[1]/2+100, 140, 40])
        screen.blit(leave, (SCREEN_SIZE[0]/2- 30, SCREEN_SIZE[1]/2+110))

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


def game(screen):
    player = [Block() for i in range(INITIAL_NUMBER_OF_BLOCK)]
    apple = randomApplePosition(player)
    snakeColor = (0,180,0)
    appleColor = (180,0,0)
    direction = "NORTH"
    score = 0
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
                    pause(screen)


        # DRAW APPLE
        pygame.draw.rect(screen, appleColor, pygame.Rect(apple.x, apple.y, STEP[0], STEP[1]))


        # DRAW SNAKE
        for i in player:
            pygame.draw.rect(screen, snakeColor, pygame.Rect(i.x, i.y, STEP[0], STEP[1]))

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
            game_over(screen)

        # Gestion game_over snake
        for i in player[1:]:
            if (player[0].x == i.x and player[0].y == i.y):
                game_over(screen)

        pygame.time.wait(100)


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption('CAU Snake')
    menu(screen)


if __name__ == '__main__': main()

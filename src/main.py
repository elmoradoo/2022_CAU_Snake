import pygame
from pygame.locals import *
from snake import Block

# SYSTEM
SCREEN_SIZE = [1920, 1080]
GAME_SIZE = 40

# COLORS
BACKGROUND_COLOR = [0, 0, 0]
GRID_COLOR = [255, 255, 255]
INITIAL_NUMBER_OF_BLOCK = 3
STEP = [SCREEN_SIZE[0] / GAME_SIZE, SCREEN_SIZE[1] / GAME_SIZE]

# NOT WORKING
def drawBackgroundGrid(screen):
    draws = GAME_SIZE * 2
    linesDraws = SCREEN_SIZE[0] / (GAME_SIZE * 2)
    columnsDraws = SCREEN_SIZE[1] / (GAME_SIZE * 2)
    for i in range(draws):
        pygame.draw.line(screen, GRID_COLOR, [0, i * linesDraws], [SCREEN_SIZE[0], i * linesDraws], 3)
        pygame.draw.line(screen, GRID_COLOR, [i * columnsDraws, 0], [i * columnsDraws, SCREEN_SIZE[1]], 3)

def setBlockPositions(snake, index, size, newx, newy):
    if (index == size):
        return
    xold = snake[index].x
    yold = snake[index].y
    snake[index].x = newx
    snake[index].y = newy
    setBlockPositions(snake, index + 1, size, xold, yold)


def game(screen):
    player = [Block() for i in range(INITIAL_NUMBER_OF_BLOCK)]
    snakeColor = (255,0,0)
    direction = "NORTH"
    while 1:
        screen.fill(BACKGROUND_COLOR)
        # drawBackgroundGrid(screen)
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    direction = "NORTH" if direction != "SOUTH" else direction
                if event.key == K_DOWN:
                    direction = "SOUTH" if direction != "NORTH" else direction
                if event.key == K_RIGHT:
                    direction = "EAST" if direction != "WEST" else direction
                if event.key == K_LEFT:
                    direction = "WEST" if direction != "EAST" else direction

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
        pygame.time.wait(100)


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption('CAU Snake')
    game(screen)


if __name__ == '__main__': main()
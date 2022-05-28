from constants import *
import user_interface

def drawBackgroundGrid(screen):
    draws = GAME_SIZE * 2
    for i in range(draws):
        pygame.draw.line(screen, GRID_COLOR, [0, i * STEP[0]], [SCREEN_SIZE[0], i * STEP[0]], 1)
        pygame.draw.line(screen, GRID_COLOR, [i * STEP[1], 0], [i * STEP[1], SCREEN_SIZE[1]], 1)

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
    apple = Block(60, 500)
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
                tmp = Block(60, 500)
                buff2 = i.split(',')
                tmp.x = int(buff2[0])
                tmp.y = int(buff2[1])
                player.append(tmp)
    except:
        print("file not found: save/player.txt")
    return player, apple, direction, score

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


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption('CAU Snake')
    user_interface.menu(screen)


if __name__ == '__main__': main()

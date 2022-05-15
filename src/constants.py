from operator import truediv
from dbus import Interface
import pygame
import sys
from pygame.locals import *
import random

# SYSTEM
SCREEN_SIZE = [800, 800]
GAME_SIZE = 40

# COLORS
BACKGROUND_COLOR = [0, 0, 0]
GRID_COLOR = [20, 30, 20]
INITIAL_NUMBER_OF_BLOCK = 3
STEP = [SCREEN_SIZE[0] / GAME_SIZE, SCREEN_SIZE[1] / GAME_SIZE]

# Classes
class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    x = 60
    y = 500

class Rank:
    name = ""
    score = 0

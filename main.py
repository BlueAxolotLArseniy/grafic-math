import pygame
from player import Player
from consts import ENABLE_ENEMIES, FPS, SCREEN_HEIGHT, SCREEN_WIDTH
from enemy import Enemy
from camera import Camera
from cave import Cave
from state import GameState
from game_operations import Game

pygame.init()

game_state = GameState()

sc = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = Player(400, 250, game_state)
enemy = Enemy(500, 250, player, 'WithOneBarrel', game_state)
enemy2 = Enemy(600, 250, player, 'WithTwoBarrels', game_state)
cave = Cave(400, 350, game_state)

clock = pygame.time.Clock()

camera = Camera()

game_operations = Game(sc, 
                 player, 
                 [enemy, enemy2], 
                 [cave], 
                 camera, 
                 game_state
                 )

while 1:
    for event in pygame.event.get():

        game_operations.events(event)

    game_operations.update(event)
    game_operations.draw()
    
    clock.tick(FPS)
    pygame.display.update()

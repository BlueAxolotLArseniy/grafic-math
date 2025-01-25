# Imports   Импорты
import pygame
from player import Player
from consts import ENABLE_ENEMIES, FPS, PAUSE_MODE, SETTINGS_BUTTON_CLICKED
from enemy import Enemy
from camera import Camera
from cave import Cave
from state import GameState
from ui_pause import UI_Pause

pygame.init()  # Init pygame   Инит pygame'a

game_state = GameState()

# Main variables   Главные переменные
sc = pygame.display.set_mode((800, 500))
player = Player(400, 250, game_state)
enemy = Enemy(500, 250, player, 'WithOneBarrel', game_state)
enemy2 = Enemy(600, 250, player, 'WithTwoBarrels', game_state)
cave = Cave(400, 350)

clock = pygame.time.Clock()  # Creating a Clock   Создание Clock

camera = Camera()

ui_pause = UI_Pause(sc, game_state)

while 1:  # Main cycle   Главный цикл

    for event in pygame.event.get():

        # Ending a programme on exit   Завершение программы при выходе
        if event.type == pygame.QUIT:
            exit()

        # All conditions with buttons pressed   Все условия с нажатыми кнопками:
        if event.type == pygame.KEYDOWN:

            # Ending a programme on exit   Завершение программы при выходе
            if event.key == pygame.K_F1:
                exit()

            if event.key == pygame.K_ESCAPE:
                if SETTINGS_BUTTON_CLICKED:
                    SETTINGS_BUTTON_CLICKED = False
                    game_state.settings_button_clicked = SETTINGS_BUTTON_CLICKED
                else:
                    PAUSE_MODE = not PAUSE_MODE
                    game_state.pause_mode = PAUSE_MODE

    sc.fill((0, 0, 0))  # Filling with black colour   Заливка черным цветом

    # Updates   Обновления

    ui_pause.update(event)

    if not game_state.pause_mode:
        camera.update()
        player.update(camera.kx, camera.ky)
        cave.update(camera.kx, camera.ky)

        if ENABLE_ENEMIES:
            enemy.update(camera.kx, camera.ky)
            enemy2.update(camera.kx, camera.ky)

        if game_state.debug_mode:
            # The number of ticks from enemy   Количество тиков во враге
            print('Debug --> Player time(ticks): ' + str(player.time))
            print('Debug --> Number of bullets: ' + str(len(player.bullets)))
            print('Debug --> FPS: ' + str(FPS))

    # Draws   Отрисовки

    ui_pause.draw()

    player.draw(sc)

    if ENABLE_ENEMIES:
        enemy.draw(sc)
        enemy2.draw(sc)

    cave.draw(sc)

    clock.tick(FPS)  # Updates ticks   Обновления тиков

    pygame.display.update()  # Update display   Обновление дисплея

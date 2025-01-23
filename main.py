# Imports   Импорты
import pygame
from player import Player
from consts import DEBUG_MODE, ENABLE_ENEMIES, FPS, PAUSE_MODE, SETTINGS_BUTTON_CLICKED
from enemy import Enemy
from camera import Camera
from cave import Cave
import button

pygame.init()  # Init pygame   Инит pygame'a

# Main variables   Главные переменные
sc = pygame.display.set_mode((800, 500))
player = Player(400, 250, DEBUG_MODE)
enemy = Enemy(500, 250, player, 'WithOneBarrel', DEBUG_MODE)
enemy2 = Enemy(600, 250, player, 'WithTwoBarrels', DEBUG_MODE)
cave = Cave(400, 350)

blur_sc = pygame.surface.Surface((800, 500))

exit_button = button.Button(0.8, (sc.get_width()/2, (sc.get_height()/3)*2), 'Выйти')
settings_button = button.Button(0.8, (sc.get_width()/2, (sc.get_height()/3)*1.5), 'Настройки')
continue_button = button.Button(0.8, (sc.get_width()/2, sc.get_height()/3), 'Продолжить')

debug_button = button.Button(0.8, (sc.get_width()/2, (sc.get_height()/3)*1.5), 'Режим Отладки')

clock = pygame.time.Clock()  # Creating a Clock   Создание Clock

camera = Camera()

while 1:  # Main cycle   Главный цикл
    mouse_pos = pygame.mouse.get_pos()

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
                else:
                    PAUSE_MODE = not PAUSE_MODE

        if PAUSE_MODE:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if DEBUG_MODE:
                    print(f"Mouse clicked at position: {mouse_pos}")
                    print(f"Exit button rect: {exit_button.image_rect}")
                    print(f"Continue button rect: {continue_button.image_rect}")
                    print(f"Settings button rect: {settings_button.image_rect}")
                    print(f"Debug button rect: {debug_button.image_rect}")
                if not SETTINGS_BUTTON_CLICKED:
                    if exit_button.image_rect.collidepoint(mouse_pos):
                        exit()
                    if continue_button.image_rect.collidepoint(mouse_pos):
                        PAUSE_MODE = False
                    if settings_button.image_rect.collidepoint(mouse_pos):
                        SETTINGS_BUTTON_CLICKED = True
                else:
                    if debug_button.image_rect.collidepoint(mouse_pos):
                        DEBUG_MODE = not DEBUG_MODE
                        
                        player.DEBUG_MODE = DEBUG_MODE
                        enemy.DEBUG_MODE = DEBUG_MODE
                        enemy2.DEBUG_MODE = DEBUG_MODE

    sc.fill((0, 0, 0))  # Filling with black colour   Заливка черным цветом
    blur_sc.fill((0, 0, 0))
    blur_sc.set_alpha(200)

    # Updates   Обновления

    if not PAUSE_MODE:
        camera.update()
        player.update(camera.kx, camera.ky)
        cave.update(camera.kx, camera.ky)

        if ENABLE_ENEMIES:
            enemy.update(camera.kx, camera.ky)
            enemy2.update(camera.kx, camera.ky)

        if DEBUG_MODE:
            # The number of ticks from enemy   Количество тиков во враге
            print('Debug --> Player time(ticks): ' + str(player.time))
            print('Debug --> Number of bullets: ' + str(len(player.bullets)))
            print('Debug --> FPS: ' + str(FPS))

    # Draws   Отрисовки
    player.draw(sc)

    if ENABLE_ENEMIES:
        enemy.draw(sc)
        enemy2.draw(sc)

    cave.draw(sc)

    if PAUSE_MODE:

        sc.blit(blur_sc, (0, 0))

        if SETTINGS_BUTTON_CLICKED:
            debug_button.update()
            debug_button.draw(sc)

        else:

            exit_button.update()
            continue_button.update()
            settings_button.update()

            exit_button.draw(sc)
            continue_button.draw(sc)
            settings_button.draw(sc)

    clock.tick(FPS)  # Updates ticks   Обновления тиков

    pygame.display.update()  # Update display   Обновление дисплея

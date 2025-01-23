# Imports   Импорты
import pygame
from player import Player
from consts import DEBUG_MODE, ENABLE_ENEMIES, FPS, PAUSE_MODE
from enemy import Enemy
from camera import Camera
from cave import Cave
import button

pygame.init()  # Init pygame   Инит pygame'a

# Main variables   Главные переменные
sc = pygame.display.set_mode((800, 500))
player = Player(400, 250)
enemy = Enemy(500, 250, player, 'WithOneBarrel')
enemy2 = Enemy(600, 250, player, 'WithTwoBarrels')
cave = Cave(400, 350)

blur_sc = pygame.surface.Surface((800, 500))

exit_button = button.Button(0.8, (sc.get_width()/2, sc.get_height()/3), 'Выйти')
continue_button = button.Button(0.8, (sc.get_width()/2, (sc.get_height()/3)*2), 'Продолжить')

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
                PAUSE_MODE = not PAUSE_MODE

        if PAUSE_MODE:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if DEBUG_MODE:
                    print(f"Mouse clicked at position: {mouse_pos}")
                    print(f"Exit button rect: {exit_button.image_rect}")
                    print(f"Continue button rect: {continue_button.image_rect}")
                if exit_button.image_rect.collidepoint(mouse_pos):
                    exit()
                if continue_button.image_rect.collidepoint(mouse_pos):
                    PAUSE_MODE = False

    sc.fill((0, 0, 0))  # Filling with black colour   Заливка черным цветом
    blur_sc.fill((0, 0, 0))
    blur_sc.set_alpha(200)

    # Updates   Обновления

    if PAUSE_MODE == False:
        camera.update()
        player.update(camera.kx, camera.ky)
        cave.update(camera.kx, camera.ky)

        if ENABLE_ENEMIES:
            enemy.update(camera.kx, camera.ky)
            enemy2.update(camera.kx, camera.ky)

    # Draws   Отрисовки
    player.draw(sc)

    if ENABLE_ENEMIES:
        enemy.draw(sc)
        enemy2.draw(sc)

    cave.draw(sc)

    if DEBUG_MODE:
        # The number of ticks from enemy   Количество тиков во враге
        print('Debug --> Player time(ticks): ' + str(player.time))
        print('Debug --> Number of bullets: ' + str(len(player.bullets)))
        print('Debug --> FPS: ' + str(FPS))

    if PAUSE_MODE:
        
        sc.blit(blur_sc, (0, 0))

        exit_button.update()
        continue_button.update()

        exit_button.draw(sc)
        continue_button.draw(sc)

    clock.tick(FPS)  # Updates ticks   Обновления тиков

    pygame.display.update()  # Update display   Обновление дисплея

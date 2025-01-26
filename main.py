import pygame
from player import Player
from consts import ENABLE_ENEMIES, FPS, SCREEN_HEIGHT, SCREEN_WIDTH
from enemy import Enemy
from camera import Camera
from cave import Cave
from state import GameState

pygame.init()

game_state = GameState()

# Main variables   Главные переменные
sc = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = Player(400, 250, game_state)
enemy = Enemy(500, 250, player, 'WithOneBarrel', game_state)
enemy2 = Enemy(600, 250, player, 'WithTwoBarrels', game_state)
cave = Cave(400, 350, game_state)

clock = pygame.time.Clock()  # Creating a Clock   Создание Clock

camera = Camera()


while 1:  # Main cycle   Главный цикл

    for event in pygame.event.get():

        # Ending a programme on exit   Завершение программы при выходе
        if event.type == pygame.QUIT:
            exit()

        # All conditions with buttons pressed   Все условия с нажатыми кнопками:
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                game_state.toggle_pause()

    sc.fill((0, 0, 0))  # Filling with black colour   Заливка черным цветом

    # Updates   Обновления

    if game_state.active_screen:
        game_state.active_screen.update(event)

    if not game_state.is_paused:
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

    player.draw(sc)

    if ENABLE_ENEMIES:
        enemy.draw(sc)
        enemy2.draw(sc)

    cave.draw(sc)

    if game_state.active_screen:
        game_state.active_screen.draw(sc)

    clock.tick(FPS)  # Updates ticks   Обновления тиков

    pygame.display.update()  # Update display   Обновление дисплея

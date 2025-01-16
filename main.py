# Imports   Импорты
import pygame
from player import Player
from consts import FPS
from enemy import Enemy
import map
from cave import Cave

pygame.init()  # Init pygame   Инит pygame'a

# Main variables   Главные переменные
sc = pygame.display.set_mode((800, 500))
player = Player(400, 250)
enemy = Enemy(500, 250, player, 'WithOneBarrel')
enemy2 = Enemy(600, 250, player, 'WithTwoBarrels')
cave = Cave(400, 350)

clock = pygame.time.Clock()  # Creating a Clock   Создание Clock

global_map = map.Map((enemy, enemy2, cave))

while 1:  # Main cycle   Главный цикл
    for event in pygame.event.get():

        # Ending a programme on exit   Завершение программы при выходе
        if event.type == pygame.QUIT:
            exit()

        # All conditions with buttons pressed   Все условия с нажатыми кнопками:
        if event.type == pygame.KEYDOWN:

            # Ending a programme on exit   Завершение программы при выходе
            if event.key == pygame.K_ESCAPE:
                exit()

    sc.fill((0, 0, 0))  # Filling with black colour   Заливка черным цветом

    global_map.update()
    
    # Updates   Обновленияa
    player.update()
    # enemy.update()
    # enemy2.update()

    # Draws   Отрисовки
    player.draw(sc)
    # enemy.draw(sc)
    # enemy2.draw(sc)
    cave.draw(sc)
    
    
    
    # -------------PRINT DEBUG--------------
    # The number of ticks from enemy   Количество тиков во враге
    print('Debug --> Enemy time(ticks): ' + str(enemy.time))
    print('Debug --> Number of bullets: ' + str(len(player.bullets)))
    # --------------------------------------
    clock.tick(FPS)  # Updates ticks   Обновления тиков

    pygame.display.update()  # Update display   Обновление дисплея

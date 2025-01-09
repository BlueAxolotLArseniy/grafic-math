# Imports   Импорты
import pygame
from player import Player
from consts import FPS
from enemy import Enemy

pygame.init()  # Init pygame   Инит pygame'a

# Main variables   Главные переменные
sc = pygame.display.set_mode((800, 500))
player = Player(400, 250)
enemy = Enemy.WithOneBarrels(500, 250, player)
enemy2 = Enemy.WithTwoBarrels(600, 250, player)

clock = pygame.time.Clock()  # Creating a Clock   Создание Clock

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

    # Updates   Обновленияa
    player.update()
    # enemy.update()
    enemy2.update()

    # Draws   Отрисовки
    player.draw(sc)
    # enemy.draw(sc)
    enemy2.draw(sc)

    #-------------PRINT DEBUG--------------
    # The number of ticks from enemy   Количество тиков во враге
    print('Debug --> Enemy time(ticks): ' + str(enemy.time))
    #--------------------------------------
    
    clock.tick(FPS)  # Updates ticks   Обновления тиков

    pygame.display.update()  # Update display   Обновление дисплея

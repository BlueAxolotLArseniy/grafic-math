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

btn_of_esc = button.Button(1, (300, 300), 'hello')

clock = pygame.time.Clock()  # Creating a Clock   Создание Clock

camera = Camera()

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
                if PAUSE_MODE == False: PAUSE_MODE = True
                else: PAUSE_MODE = False

    sc.fill((0, 0, 0))  # Filling with black colour   Заливка черным цветом

    # Updates   Обновления
    
    if PAUSE_MODE == False:
        btn_of_esc.update()
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
    btn_of_esc.draw(sc)
    if DEBUG_MODE:
        # -------------PRINT DEBUG--------------
        # The number of ticks from enemy   Количество тиков во враге
        print('Debug --> Player time(ticks): ' + str(player.time))
        print('Debug --> Number of bullets: ' + str(len(player.bullets)))
        print('Debug --> FPS: ' + str(FPS))
        # --------------------------------------
    
    clock.tick(FPS)  # Updates ticks   Обновления тиков

    pygame.display.update()  # Update display   Обновление дисплея

import pygame
import random
pygame.init()

sc = pygame.display.set_mode((800, 500))

class AirShipTheHeadPerson(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*2, self.image.get_height()*2))#a
        self.rect = self.image.get_rect(center=(x, y))
        self.original_image = self.image
        self.original_rect = self.rect.copy()

airshiplayer = AirShipTheHeadPerson(50, 100, 'ship.png')

move_trigger_delay = [0, 0, 0, 0]

clock = pygame.time.Clock()
FPS = 30

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            print('aa')
            if event.type == pygame.K_LEFT:
                airshiplayer.rect.centerx -= 20
                print('a')

    sc.fill((0, 0, 0))
    sc.blit(airshiplayer.image, airshiplayer.rect)
    pygame.display.update()
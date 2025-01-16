import pygame

class Cave(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.x, self.y = x, y

        self.x_speed = 0
        self.y_speed = 0

        self.image = pygame.image.load('images/cave.png').convert()
        self.image.set_colorkey((0, 0, 0))
        self.original_image = self.image
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*15, self.image.get_height()*15))
        
        self.rect = self.image.get_rect(center=(self.x, self.y))
        
    def update(self):
        pass

    def draw(self, sc: pygame.Surface):
        sc.blit(self.image, self.rect)

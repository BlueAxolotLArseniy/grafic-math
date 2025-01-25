import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, size, pos, text):
        self.image = pygame.image.load('images/settings_textures/button.png').convert()
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*size, self.image.get_height()*size))

        self.image_rect = self.image.get_rect(center=pos)

        self.surface_pos = self.image_rect.center

        self.font = pygame.font.Font('fonts/Monocraft.otf', int(24*size))
        self.sc_text = self.font.render(text, 0, (255, 255, 255))
        self.button_pos = self.sc_text.get_rect(center=(size*300//2, size*70//2))

        self.surface = pygame.Surface((300*size, 70*size))

    def update(self):
        ...

    def draw(self, sc):
        self.surface.fill((0, 0, 0))
        self.surface.blit(self.sc_text, self.button_pos)

        sc.blit(
            self.surface,
            (self.surface_pos[0]-self.image_rect.width / 2, self.surface_pos[1]-self.image_rect.height/2)
        )

        sc.blit(self.image, self.image_rect)

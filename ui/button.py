from typing import Tuple
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

        self.clicked = False  # Tracks if the button was clicked

    def is_clicked(self, event):
        # Check for mouse events
        # for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.collide(event.pos):  # Left mouse button and collision
                self.clicked = True  # Mark as clicked
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and self.clicked and self.collide(event.pos):
                self.clicked = False  # Reset click state
                return True  # Return True to indicate the button was clicked
        return False

    def draw(self, sc):
        self.surface.fill((0, 0, 0))
        self.surface.blit(self.sc_text, self.button_pos)

        sc.blit(
            self.surface,
            (self.surface_pos[0]-self.image_rect.width / 2, self.surface_pos[1]-self.image_rect.height/2)
        )

        sc.blit(self.image, self.image_rect)

    def collide(self, mouse_pos: Tuple[int, int]) -> bool:
        return self.image_rect.collidepoint(mouse_pos)

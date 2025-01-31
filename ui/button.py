from typing import Tuple
import pygame


class Button:
    def __init__(self, size: float, text: str, action):
        # Load and scale the button image
        self.image = pygame.image.load('images/settings_textures/button.png').convert()
        self.image = pygame.transform.scale(self.image, (int(300 * size), int(70 * size)))
        self.image.set_colorkey((0, 0, 0))  # Set transparency

        # Render the text
        font = pygame.font.Font('fonts/Monocraft.otf', round(24 * size))  # Use `round` for exact size
        self.text = font.render(text, False, (255, 255, 255))

        self.clicked = False  # Tracks if the button was clicked

        self.action = action

    def set_position(self, pos):
        self.rect = self.image.get_rect(center=pos)
        self.text_rect = self.text.get_rect(center=self.rect.center)  # Center text inside the button

    def update(self, event):
        if self.is_clicked(event):
            self.action()

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

    def draw(self, screen):
        screen.blit(self.image, self.rect)  # Draw button image
        screen.blit(self.text, self.text_rect)  # Draw text centered

    def collide(self, mouse_pos: Tuple[int, int]) -> bool:
        return self.rect.collidepoint(mouse_pos)

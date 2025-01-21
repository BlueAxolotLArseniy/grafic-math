import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, size, coords, text):
        self.image = pygame.image.load('images/settings_textures/button.png').convert()
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*size, self.image.get_height()*size))

        self.rect = self.image.get_rect(center=(size*300//2, size*70//2))
        
        self.coords = coords
        
        self.f = pygame.font.Font('fonts/Monocraft.otf', 24)
        self.sc_text = self.f.render(text, 0, (255, 255, 255))
        self.pos = self.sc_text.get_rect(center=(size*300//2, size*70//2))
        
        self.sf = pygame.Surface((300*size, 70*size))
    
    def update(self):
        self.sf.fill((0, 0, 0))
    
    def draw(self, sc):
        self.sf.blit(self.sc_text, self.pos)
        self.sf.blit(self.image, self.rect)
        
        sc.blit(self.sf, (self.coords[0], self.coords[1]))
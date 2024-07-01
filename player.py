import pygame
class Player:
    def __init__(self, x,y):
        self.image = pygame.image.load("assets/guy1.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
            
        
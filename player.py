import pygame
class Player:
    def __init__(self, x,y):
        self.all_images = []
        for i in range(1,5):
            img = pygame.image.load(f"assets/guy{i}.png")
            self.all_images.append(img)
            
        self.image = self.all_images[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.image_number = 0
        self.last_image_changed = 0
        self.direction = 1
        self.flip = False
        self.idle = True
    
    def animation(self):
        if not self.idle:
            if pygame.time.get_ticks() - self.last_image_changed > 300:
                self.last_image_changed = pygame.time.get_ticks()
                self.image_number += 1
                if self.image_number >= len(self.all_images):
                    self.image_number = 0
        self.image = self.all_images[self.image_number]
        
        
    def draw(self, screen):
        self.image = pygame.transform.flip(self.image, self.flip, False)
        screen.blit(self.image, self.rect)
        
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.idle = False
            self.flip = True
            self.direction = -1
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.idle = False
            self.flip = False
            self.rect.x += 5
            self.direction = 1
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.idle = True
            
        
        



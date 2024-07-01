import pygame
from player import Player
screen_width = 800
screen_height = 600
bg_image = pygame.image.load("assets/background.png")
bg_rect = bg_image.get_rect()

my_player = Player(100, 300)

bg_rect.topleft = (0,0)

screen = pygame.display.set_mode((screen_width, screen_height))
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(bg_image, bg_rect) 
    my_player.draw(screen)  
    my_player.move()     
    pygame.display.update()



    
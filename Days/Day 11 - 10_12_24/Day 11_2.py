# 100 Projects in 100 Days
# 
# 
# By Simon A. Betts	10/12/2024

"""
Day 11: Pygame


"""

# Example file showing a circle moving on screen
import pygame
from random import random

WIDTH:int = 1280
HEIGHT:int = 720

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0

# players

player_scale_x = 50;
player_scale_y = 50;

img_searcher = pygame.image.load('assets/images/searcher.png')
img_mispa = pygame.image.load('assets/images/mispa.png')

img_searcher_scaled = pygame.transform.scale(img_searcher, (player_scale_x,player_scale_y))
img_mispa_scaled = pygame.transform.scale(img_mispa, (player_scale_x,player_scale_y))

play_sear_x = 0
play_sear_y = 0
play_mispa_x = random()*WIDTH
play_mispa_y = random()*HEIGHT

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

def player_searcher():
	screen.blit(img_searcher_scaled, (play_sear_x, play_sear_y))
def player_mispa():
	screen.blit(img_mispa_scaled, (play_mispa_x, play_mispa_y))

# Game loop
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("lime green")

    player_searcher()
    player_mispa()
    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
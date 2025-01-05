import pygame
#import os
import random 

pygame.init()

WIDTH = HEIGHT = 750 
SCREEN_SIZE = (WIDTH,HEIGHT)

FPS = 60
Atom_HEIGHT = 15
Atom_WIDTH = 15
SCALE = (Atom_HEIGHT,Atom_WIDTH)

# |== Colours ==|
WHITE = (255,255,255)
BLACK = (0,0,0)

# |== Assets ==|
red_atom = pygame.image.load('assets/images/red_atom.png')
red_atom = pygame.transform.scale(red_atom,SCALE)
green_atom = pygame.image.load('assets/images/green_atom.png')
green_atom = pygame.transform.scale(green_atom,SCALE)
blue_atom = pygame.image.load('assets/images/blue_atom.png')
blue_atom = pygame.transform.scale(blue_atom,SCALE)
black_atom = pygame.image.load('assets/images/black_atom.png')
black_atom = pygame.transform.scale(black_atom,SCALE)

pygame.display.set_caption("Atom Simulation")
screen = pygame.display.set_mode(SCREEN_SIZE)

def draw_window(green_atom_rec) -> None:
	screen.fill(WHITE)
	screen.blit(green_atom,(green_atom_rec.x,green_atom_rec.y))
	pygame.display.update()


def main():

	green_atom_rec = pygame.Rect(((WIDTH/2)-(Atom_WIDTH/2)),((HEIGHT/2)-(Atom_HEIGHT/2)),Atom_HEIGHT,Atom_WIDTH)

	clock = pygame.time.Clock()
	running = True
	print(f'Start -->')

	while running:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		green_atom_rec.x += 1
		draw_window(green_atom_rec)

	print(f'End --X')


if __name__ == '__main__':
	main()
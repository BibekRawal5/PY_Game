import os
import pygame

FPS = 60
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game")

BORDER = pygame.Rect(WIDTH/2, 0, 10, HEIGHT)

BLACK = (0,0,0)
RED = (255,0,0)

def draw_window():
    WIN.fill(BLACK)
    # WIN.blit(WIN, dest)
    pygame.draw.rect(WIN, RED, BORDER)
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()
    
    pygame.QUIT



if __name__ == "__main__":
    main()
import time

import pygame

if __name__ == '__main__':
    clock = pygame.time.Clock()
    pygame.init()

    WIDTH = 200
    HEIGHT = 200

    pygame.display.set_caption("uwu")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    icon = pygame.image.load("logo.jpg").convert()
    pygame.display.set_icon(icon)

    bg = pygame.image.load("logo.jpg").convert()
    bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

    image = pygame.image.load("ubuntu.png").convert_alpha()
    image = pygame.transform.scale(image, (50, 50))

    rect = pygame.rect.Rect(0, 0, 50, 50)


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        rect = rect.move(1,1)

        screen.blit(bg, (0, 0))
        screen.b

        list(image, (100, 100))
        pygame.draw.rect(screen, (255, 150, 75), rect)

        pygame.display.update()

        clock.tick(30)


    pygame.quit()

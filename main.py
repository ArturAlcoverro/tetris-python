import time
import pygame
import sys
import integer

display = width, height = 451, 601
vCells, hCells = 20, 15
cellHeight, cellWidth = 600 / 20, 450 / 15

posX, posY = 0, 0

pygame.init()

screen = pygame.display.set_mode(display)

pygame.display.flip()
move_ticker = integer.Integer()

initTime = time.time()
str = "Hola"


def controls():
    global posX, posY

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        posX -= 1
        if posX < 0:
            posX = hCells - 1
    if keys[pygame.K_RIGHT]:
        posX += 1
        if posX > hCells - 1:
            posX = 0
    if keys[pygame.K_UP]:
        posY -= 1
        if posY < 0:
            posY = vCells - 1
    if keys[pygame.K_DOWN]:
        posY += 1
        if posY > vCells - 1:
            posY = 0


while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    white = (255, 255, 255)
    red = (255, 0, 0)

    controls()

    for y in range(vCells):
        for x in range(hCells):
            polygon = [
                (x * cellWidth, y * cellHeight),
                ((x + 1) * cellWidth, y * cellHeight),
                ((x + 1) * cellWidth, (y + 1) * cellHeight),
                (x * cellWidth, (y + 1) * cellHeight)
            ]
            pygame.draw.polygon(screen, white, polygon, 1)

            if x == posX and y == posY:
                pygame.draw.polygon(screen, red, polygon)

    pygame.display.flip()
    time.sleep(.01)

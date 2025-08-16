import pygame
import math

def checkInfinity(c, n_iterations):
    z=complex(0,0)
    for i in range(n_iterations):
        if z.real**2 + z.imag**2>4:
            return True
        z = z**2 + c
    return False
def drawGrid(screen, grid, color):
    i, j = 0, 0
    screen.fill((0,0,0))
    for row in grid:
        j=0
        for col in row:
            if col==True:
                pygame.draw.circle(screen, color, (j, i), 1)
            j+=1
        i+=1
    pygame.display.flip()

def main():
    pygame.init()
    DIMENSIONS = (1200, 800)
    COLOR = (0, 0, 255)
    NUMBER_OF_ITERATIONS = 100
    window = pygame.display.set_mode(DIMENSIONS)
    pygame.display.set_caption("Mandelbrot Set")

    grid = [[False for j in range(1200)] for i in range(800)]

    for i in range(1200):
        for j in range(800):
            c = complex((i-800)*0.0025,(j-400)*0.0025)
            if not checkInfinity(c, NUMBER_OF_ITERATIONS):
                grid[j][i] = True

    drawGrid(window, grid, COLOR)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
if __name__ == "__main__":
    main()

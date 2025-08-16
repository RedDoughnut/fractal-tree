import pygame
import math
from time import perf_counter

def getFromRatio(x1, x2, m, n):
    return (n*x1 + m*x2)/(m+n)
def distance(A, B):
    return math.sqrt((B[0]-A[0])**2 + (B[1]-A[1])**2)
def getThirdPoint(A, B):
    x1, y1 = A
    x2, y2 = B

    dx, dy = x2 - x1, y2 - y1

    angle = math.radians(60)
    cos60, sin60 = math.cos(angle), math.sin(angle)

    rx = dx * cos60 - dy * sin60
    ry = dx * sin60 + dy * cos60

    p3 = (x1 + rx, y1 + ry)

    return p3

def kochSnowflakeStep(sides):
    new_sides = []
    for side in sides:
        first_third = (getFromRatio(side[0][0], side[1][0], 1, 2), getFromRatio(side[0][1], side[1][1], 1, 2))
        second_third = (getFromRatio(side[0][0], side[1][0], 2, 1), getFromRatio(side[0][1], side[1][1], 2, 1))
        triangle_point = getThirdPoint(first_third, second_third)

        new_sides.append((side[0], first_third))
        new_sides.append((first_third, triangle_point))
        new_sides.append((triangle_point, second_third))
        new_sides.append((second_third, side[1]))
    return new_sides
def drawSnowflake(window, sides):
    window.fill((0,0,0))
    for side in sides:
        pygame.draw.line(window, (255,255,255), side[0], side[1])
    pygame.display.update()
def main():
    pygame.init()
    pygame.font.init()

    font = pygame.font.SysFont("Arial", 18)
    DIMENSIONS = (1280, 800)
    FPS = 120
    window = pygame.display.set_mode(DIMENSIONS)
    pygame.display.set_caption("Koch Snowflake")

    DELAY = 2.0
    CAP = 7
    sides = [
    ((440, 555.47), (840, 555.47)),
    ((840, 555.47), (640, 209.06)),
    ((640, 209.06), (440, 555.47)),
    ]
    drawSnowflake(window, sides)

    depth = 1
    clock = pygame.time.Clock()

    timeOfLastUpdate = perf_counter()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if perf_counter() - timeOfLastUpdate >= DELAY and depth<CAP:
            depth += 1
            sides = kochSnowflakeStep(sides)
            drawSnowflake(window, sides)
            text = font.render(f"Depth:{depth}", True, (255,255,255))
            window.blit(text, (5,5))
            pygame.display.update()
            timeOfLastUpdate = perf_counter()
        clock.tick(FPS)
    pygame.quit()
if __name__=="__main__":
    main()
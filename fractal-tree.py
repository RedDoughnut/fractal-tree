import pygame
import math

def rotate(center, point, alpha):
    x2, y2 = center
    x1, y1 = point
    x_new = (x1-x2) * math.cos(alpha) - (y1-y2) * math.sin(alpha)
    y_new = (x1-x2) * math.sin(alpha) + (y1-y2) * math.cos(alpha)

    return (x_new + x2, y_new + y2)
def draw_tree(screen, start, ratio, angle, length, width, color, depth, cur_angle):
    if depth==0:
        return
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return
    length *= ratio
    width = round(width*ratio-0.01)
    left_coordinate = (start[0] - math.sin(angle) * length, start[1] - math.cos(angle) * length)
    right_coordinate = (start[0] + math.sin(angle) * length, start[1] - math.cos(angle) * length)
    left_coordinate = rotate(start, left_coordinate, cur_angle)
    right_coordinate = rotate(start, right_coordinate, cur_angle)
    pygame.draw.line(screen, color, start, left_coordinate, width)
    pygame.draw.line(screen, color, start, right_coordinate, width)
    draw_tree(screen, left_coordinate, ratio, angle, length, width, color, depth-1, cur_angle-angle)
    draw_tree(screen, right_coordinate, ratio, angle, length, width, color, depth-1, cur_angle+angle)
def main():
    pygame.init()
    DIMENSIONS = (1280, 800)
    window = pygame.display.set_mode((DIMENSIONS))
    pygame.display.set_caption("Fractal Tree")

    RATIO = 0.75
    ANGLE = 2*math.pi/11
    WIDTH = 7
    START_LENGTH = 150
    COLOR = (255,255,255)
    DEPTH = 15
    start = (DIMENSIONS[0]/2, DIMENSIONS[1]-START_LENGTH)
    
    window.fill((0,0,0))
    pygame.draw.line(window, COLOR, (start[0], start[1]+START_LENGTH), (start[0], start[1]), WIDTH)
    
    draw_tree(window, start, RATIO, ANGLE/2, START_LENGTH, WIDTH, COLOR, DEPTH, 0)
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
if __name__ == "__main__":
    main()

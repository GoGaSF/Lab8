import pygame
import sys


def main():
    pygame.init()
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    GREEN = (124, 252, 0)
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    color = BLACK
    layer = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # DEFINE POS
    X, Y, cur_X, cur_Y = -1, -1, -1, -1
    SCREEN.fill(WHITE)
    layer.fill(WHITE)

    # DEFINE FLAGS
    isMouseDown = False
    drawRect = True
    drawCircle = False
    eraser = False
    running = True
    while running:
        pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            # KEYS TRACKING
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    color = BLACK

                if event.key == pygame.K_2:
                    color = RED

                if event.key == pygame.K_3:
                    color = BLUE

                if event.key == pygame.K_4:
                    color = YELLOW

                if event.key == pygame.K_5:
                    color = GREEN

                if event.key == pygame.K_q:
                    drawRect = True
                    drawCircle = False
                    eraser = False

                if event.key == pygame.K_w:
                    drawRect = False
                    drawCircle = True
                    eraser = False

                if event.key == pygame.K_e:
                    drawRect = False
                    drawCircle = False
                    eraser = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    isMouseDown = True
                    cur_X = event.pos[0]
                    cur_Y = event.pos[1]
                    X = event.pos[0]
                    Y = event.pos[1]

            # MOUSE TRACKING
            if event.type == pygame.MOUSEBUTTONUP:
                isMouseDown = False
                layer.blit(SCREEN, (0, 0))

            if event.type == pygame.MOUSEMOTION:
                if isMouseDown:
                    cur_X = event.pos[0]
                    cur_Y = event.pos[1]

        # DRAWING RECTANGULAR
        if isMouseDown and X != -1 and Y != -1 and cur_X != -1 and cur_Y != -1 and drawRect:
            SCREEN.blit(layer, (0, 0))
            r = calculateRect(X, Y, cur_X, cur_Y)
            pygame.draw.rect(SCREEN, color, pygame.Rect(r), 1)

        # DRAWING ELLIPSE
        if isMouseDown and X != -1 and Y != -1 and cur_X != -1 and cur_Y != -1 and drawCircle:
            SCREEN.blit(layer, (0, 0))
            r = calculateRect(X, Y, cur_X, cur_Y)
            pygame.draw.ellipse(SCREEN, color, r, 1)
        mouse = pygame.mouse.get_pos()

        # ERASER
        if eraser and pygame.mouse.get_pressed()[0]:
            pygame.draw.circle(SCREEN, WHITE, mouse, 25)

        pygame.display.flip()
        clock.tick(60)


# CALCULATE THE RECT
def calculateRect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))


main()
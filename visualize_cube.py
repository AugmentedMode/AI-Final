import pygame, sys
from pygame.locals import *
import time


def main(visual_state):
    pygame.init()
    clock = pygame.time.Clock()

    # Size of Display
    display_width = 800
    display_height = 400
    DISPLAY = pygame.display.set_mode((display_width,display_height),0,32)

    # Background color
    GRAY = (128,128,128)
    # Font color
    BLACK = (0,0,0)
    # Colors of cubes
    WHITE  = (255,255,255)
    BLUE   = (0,0,255)
    RED    = (255,0,0)
    GREEN  = (0,255,0)
    YELLOW = (255,255,0)
    ORANGE = (255,165,0)

    # Map to grab color
    get_color = {0: WHITE, 1: BLUE, 2: RED,
                3: GREEN, 4: YELLOW, 5: ORANGE}

    # Display text to screen
    myfont = pygame.font.SysFont('Arial', 44)
    myfontsmall = pygame.font.SysFont('Arial', 20)
    textsurface = myfont.render('Solved!', False, BLACK)

    # Window title
    pygame.display.set_caption("Q-Learning Rubik's Cube")

    # Dimensions of the cubes
    X = 50
    Y = 50

    # Count to increment through all of the states
    count = 0

    DONE = True

    while DONE:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()


        DISPLAY.fill(GRAY)

        # TOP
        pygame.draw.rect(DISPLAY,get_color[visual_state[count][0]],(200,50,X,Y))   #0
        pygame.draw.rect(DISPLAY,get_color[visual_state[count][1]],(250,50,X,Y))   #1
        pygame.draw.rect(DISPLAY,get_color[visual_state[count][2]],(200,100,X,Y))  #2
        pygame.draw.rect(DISPLAY,get_color[visual_state[count][3]],(250,100,X,Y))  #3

        # MIDDLE RIGHT
        pygame.draw.rect(DISPLAY,get_color[visual_state[count][4]],(300,150,X,Y))   #4
        pygame.draw.rect(DISPLAY,get_color[visual_state[count][5]],(350,150,X,Y))   #5
        pygame.draw.rect(DISPLAY,get_color[visual_state[count][6]],(300,200,X,Y))   #6
        pygame.draw.rect(DISPLAY,get_color[visual_state[count][7]],(350,200,X,Y))   #7

        # MIDDLE LEFT
        pygame.draw.rect(DISPLAY,get_color[visual_state[count][8]],(200,150,X,Y))   #8
        pygame.draw.rect(DISPLAY,get_color[visual_state[count][9]],(250,150,X,Y))   #9
        pygame.draw.rect(DISPLAY,get_color[visual_state[count][10]],(200,200,X,Y))  #10
        pygame.draw.rect(DISPLAY,get_color[visual_state[count][11]],(250,200,X,Y))  #11

        # BOTTOM
        pygame.draw.rect(DISPLAY,get_color[visual_state[count][12]],(200,250,X,Y))  #12
        pygame.draw.rect(DISPLAY,get_color[visual_state[count][13]],(250,250,X,Y))  #13
        pygame.draw.rect(DISPLAY,get_color[visual_state[count][14]],(200,300,X,Y))  #14
        pygame.draw.rect(DISPLAY,get_color[visual_state[count][15]],(250,300,X,Y))  #15

        # FAR LEFT
        pygame.draw.rect(DISPLAY,get_color[visual_state[count][16]],(100,150,X,Y))  #16
        pygame.draw.rect(DISPLAY,get_color[visual_state[count][17]],(150,150,X,Y))  #17
        pygame.draw.rect(DISPLAY,get_color[visual_state[count][18]],(100,200,X,Y))  #18
        pygame.draw.rect(DISPLAY,get_color[visual_state[count][19]],(150,200,X,Y))  #19

        # FAR RIGHT
        pygame.draw.rect(DISPLAY,get_color[visual_state[count][20]],(400,150,X,Y))  #20
        pygame.draw.rect(DISPLAY,get_color[visual_state[count][21]],(450,150,X,Y))  #21
        pygame.draw.rect(DISPLAY,get_color[visual_state[count][22]],(400,200,X,Y))  #22
        pygame.draw.rect(DISPLAY,get_color[visual_state[count][23]],(450,200,X,Y))  #23

        count += 1

        pygame.display.update()
        clock.tick(3)

        if count == len(visual_state):
            DISPLAY.blit(textsurface,(0,0))
            DONE = False
            pygame.display.update()

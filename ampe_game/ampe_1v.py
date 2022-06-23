import pygame

# Initialize the pygame
pygame.init()


playground = pygame.display.set_mode((450, 670))  # screen width and height

# Title and Icon
pygame.display.set_caption("Ampe")
icon = pygame.image.load('ampe.png')
pygame.display.set_icon(icon)

# Text and Score Initializing
score_value_p1 = 0
score_value_p2 = 0
font = pygame.font.SysFont('Helvetica', 12, True)  # [font type, size, bold, italic]
player1_text_x = 40
player1_text_y = 305
player2_text_x = 360
player2_text_y = 305

player1_score_text_x = 40
player1_score_text_y = 325
player2_score_text_x = 360
player2_score_text_y = 325


# Functions to display text
def show_label_1(x, y):
    p1_label = font.render("Player 1", True, (0, 0, 0))
    playground.blit(p1_label, (x, y))


def show_label_1_score(x, y):
    p1_score_label = font.render("Score: " + str(score_value_p1), True, (0, 0, 0))
    playground.blit(p1_score_label, (x, y))


def show_label_2(x, y):
    p2_label = font.render("Player 2", True, (0, 0, 0))
    playground.blit(p2_label, (x, y))


def show_label_2_score(x, y):
    p2_score_label = font.render("Score: " + str(score_value_p2), True, (0, 0, 0))
    playground.blit(p2_score_label, (x, y))


# Functions to create the playground, bounce and attack pads
def playground_colour():  # RGB - Screen color in hex code
    playground.fill((238, 238, 238))


def p1_playpad():
    colour1_bouncepad = (255, 186, 144)
    colour1_attackepad = (255, 101, 101)
    # pygame.RECT (x-y coordinates, rect dimensions, fill)
    pygame.draw.rect(playground, colour1_bouncepad, pygame.Rect(115, 30, 220, 80))
    pygame.draw.rect(playground, colour1_attackepad, pygame.Rect(135, 180, 80, 80))
    pygame.draw.rect(playground, colour1_attackepad, pygame.Rect(235, 180, 80, 80))


def p1_playpad_active_bounce():
    colour1_active_bouncepad = (148, 214, 255)
    pygame.draw.rect(playground, colour1_active_bouncepad, pygame.Rect(115, 30, 220, 80))


def p1_playpad_active_left():
    colour1_active_attackepad = (101, 104, 255)
    pygame.draw.rect(playground, colour1_active_attackepad, pygame.Rect(135, 180, 80, 80))


def p1_playpad_active_right():
    colour1_active_attackepad = (101, 104, 255)
    pygame.draw.rect(playground, colour1_active_attackepad, pygame.Rect(235, 180, 80, 80))


def p2_playpad():
    colour2_bouncepad = (88, 255, 125)
    colour2_attackepad = (48, 193, 52)
    pygame.draw.rect(playground, colour2_bouncepad, pygame.Rect(115, 560, 220, 80))
    pygame.draw.rect(playground, colour2_attackepad, pygame.Rect(135, 400, 80, 80))
    pygame.draw.rect(playground, colour2_attackepad, pygame.Rect(235, 400, 80, 80))


def p2_playpad_active_bounce():
    colour2_active_bouncepad = (255, 88, 218)
    pygame.draw.rect(playground, colour2_active_bouncepad, pygame.Rect(115, 560, 220, 80))


def p2_playpad_active_left():
    colour2_active_attackepad = (131, 33, 129)
    pygame.draw.rect(playground, colour2_active_attackepad, pygame.Rect(135, 400, 80, 80))


def p2_playpad_active_right():
    colour2_active_attackepad = (131, 33, 129)
    pygame.draw.rect(playground, colour2_active_attackepad, pygame.Rect(235, 400, 80, 80))


# Functions for play functionality
def p1_same():
    # Check for Player 1 Keystrokes
    if event.type == pygame.KEYDOWN:  # Checks if any key on keyboard is pressed down
        if event.key == pygame.K_LEFT:  # Controls for player 1 are left, down, right
            # print("Player 1 Left arrow is pressed")
            p1_playpad_active_left()
        if event.key == pygame.K_RIGHT:
            # print("Player 1 Right arrow is pressed")
            p1_playpad_active_right()
        if event.key == pygame.K_DOWN:
            # print("Player 1 Down arrow is pressed")
            p1_playpad_active_bounce()

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            # print("Player 1 Left arrow is released")
            pass
        if event.key == pygame.K_RIGHT:
            # print("Player 1 Right arrow is released")
            pass
        if event.key == pygame.K_DOWN:
            # print("Player 1 Down arrow is released")
            pass


def p2_different():
    # Check for Player 2 Keystrokes
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:  # Controls for player 2 are "a", "s", "d"
            # print("Player 2 Left arrow is pressed")
            p2_playpad_active_left()
        if event.key == pygame.K_d:
            # print("Player 2 Right arrow is pressed")
            p2_playpad_active_right()
        if event.key == pygame.K_s:
            # print("Player 2 Down arrow is pressed")
            p2_playpad_active_bounce()

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_a:
            # print("Player 2 Left arrow is released")
            pass
        if event.key == pygame.K_d:
            # print("Player 2 Right arrow is released")
            pass
        if event.key == pygame.K_s:
            # print("Player 2 Down arrow is released")
            pass


def score_play():
    # Functionality keys for scoring

    global score_value_p1, score_value_p2
    pressed = pygame.key.get_pressed()

    p1_point1 = pressed[pygame.K_LEFT] and pressed[pygame.K_a]
    p1_point2 = pressed[pygame.K_RIGHT] and pressed[pygame.K_d]  # was working, double the score
    # p1_point2 = pressed[pygame.K_RIGHT] and pressed[pygame.K_d] or pressed[pygame.K_LEFT] and pressed[pygame.K_a]

    p2_point1 = pressed[pygame.K_LEFT] and pressed[pygame.K_d]
    p2_point2 = pressed[pygame.K_RIGHT] and pressed[pygame.K_a]  # was working, double the score
    # p2_point2 = pressed[pygame.K_RIGHT] and pressed[pygame.K_a] or pressed[pygame.K_LEFT] and pressed[pygame.K_d]

    if event.type == pygame.KEYDOWN:
        pygame.time.delay(60)

        if event.key == p1_point1:
            score_value_p1 += 1
        if event.key == p1_point2:
            score_value_p1 += 1

        if event.key == p2_point1:
            score_value_p2 += 1
        if event.key == p2_point2:
            score_value_p2 += 1


# Game Loop

running = True
while running:
    pygame.time.delay(150)

    # For Playground colour
    playground_colour()

    # Player 1 play pad
    p1_playpad()

    # Player 2 play pad
    p2_playpad()

    # Player Labels
    show_label_1(player1_text_x, player1_text_y)
    show_label_2(player2_text_x, player2_text_y)

    # Score Labels
    show_label_1_score(player1_score_text_x, player1_score_text_y)
    show_label_2_score(player2_score_text_x, player2_score_text_y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        p1_same()
        p2_different()
        score_play()

    pygame.display.update()

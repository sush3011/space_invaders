import pygame

# Initialize the game
pygame.init()

# Create the Screen
screen = pygame.display.set_mode((800, 600))

# Title
pygame.display.set_caption("Space Invaders")

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0.1


def player(x, y):
    screen.blit(playerImg, (x, y))


# Main Game Loop
running = True

while running:

    # Colour of Screen(r, g, b)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Detect key presses
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -2
        if event.key == pygame.K_RIGHT:
            playerX_change = 2

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0

    #  Display the Player
    player(playerX, playerY)

    # Moving the player
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 750:
        playerX = 750

    pygame.display.update()

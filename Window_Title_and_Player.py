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


def player():
    screen.blit(playerImg, (playerX, playerY))


# Main Game Loop
running = True

while running:

    # Colour of Screen(r, g, b)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #  Display the Player
    player()

    pygame.display.update()

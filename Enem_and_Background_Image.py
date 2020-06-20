import pygame
import random

# Initialize the game
pygame.init()

# Create the Screen
screen = pygame.display.set_mode((800, 600))

# Setting the Background
background = pygame.image.load('background.jpg')

# Title
pygame.display.set_caption("Space Invaders")

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0.1

# Enemy
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 1.5
enemyY_change = 40


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# Main Game Loop
running = True

while running:

    # Colour of Screen(r, g, b)
    screen.fill((0, 0, 0))

    # background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Detect key presses
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -5
        if event.key == pygame.K_RIGHT:
            playerX_change = 5

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0

    #  Display the Player
    player(playerX, playerY)

    # Display the Enemy
    enemy(enemyX, enemyY)

    # Moving the player
    playerX += playerX_change

    # Border check for player
    if playerX <= 0:
        playerX = 0
    elif playerX >= 735:
        playerX = 735

    # Moving the enemy
    enemyX += enemyX_change

    # Border check for enemy
    if enemyX <= 0:
        enemyY += enemyY_change
        enemyX_change = 1.5
    elif enemyX >= 740:
        enemyY += enemyY_change
        enemyX_change = -1.5

    pygame.display.update()

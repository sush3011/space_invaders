import pygame
import random
import math

# Initialize the game
pygame.init()

# Create the Screen
screen = pygame.display.set_mode((800, 600))

# Setting the Background
background = pygame.image.load('background.jpg')

# Title
pygame.display.set_caption("Space Invaders")

# Score
score = 0

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

# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
# Ready - We can't see the bullet on the screen
# Fire - The bullet is currently moving
bullet_state = "ready"


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 33, y + 10))


def is_collision():
    global enemyX
    global enemyY
    global bulletX
    global bulletY

    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY + bulletY, 2)))
    if distance < 150:
        return True
    else:
        return False


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
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

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

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Collision check
    collision = is_collision()

    if collision:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        print(score)
        enemyX = random.randint(0, 800)
        enemyY = random.randint(50, 150)

    pygame.display.update()

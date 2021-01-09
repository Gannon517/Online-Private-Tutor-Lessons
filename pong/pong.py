import pygame
import sys
import random

def ballRestart():
    global ballSpeedX
    global ballSpeedY
    ball.center = (screenWidth/2, screenHeight/2)
    ballSpeedX *= random.choice((1,-1))
    ballSpeedY *= random.choice((1,-1))

pygame.init()
clock = pygame.time.Clock()

screenWidth = 960
screenHeight = 720
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Pong')

ball = pygame.Rect(screenWidth/2 - 15, screenHeight/2 - 15, 30,30)
player = pygame.Rect(screenWidth -20, screenHeight/2 - 70, 10, 140)
opponent = pygame.Rect(10, screenHeight/2 - 70, 10, 140)

black = (0,0,0)
lightGrey = (200,200,200)

ballSpeedX = 7
ballSpeedY = 7
playerSpeed = 0
opponentSpeed = 7

#scores
playerScore = 0
opponentScore = 0
gameFont = pygame.font.Font("freesansbold.ttf", 32)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                playerSpeed += 7
            if event.key == pygame.K_UP:
                playerSpeed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                playerSpeed -= 7
            if event.key == pygame.K_UP:
                playerSpeed += 7

    #ball animation
    ball.x += ballSpeedX
    ball.y += ballSpeedY
    if ball.top <= 0 or ball.bottom >= screenHeight:
        ballSpeedY *= -1
    if ball.left <= 0:
        playerScore += 1
        ballRestart()
    if ball.right >= screenWidth:
        opponentScore += 1
        ballRestart()
    if ball.colliderect(player) or ball.colliderect(opponent):
        ballSpeedX *= -1

    #player animation
    player.y += playerSpeed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screenHeight:
        player.bottom = screenHeight

    #opponent animation
    if opponent.top < ball.y:
        opponent.top += opponentSpeed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponentSpeed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screenHeight:
        opponent.bottom = screenHeight

    #visuals
    screen.fill(black)
    pygame.draw.rect(screen, lightGrey, player)
    pygame.draw.rect(screen, lightGrey, opponent)
    pygame.draw.ellipse(screen, lightGrey, ball)
    pygame.draw.aaline(screen,lightGrey, (screenWidth/2,0), (screenWidth/2,screenHeight))

    #texts
    playerText = gameFont.render(f"{playerScore}", False, lightGrey)
    screen.blit(playerText, (495, 360))
    opponentText = gameFont.render(f"{opponentScore}", False, lightGrey)
    screen.blit(opponentText, (450, 360))
    
    #updates window
    pygame.display.flip()
    clock.tick(60)
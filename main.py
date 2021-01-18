import pygame
from brickbreaker.constants import WIDTH, HEIGHT, bricks, CLOCK, FPS, BLACK, WHITE, HEARTFILE, font
from brickbreaker.paddle import Paddle
from brickbreaker.ball import Ball
from brickbreaker.brick import Brick
pygame.init()


win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brick Breaker PingPong Blast")


def main():

    run = True
    # playerPaddle = Paddle(0, HEIGHT - 30, )
    # ball = Ball(WIDTH // 2, HEIGHT // 2, 5, 15)
    brickBlocks = []
    score = 10
    lives = 3

    def reset():
        global playerPaddle, ball
        playerPaddle = Paddle(0, HEIGHT - 30, )
        ball = Ball(WIDTH // 2, HEIGHT // 2, 0, 15)

    reset()
    col = 0
    for rowZ in bricks:
        row = 0
        for brick in rowZ:
            if brick == 1:
                brickBlocks.append(Brick(row * 100, col*30, ))
                # print(row*100, col*30)
            row += 1
        col += 1

    while run:
        scoreView = font.render(f'Score: {score}', 1, WHITE)
        CLOCK.tick(FPS)
        win.fill(BLACK)
        playerPaddle.draw(win)
        playerPaddle.move()
        win.blit(scoreView, (0, HEIGHT - scoreView.get_height()))

        ball.move(playerPaddle, brickBlocks)

        for brick in brickBlocks:
            brick.draw(win)
        ball.draw(win)
        if ball.isOff():
            reset()
            lives -= 1

        for brick in brickBlocks:
            if ball.rect.colliderect(brick.rect):
                brick.health -= 1
                if brick.health == 0:

                    brickBlocks.remove(brick)
                ball.vy *= -1
                score += 1

        for life in range(1, lives+1):
            win.blit(HEARTFILE, (WIDTH - 40 * life, HEIGHT - 40))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                ball.vy = 5
                ball.vx = 5

        if lives == 0:
            youLost(score)

            # youLost(score)
        pygame.display.update()


def youLost(score):
    run = True
    displayScore = 0
    while run:
        displayScoreText = font.render(
            f'Your Total Score: {displayScore}', 1, WHITE)
        CLOCK.tick(60)
        win.fill(BLACK)
        win.blit(displayScoreText, (0, 0))

        if displayScore != score:
            displayScore += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


main()
pygame.quit()

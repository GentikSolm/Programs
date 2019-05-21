import sys, pygame, time

pygame.init()

size = width, height = 720, 360
speed = [1, 2]
black = 0, 0, 0
color = 200,200,200
screen = pygame.display.set_mode(size, flags=pygame.NOFRAME)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()
exit = pygame.draw.rect(screen, color, [680, 0, 40, 30])
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            if exit.collidepoint(pygame.mouse.get_pos()):
                sys.exit()
            # loc = pygame.mouse.get_pos()
            # if loc[0] > 680 and loc[1] < 30:
            #     sys.exit()
    ballrect = ballrect.move(speed)

    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    screen.fill(black)
    screen.blit(ball, ballrect)
    exit = pygame.draw.rect(screen, color, [680, 0, 40, 30])
    pygame.display.flip()
    time.sleep(.005)

import sys, pygame, math
pygame.init()

size = width, height = 1000, 1000

a = 9.8
u = 0
t = 0
v = u + a*t

speed = [1, 0]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(speed)
            print(a,u,t,v)
    speed[1] = (float(u) + float(a/1000)*float(t))
    ballrect = ballrect.move([round(speed[0]),round(speed[1])])
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = (speed[0]*0.80)
        speed[0] = -speed[0]
        if speed[0] < 1 and speed[0] > -1:
            print("oof")
            if speed[0] > 0:
                print("yeet2")
                ballrect = ballrect.move([1,0])
            elif speed[0] < 0:
                print("yeet3")
                ballrect = ballrect.move([-1,0])
        else:
            ballrect = ballrect.move(speed)
    if ballrect.top < 0 or ballrect.bottom > height:
        u = float(-speed[1])*0.9
        speed[1] = u
        ballrect = ballrect.move(speed)
        t = 0
        print("yeet")
    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
    t += 1

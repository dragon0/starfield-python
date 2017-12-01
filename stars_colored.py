import pygame
import atexit
import random

def make_point():
    x = random.randint(-50, 50)
    y = random.randint(-50, 50)
    z = 100
    return x, y, z

def make_point_randz():
    x = random.randint(-50, 50)
    y = random.randint(-50, 50)
    z = random.randint(1, 100)
    c = make_color()
    return x, y, z, c

def make_color():
    r = random.randrange(255)
    g = random.randrange(255)
    b = random.randrange(255)
    return r, g, b

pygame.init()
atexit.register(pygame.quit)

size = width, height = 500,500
black = 0, 0, 0
white = 0xff, 0xff, 0xff

centerx = width/2
centery = height/2

f = 90

screen = pygame.display.set_mode(size)

points = [make_point_randz() for _ in xrange(1000)]

clock = pygame.time.Clock()
running = True
while running:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)

    count = 0
    for i in xrange(len(points)):
        x, y, z, c = points[i]
        z -= 1
        if z > 0:
            xp = x*f / z
            yp = y*f / z

            xp += centerx
            yp += centery

            s = f / z

    #        count += 1
    #        print 'p', xp, yp,
    #        if count % 8 == 0:
    #            print

            #pygame.draw.rect(screen, white, (xp, yp, s, s))
            pygame.draw.circle(screen, c, (xp, yp), s)
        else:
            x, y, z = make_point()
        points[i] = (x, y, z, c)

    pygame.display.flip()


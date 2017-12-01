import pygame
import atexit

pygame.init()
atexit.register(pygame.quit)

size = width, height = 500,500
black = 0, 0, 0
white = 0xff, 0xff, 0xff

centerx = width/2
centery = height/2

f = 90

screen = pygame.display.set_mode(size)

points = []
for x in xrange(-45, 55, 10):
    for y in xrange(-45, 55, 10):
        for z in xrange(-45, 55, 10):
            points.append((x, y, z))


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
        x, y, z = points[i]
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
            pygame.draw.circle(screen, white, (xp, yp), s)
        else:
            z += 100
        points[i] = (x, y, z)

    pygame.display.flip()


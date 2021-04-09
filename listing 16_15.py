import pygame, sys
pygame.init()
screen = pygame.display.set_mode([1980,1260])
screen.fill([255,255,255])
my_ball = pygame.image.load('peacock_cichlid.png')
x = 50
y = 50
x_speed = 1
y_speed = 1
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.delay(1)
    pygame.draw.rect(screen, [255,255,255], [x, y, 1000, 586], 0)
    x = x + x_speed
    y = y + y_speed
    if x > screen.get_width() - 1000 or x < 0:
        x_speed = - x_speed
    if y > screen.get_height() - 586 or y < 0:
        y_speed = - y_speed
    screen.blit(my_ball, [x,y])
    pygame.display.flip()
pygame.quit()

import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

x, y = 400, 300

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 5
    if keys[pygame.K_RIGHT]:
        x += 5
    if keys[pygame.K_UP]:
        y -= 5
    if keys[pygame.K_DOWN]:
        y += 5

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 200, 0), (x, y), 30)
    pygame.display.flip()
    clock.tick(60)

    if y < 30:
        y = 30
    if y > 570:
        y = 570
    if x > 770:
        x = 770
    if x < 30:
        x = 30
pygame.quit()


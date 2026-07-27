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
    if keys[pygame.K_LEFT]:  x -= 5
    if keys[pygame.K_RIGHT]: x += 5
    if keys[pygame.K_UP]:    y -= 5
    if keys[pygame.K_DOWN]:  y += 5

    screen.fill((0, 0, 0))
    pygame.draw.circle
(screen, (255, 200, 0), (x, y), 30)
    pygame.display.flip()
    clock.tick(60)

import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Ball properties
x, y = WIDTH // 2, 50
radius = 20
velocity_y = 0
gravity = 500  # pixels per second^2

while True:
    dt = clock.tick(60) / 1000  # Delta time (in seconds)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Apply gravity
    velocity_y += gravity * dt
    y += velocity_y * dt

    # Collision with ground
    if y + radius > HEIGHT:
        y = HEIGHT - radius
        velocity_y = -velocity_y * 0.8  # bounce back with reduced speed

    # Draw
    screen.fill(BLACK)
    pygame.draw.circle(screen, WHITE, (int(x), int(y)), radius)
    pygame.display.flip()

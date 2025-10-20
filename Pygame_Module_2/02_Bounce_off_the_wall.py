import pygame
import sys

pygame.init()

# Window setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Physics Motion: Gravity + Wall Bounce")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
RED = (255, 50, 50)

# Ball properties
x, y = WIDTH // 2, 50
radius = 20
velocity_x = 200    # horizontal speed (pixels/sec)
velocity_y = 0      # vertical velocity
gravity = 500       # acceleration (pixels/sec²)
bounce_loss = 0.8   # energy lost per bounce
ground_loss = 0.8   # energy lost per horizontal motion

while True:
    dt = clock.tick(60) / 1000  # convert milliseconds → seconds

    # Handle quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update physics
    velocity_y += gravity * dt
    x += velocity_x * dt
    y += velocity_y * dt

    # Bounce off floor
    if y + radius > HEIGHT:
        y = HEIGHT - radius
        velocity_y = -velocity_y * bounce_loss

    # Bounce off walls
    if x - radius < 0 or x + radius > WIDTH:
        velocity_x = -velocity_x 
        velocity_x *= ground_loss
    
    # Draw everything
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (int(x), int(y)), radius)
    pygame.display.flip()

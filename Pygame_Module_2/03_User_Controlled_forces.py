import pygame
import sys

pygame.init()

# ----- Window Settings -----
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Free Motion Ball ⚙️")

# ----- Colors -----
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# ----- Ball Setup -----
x, y = WIDTH // 2, HEIGHT // 2
radius = 20
vel_x, vel_y = 0, 0
gravity = 0.5
bounce = 0.8
move_speed = 0.5
air_resistance = 0.99

clock = pygame.time.Clock()

# ----- Game Loop -----
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # ----- Horizontal Movement -----
    if keys[pygame.K_LEFT]:
        vel_x -= move_speed
    if keys[pygame.K_RIGHT]:
        vel_x += move_speed

    # ----- Vertical Movement -----
    if keys[pygame.K_UP] and y >= HEIGHT - radius - 1:  # Jump only when on ground
        vel_y = -10
    if keys[pygame.K_DOWN] and vel_y > 0:  # Accelerate fall
        vel_y += 0.5

    # ----- Apply Gravity -----
    vel_y += gravity

    # ----- Update Position -----
    x += vel_x
    y += vel_y

    # ----- Collision with Walls -----
    if x - radius <= 0 or x + radius >= WIDTH:
        vel_x = -vel_x * bounce

    # ----- Collision with Ground -----
    if y + radius >= HEIGHT:
        y = HEIGHT - radius
        vel_y = -vel_y * bounce

    # ----- Air Resistance -----
    vel_x *= air_resistance
    vel_y *= air_resistance

    # ----- Drawing -----
    screen.fill(BLACK)
    pygame.draw.circle(screen, WHITE, (int(x), int(y)), radius)

    pygame.display.flip()
    clock.tick(60)

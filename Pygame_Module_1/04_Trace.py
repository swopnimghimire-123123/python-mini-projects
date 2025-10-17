import pygame
import sys
import math

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Trail Effect Demo")

# Colors
BLUE = (0, 120, 255)
BLACK = (0, 0, 0)

# Player
player_size = 50
player_speed = 300
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT // 2 - player_size // 2

clock = pygame.time.Clock()

# ----- Create a Transparent Surface for Trails -----
trail_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

running = True
while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    dx, dy = 0, 0
    if keys[pygame.K_LEFT]:
        dx -= 1
    if keys[pygame.K_RIGHT]:
        dx += 1
    if keys[pygame.K_UP]:
        dy -= 1
    if keys[pygame.K_DOWN]:
        dy += 1

    length = math.hypot(dx, dy)
    if length != 0:
        dx /= length
        dy /= length

    player_x += dx * player_speed * dt
    player_y += dy * player_speed * dt

    player_x = max(0, min(WIDTH - player_size, player_x))
    player_y = max(0, min(HEIGHT - player_size, player_y))

    # ----- Draw Trail -----
    # Fill the trail surface with a transparent black (alpha=25 means slightly fades)
    trail_surface.fill((0, 0, 0, 25))  
    screen.blit(trail_surface, (0, 0))  # Overlay it on main screen

    # Draw the player (this stays bright, trails fade behind it)
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))

    pygame.display.flip()

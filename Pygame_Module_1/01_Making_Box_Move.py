import pygame
import sys

# Initialize Pygame
pygame.init()

# ----- Window Setup -----
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Smooth Movement Demo")

# ----- Clock for FPS -----
clock = pygame.time.Clock()

# ----- Colors -----
WHITE = (255, 255, 255)
BLUE = (0, 120, 255)

# ----- Player Setup -----
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT // 2 - player_size // 2
player_speed = 300  # pixels per second

# ----- Game Loop -----
while True:
    # Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # ----- Delta Time (time between frames) -----
    dt = clock.tick(60) / 1000  # convert ms to seconds (important!)

    # ----- Movement -----
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed * dt
    if keys[pygame.K_RIGHT]:
        player_x += player_speed * dt
    if keys[pygame.K_UP]:
        player_y -= player_speed * dt
    if keys[pygame.K_DOWN]:
        player_y += player_speed * dt

    # ----- Boundaries ----- 
    player_x = max(0, min(WIDTH - player_size, player_x))
    player_y = max(0, min(HEIGHT - player_size, player_y))

    # ----- Drawing -----
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))
    pygame.display.flip()

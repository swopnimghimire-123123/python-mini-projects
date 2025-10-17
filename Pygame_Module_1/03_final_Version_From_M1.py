import pygame
import sys
import math

# ----- Initialize Pygame -----
pygame.init()

# ----- Window Settings -----
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Module 1: Smooth Movement + Dynamic Background")

# ----- Colors -----
WHITE = (255, 255, 255)
BLUE = (0, 120, 255)
BLACK = (0, 0, 0)

# ----- Player Settings -----
player_size = 50
player_speed = 300  # pixels per second
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT // 2 - player_size // 2

# ----- Clock and Font -----
clock = pygame.time.Clock()
font = pygame.font.Font(None, 28)

# ----- Game Loop -----
running = True
while running:
    # Time delta for smooth motion
    dt = clock.tick(60) / 1000  # seconds between frames (60 FPS target)

    # ----- Event Handling -----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # ----- Movement Input -----
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

    # ----- Normalize Diagonal Movement -----
    length = math.hypot(dx, dy)
    if length != 0:
        dx /= length
        dy /= length

    # ----- Update Player Position -----
    player_x += dx * player_speed * dt
    player_y += dy * player_speed * dt

    # ----- Keep Player Inside Window -----
    player_x = max(0, min(WIDTH - player_size, player_x))
    player_y = max(0, min(HEIGHT - player_size, player_y))

    # ----- Dynamic Background Color -----
    if keys[pygame.K_LEFT]:
        bg_color = (255, 230, 230)  # light red
    elif keys[pygame.K_RIGHT]:
        bg_color = (230, 255, 230)  # light green
    elif keys[pygame.K_UP]:
        bg_color = (230, 230, 255)  # light blue
    elif keys[pygame.K_DOWN]:
        bg_color = (255, 255, 200)  # light yellow
    else:
        bg_color = WHITE


    # ----- Drawing -----
    screen.fill(bg_color)
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))

    # ----- FPS Display -----
    fps_text = font.render(f"FPS: {int(clock.get_fps())}", True, BLACK)
    screen.blit(fps_text, (10, 10))

    # ----- Update Display -----
    pygame.display.flip()

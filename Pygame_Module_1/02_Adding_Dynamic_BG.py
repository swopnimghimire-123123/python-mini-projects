import pygame
pygame.init()

# ----- Window setup -----
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Smooth Movement + Dynamic Background")

# ----- Colors -----
BLACK = (0, 0, 0)
BLUE = (0, 120, 255)
RED = (255, 80, 80)
GREEN = (80, 255, 80)
YELLOW = (255, 255, 80)
PURPLE = (200, 100, 255)

# ----- Player setup -----
player_size = 50
player = pygame.Rect(WIDTH // 2 - player_size // 2, HEIGHT // 2 - player_size // 2, player_size, player_size)
speed = 250  # pixels per second (not per frame)

# ----- Clock for framerate control -----
clock = pygame.time.Clock()

# ----- Game loop -----
running = True
while running:
    dt = clock.tick(60) / 1000  # seconds since last frame

    # --- Handle events ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Get key states ---
    keys = pygame.key.get_pressed()

    # Movement logic
    dx, dy = 0, 0
    if keys[pygame.K_LEFT]:
        dx = -1
    if keys[pygame.K_RIGHT]:
        dx = 1
    if keys[pygame.K_UP]:
        dy = -1
    if keys[pygame.K_DOWN]:
        dy = 1

    # Normalize diagonal movement (so diagonal isn’t faster)
    if dx != 0 and dy != 0:
        dx *= 0.7071
        dy *= 0.7071

    # Update player position (speed × time)
    player.x += dx * speed * dt
    player.y += dy * speed * dt

    # Keep player inside screen
    player.x = max(0, min(WIDTH - player.width, player.x))
    player.y = max(0, min(HEIGHT - player.height, player.y))

    # --- Background color logic ---
    if keys[pygame.K_LEFT]:
        bg_color = RED
    elif keys[pygame.K_RIGHT]:
        bg_color = GREEN
    elif keys[pygame.K_UP]:
        bg_color = YELLOW
    elif keys[pygame.K_DOWN]:
        bg_color = PURPLE
    else:
        bg_color = BLACK

    # --- Draw everything ---
    screen.fill(bg_color)
    pygame.draw.rect(screen, BLUE, player)
    pygame.display.flip()

    font = pygame.font.Font(None, 24)
    fps_text = font.render(f"FPS: {int(clock.get_fps())}", True, (0, 0, 0))
    screen.blit(fps_text, (10, 10))

pygame.quit()

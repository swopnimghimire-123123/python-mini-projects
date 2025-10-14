import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# ----- Window Settings -----
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Ball 🎯")

# ----- Colors -----
WHITE = (255, 255, 255)
BLUE = (50, 100, 255)
RED = (255, 50, 50)
BLACK = (0, 0, 0)

# ----- Font -----
font = pygame.font.Font(None, 36)

# ----- Function to Run the Game -----
def start_game():
    # Player Setup
    player_size = 40
    player_x = WIDTH // 2 - player_size // 2
    player_y = HEIGHT - player_size - 10
    player_speed = 6

    # Ball Setup
    ball_size = 25
    ball_x = random.randint(0, WIDTH - ball_size)
    ball_y = random.randint(0, HEIGHT - ball_size)

    # Score & Timer Setup
    score = 0
    total_time = 30
    start_ticks = pygame.time.get_ticks()

    # Clock
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # ----- Movement -----
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
        if keys[pygame.K_UP]:
            player_y -= player_speed
        if keys[pygame.K_DOWN]:
            player_y += player_speed

        # ----- Boundaries -----
        player_x = max(0, min(WIDTH - player_size, player_x))
        player_y = max(0, min(HEIGHT - player_size, player_y))

        # ----- Collision Detection -----
        player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
        ball_rect = pygame.Rect(ball_x, ball_y, ball_size, ball_size)

        if player_rect.colliderect(ball_rect):
            score += 1
            ball_x = random.randint(0, WIDTH - ball_size)
            ball_y = random.randint(0, HEIGHT - ball_size)

        # ----- Timer -----
        seconds_passed = (pygame.time.get_ticks() - start_ticks) / 1000
        time_left = max(0, int(total_time - seconds_passed))

        if time_left == 0:
            running = False

        # ----- Drawing -----
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLUE, player_rect)
        pygame.draw.circle(screen, RED, (ball_x + ball_size // 2, ball_y + ball_size // 2), ball_size // 2)

        # Display Score & Timer
        score_text = font.render(f"Score: {score}", True, BLACK)
        timer_text = font.render(f"Time: {time_left}", True, BLACK)
        screen.blit(score_text, (10, 10))
        screen.blit(timer_text, (WIDTH - 130, 10))

        # ----- Update Display -----
        pygame.display.flip()
        clock.tick(60)

    # Show Game Over Screen
    show_game_over(score)


# ----- Function to Show Game Over and Restart -----
def show_game_over(final_score):
    while True:
        screen.fill(WHITE)
        end_text = font.render(f"Time's Up! Final Score: {final_score}", True, BLACK)
        restart_text = font.render("Press R to Restart or Q to Quit", True, (100, 100, 100))

        screen.blit(end_text, (WIDTH // 2 - end_text.get_width() // 2, HEIGHT // 2 - 60))
        screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    start_game()
                    return
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()


# ----- Start the Game -----
start_game()

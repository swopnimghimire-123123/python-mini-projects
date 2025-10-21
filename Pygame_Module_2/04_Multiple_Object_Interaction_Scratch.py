import pygame
import random
import math
import sys

# ----- Initialize Pygame -----
pygame.init()

# ----- Window Setup -----
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball Collision Simulation 💥")

# ----- Colors -----
BLACK = (0, 0, 0)
COLORS = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255),
    (255, 255, 0), (255, 0, 255), (0, 255, 255)
]

# ----- Ball Class -----
class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel_x = random.uniform(-4, 4)
        self.vel_y = random.uniform(-4, 4)

    def update(self):
        # Move ball
        self.x += self.vel_x
        self.y += self.vel_y

        # Proper wall collision (ball can't leave screen)
        if self.x - self.radius <= 0:
            self.x = self.radius
            self.vel_x *= -1
        if self.x + self.radius >= WIDTH:
            self.x = WIDTH - self.radius
            self.vel_x *= -1
        if self.y - self.radius <= 0:
            self.y = self.radius
            self.vel_y *= -1
        if self.y + self.radius >= HEIGHT:
            self.y = HEIGHT - self.radius
            self.vel_y *= -1

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)

    def check_collision(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        distance = math.hypot(dx, dy)

        if distance < self.radius + other.radius:
            angle = math.atan2(dy, dx)

            # Swap velocities (elastic collision)
            self.vel_x, other.vel_x = other.vel_x, self.vel_x
            self.vel_y, other.vel_y = other.vel_y, self.vel_y

            # Separate overlapping balls
            overlap = 0.5 * (self.radius + other.radius - distance + 1)
            self.x -= math.cos(angle) * overlap
            self.y -= math.sin(angle) * overlap
            other.x += math.cos(angle) * overlap
            other.y += math.sin(angle) * overlap

# ----- Create Balls -----
NUM_BALLS = 10
balls = []
for _ in range(NUM_BALLS):
    radius = random.randint(20, 30)
    x = random.randint(radius, WIDTH - radius)
    y = random.randint(radius, HEIGHT - radius)
    color = random.choice(COLORS)
    balls.append(Ball(x, y, radius, color))

# ----- Clock -----
clock = pygame.time.Clock()

# ----- Game Loop -----
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)

    # Update, check collisions, draw
    for i, ball in enumerate(balls):
        ball.update()
        for j in range(i + 1, len(balls)):
            ball.check_collision(balls[j])
        ball.draw(screen)

    pygame.display.flip()
    clock.tick(60)

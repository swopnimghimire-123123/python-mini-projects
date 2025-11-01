import pygame
import random
import math
import sys
import itertools

pygame.init()

# ----- Window setup -----
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball Collision — Reliable Version")

# ----- Colors -----
BLACK = (0, 0, 0)
COLORS = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255),
    (255, 255, 0), (255, 0, 255), (0, 255, 255)
]

# ----- Ball Sprite Class -----
class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, color):
        super().__init__()
        self.radius = radius
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        self.rect = self.image.get_rect(center=(x, y))
        # Use floats for accurate movement
        self.pos = pygame.math.Vector2(self.rect.center)
        self.vel = pygame.math.Vector2(random.uniform(-150, 150), random.uniform(-150, 150))  # pixels/sec

    def update(self, dt):
        # Integrate position
        self.pos += self.vel * dt
        self.rect.center = (int(self.pos.x), int(self.pos.y))

        # Wall bounce — reflect velocity and keep inside screen
        if self.pos.x - self.radius < 0:
            self.pos.x = self.radius
            self.vel.x *= -1
        if self.pos.x + self.radius > WIDTH:
            self.pos.x = WIDTH - self.radius
            self.vel.x *= -1
        if self.pos.y - self.radius < 0:
            self.pos.y = self.radius
            self.vel.y *= -1
        if self.pos.y + self.radius > HEIGHT:
            self.pos.y = HEIGHT - self.radius
            self.vel.y *= -1

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)


def handle_ball_collisions(balls):
    """Pairwise collision resolution (each unordered pair handled once)."""
    for a, b in itertools.combinations(balls, 2):
        # Vector between centers
        delta = b.pos - a.pos
        dist = delta.length()
        min_dist = a.radius + b.radius
        if dist == 0:
            # Exact same position — jitter them apart slightly
            dist = 0.01
            delta = pygame.math.Vector2(random.uniform(-1,1), random.uniform(-1,1)).normalize()
        if dist < min_dist:
            # --- Separate overlapping balls ---
            overlap = min_dist - dist
            # Move each ball away proportional to their mass (equal mass here -> half/half)
            correction = delta.normalize() * (overlap / 2)
            a.pos -= correction
            b.pos += correction
            a.rect.center = (int(a.pos.x), int(a.pos.y))
            b.rect.center = (int(b.pos.x), int(b.pos.y))

            # --- Compute simple elastic collision along normal ---
            # Normal vector
            normal = delta.normalize()
            # Relative velocity
            rel_vel = b.vel - a.vel
            # Velocity along normal
            vel_along_normal = rel_vel.dot(normal)
            if vel_along_normal > 0:
                # They are moving apart already; skip
                continue

            # For equal mass spheres, exchange impulse magnitude:
            # coefficient of restitution (bounciness) between 0 and 1
            restitution = 1.0  # 1.0 = perfectly elastic
            j = -(1 + restitution) * vel_along_normal
            j /= 2  # divide by sum of inverse masses (1/m + 1/m) with m=1 => 2

            impulse = normal * j
            a.vel -= impulse
            b.vel += impulse


# ----- Setup multiple balls -----
balls = []
group = pygame.sprite.Group()
for _ in range(12):  # number of balls
    radius = random.randint(18, 28)
    # ensure not spawning overlapping initially
    while True:
        x = random.randint(radius, WIDTH - radius)
        y = random.randint(radius, HEIGHT - radius)
        # simple check against existing balls
        ok = True
        for other in balls:
            if math.hypot(other.pos.x - x, other.pos.y - y) < other.radius + radius + 5:
                ok = False
                break
        if ok:
            break
    color = random.choice(COLORS)
    ball = Ball(x, y, radius, color)
    balls.append(ball)
    group.add(ball)

clock = pygame.time.Clock()

# ----- Main Loop -----
while True:
    dt = clock.tick(60) / 1000.0  # seconds

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update balls
    for ball in balls:
        ball.update(dt)

    # Resolve pairwise collisions once per pair
    handle_ball_collisions(balls)

    # Draw
    screen.fill(BLACK)
    for ball in balls:
        ball.draw(screen)

    pygame.display.flip()
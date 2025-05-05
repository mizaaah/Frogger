import pygame
import random
import time

# Initialisation
pygame.init()
WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Crazy Frogue - Niveaux et Difficulté")

# Couleurs
WHITE = (255, 255, 255)
GREEN = (50, 205, 50)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
YELLOW = (255, 215, 0)

# Constantes
FROG_SIZE = 40
CAR_WIDTH, CAR_HEIGHT = 80, 40
POINT_SIZE = 20
BASE_SCROLL_SPEED = 3
LEVEL_UP_DISTANCE = 1000  # Pixels montés pour monter de niveau
LEVEL_DISPLAY_TIME = 2  # secondes

# Images (placeholder)
frog_image = pygame.Surface((FROG_SIZE, FROG_SIZE))
frog_image.fill(GREEN)

car_image = pygame.Surface((CAR_WIDTH, CAR_HEIGHT))
car_image.fill(RED)

point_image = pygame.Surface((POINT_SIZE, POINT_SIZE))
point_image.fill(YELLOW)

clock = pygame.time.Clock()
FPS = 60

class Player:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.size = FROG_SIZE
        self.speed = 5

    def draw(self, window):
        window.blit(frog_image, (self.x, self.y))

    def move(self, keys):
        scroll = 0
        if keys[pygame.K_LEFT] and self.x - self.speed > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x + self.speed < WIDTH - self.size:
            self.x += self.speed
        if keys[pygame.K_UP]:
            scroll = BASE_SCROLL_SPEED
        elif keys[pygame.K_DOWN]:
            scroll = -BASE_SCROLL_SPEED
        return scroll

class Car:
    def __init__(self, x, y, speed, direction=1):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = direction

    def update(self, scroll, speed_multiplier):
        self.x += self.speed * self.direction * speed_multiplier
        self.y += scroll
        if self.direction == 1 and self.x > WIDTH:
            self.x = -CAR_WIDTH
        elif self.direction == -1 and self.x < -CAR_WIDTH:
            self.x = WIDTH
        if self.y > HEIGHT:
            self.y = random.randint(-1000, -100)

    def draw(self, window):
        window.blit(car_image, (self.x, self.y))

class PointItem:
    def __init__(self):
        self.size = POINT_SIZE
        self.respawn()

    def respawn(self):
        self.x = random.randint(50, WIDTH - 50)
        self.y = random.randint(-1000, HEIGHT - 100)

    def update(self, scroll):
        self.y += scroll
        if self.y > HEIGHT:
            self.respawn()

    def draw(self, window):
        window.blit(point_image, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)

def generate_cars(n):
    cars = []
    for i in range(n):
        y = random.randint(-800, HEIGHT)
        speed = random.randint(2, 5)
        direction = 1 if i % 2 == 0 else -1
        x = random.randint(0, WIDTH - CAR_WIDTH)
        cars.append(Car(x, y, speed, direction))
    return cars

def draw_score(window, score, level):
    font = pygame.font.SysFont("arial", 30)
    text = font.render(f"Score : {score}   Niveau : {level}", True, BLACK)
    window.blit(text, (10, 10))

def draw_level_up(window, level):
    font = pygame.font.SysFont("arial", 50, bold=True)
    text = font.render(f"NIVEAU {level}", True, RED)
    rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    window.blit(text, rect)

def main():
    run = True
    player = Player()
    level = 1
    total_distance = 0
    score = 0
    cars = generate_cars(6)
    point_items = [PointItem() for _ in range(8)]
    level_up_time = None

    while run:
        clock.tick(FPS)
        WINDOW.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        scroll = player.move(keys)

        # Distance monté
        total_distance += scroll
        if scroll < 0:
            score = max(0, score - 1)

        # Niveau up
        new_level = max(1, total_distance // LEVEL_UP_DISTANCE + 1)
        if new_level > level:
            level = new_level
            level_up_time = time.time()
            # Augmenter difficulté
            if len(cars) < 15:
                cars.append(Car(
                    random.randint(0, WIDTH - CAR_WIDTH),
                    random.randint(-1000, 0),
                    random.randint(2, 5),
                    random.choice([-1, 1])
                ))

        # Mettre à jour les voitures
        for car in cars:
            car.update(scroll, 1 + (level - 1) * 0.1)  # vitesse augmente
            car.draw(WINDOW)
            if pygame.Rect(car.x, car.y, CAR_WIDTH, CAR_HEIGHT).colliderect(
                pygame.Rect(player.x, player.y, player.size, player.size)
            ):
                print("Collision ! Reset score.")
                score = 0
                total_distance = 0
                level = 1
                level_up_time = time.time()
                for c in cars:
                    c.y = random.randint(-1000, -100)
                for p in point_items:
                    p.respawn()

        # Mettre à jour pièces
        for item in point_items:
            item.update(scroll)
            if item.get_rect().colliderect(
                pygame.Rect(player.x, player.y, player.size, player.size)
            ):
                score += level
                item.respawn()
            item.draw(WINDOW)

        player.draw(WINDOW)
        draw_score(WINDOW, score, level)

        if level_up_time and time.time() - level_up_time < LEVEL_DISPLAY_TIME:
            draw_level_up(WINDOW, level)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()

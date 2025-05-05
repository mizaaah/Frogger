import pygame
import random

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Crazy Frogue - Scrolling Infini")

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
SCROLL_SPEED = 3

# Images
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
        self.y = HEIGHT // 2  # Centré verticalement
        self.size = FROG_SIZE
        self.speed = 5

    def draw(self, window):
        window.blit(frog_image, (self.x, self.y))

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x - self.speed > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x + self.speed < WIDTH - self.size:
            self.x += self.speed
        # Vers le haut = fait défiler le monde
        if keys[pygame.K_UP]:
            return SCROLL_SPEED
        return 0

class Car:
    def __init__(self, x, y, speed, direction=1):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = direction

    def update(self, scroll):
        self.x += self.speed * self.direction
        self.y += scroll
        if self.direction == 1 and self.x > WIDTH:
            self.x = -CAR_WIDTH
        elif self.direction == -1 and self.x < -CAR_WIDTH:
            self.x = WIDTH

        # Repositionne plus haut si sort par le bas
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

def generate_cars():
    cars = []
    for i in range(8):
        y = random.randint(-800, HEIGHT)
        speed = random.randint(2, 5)
        direction = 1 if i % 2 == 0 else -1
        x = random.randint(0, WIDTH - CAR_WIDTH)
        cars.append(Car(x, y, speed, direction))
    return cars

def draw_score(window, score):
    font = pygame.font.SysFont("arial", 30)
    text = font.render(f"Score : {score}", True, BLACK)
    window.blit(text, (10, 10))

def main():
    run = True
    player = Player()
    cars = generate_cars()
    point_items = [PointItem() for _ in range(8)]
    score = 0

    while run:
        clock.tick(FPS)
        WINDOW.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        scroll = player.move(keys)

        # Mettre à jour voitures
        for car in cars:
            car.update(scroll)
            car.draw(WINDOW)
            if pygame.Rect(car.x, car.y, CAR_WIDTH, CAR_HEIGHT).colliderect(
                pygame.Rect(player.x, player.y, player.size, player.size)
            ):
                print("Collision !")
                score = 0
                # Reset positions
                for c in cars:
                    c.y = random.randint(-1000, -100)
                for p in point_items:
                    p.respawn()

        # Mettre à jour les pièces
        for item in point_items:
            item.update(scroll)
            if item.get_rect().colliderect(
                pygame.Rect(player.x, player.y, player.size, player.size)
            ):
                score += 1
                item.respawn()
            item.draw(WINDOW)

        # Dessiner joueur et score
        player.draw(WINDOW)
        draw_score(WINDOW, score)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()

import pygame
import random

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Crazy Frogue")

# Couleurs
WHITE = (255, 255, 255)
GREEN = (50, 205, 50)
BLACK = (0, 0, 0)
RED = (200, 0, 0)

# Horloge
clock = pygame.time.Clock()
FPS = 60

# Chargement des images (placeholders)
FROG_SIZE = 40
frog_image = pygame.Surface((FROG_SIZE, FROG_SIZE))
frog_image.fill(GREEN)

CAR_WIDTH, CAR_HEIGHT = 80, 40
car_image = pygame.Surface((CAR_WIDTH, CAR_HEIGHT))
car_image.fill(RED)

# Joueur
class Player:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT - FROG_SIZE
        self.size = FROG_SIZE
        self.speed = 5

    def draw(self, window):
        window.blit(frog_image, (self.x, self.y))

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x - self.speed > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x + self.speed < WIDTH - self.size:
            self.x += self.speed
        if keys[pygame.K_UP] and self.y - self.speed > 0:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y + self.speed < HEIGHT - self.size:
            self.y += self.speed

# Obstacle (voitures)
class Car:
    def __init__(self, x, y, speed, direction=1):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = direction  # 1 = droite, -1 = gauche

    def update(self):
        self.x += self.speed * self.direction
        if self.direction == 1 and self.x > WIDTH:
            self.x = -CAR_WIDTH
        elif self.direction == -1 and self.x < -CAR_WIDTH:
            self.x = WIDTH

    def draw(self, window):
        window.blit(car_image, (self.x, self.y))

# Génération de voitures sur plusieurs lignes
def generate_cars():
    cars = []
    for i in range(5):
        y = 100 + i * 80
        speed = random.randint(3, 6)
        direction = 1 if i % 2 == 0 else -1
        x = random.randint(0, WIDTH)
        cars.append(Car(x, y, speed, direction))
    return cars

# Affichage du score
def draw_score(window, score):
    font = pygame.font.SysFont("arial", 30)
    text = font.render(f"Score : {score}", True, BLACK)
    window.blit(text, (10, 10))

# Boucle principale du jeu
def main():
    run = True
    player = Player()
    cars = generate_cars()
    score = 0

    while run:
        clock.tick(FPS)
        WINDOW.fill(WHITE)

        # Événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Mouvements
        keys = pygame.key.get_pressed()
        player.move(keys)

        # Mise à jour des voitures
        for car in cars:
            car.update()
            car.draw(WINDOW)
            # Collision
            if pygame.Rect(car.x, car.y, CAR_WIDTH, CAR_HEIGHT).colliderect(
                pygame.Rect(player.x, player.y, player.size, player.size)
            ):
                print("Collision !")
                score = 0
                player.y = HEIGHT - FROG_SIZE

        # Score si le joueur atteint le haut
        if player.y <= 0:
            score += 1
            player.y = HEIGHT - FROG_SIZE

        # Dessin
        player.draw(WINDOW)
        draw_score(WINDOW, score)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()

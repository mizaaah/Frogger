import pygame
import random
import sys

# Initialisation
pygame.init()
WIDTH, HEIGHT = 600, 800
COLS = 10
TILE_SIZE = WIDTH // COLS

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 36)

# Couleurs
COLORS = {
    "grass": (34, 177, 76),
    "road": (128, 128, 128),
    "water": (0, 162, 232),
    "rail": (100, 100, 100),
    "empty": (200, 200, 200),
}
RED = (200, 0, 0)
BROWN = (139, 69, 19)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Joueur
player = pygame.Rect(WIDTH // 2, HEIGHT - TILE_SIZE * 2, TILE_SIZE, TILE_SIZE)

# Map
terrain_map = []
cars = []
logs = []
trains = []

# Score
score = 0
scroll_y = 0

def generate_row():
    terrain_types = ["grass", "road", "water", "rail", "empty"]
    terrain = random.choices(terrain_types, weights=[30, 30, 20, 10, 10])[0]
    terrain_map.insert(0, terrain)

    if terrain == "road":
        for _ in range(random.randint(2, 4)):
            car = pygame.Rect(random.randint(0, WIDTH), 0, TILE_SIZE, TILE_SIZE)
            cars.append((car, random.choice([-5, 5])))
    elif terrain == "water":
        for _ in range(random.randint(2, 3)):
            log = pygame.Rect(random.randint(0, WIDTH), 0, TILE_SIZE * 3, TILE_SIZE)
            logs.append((log, random.choice([-3, 3])))
    elif terrain == "rail":
        if random.random() < 0.5:
            train = pygame.Rect(-300, 0, TILE_SIZE * 5, TILE_SIZE)
            trains.append((train, 10))

def move_player(dx, dy):
    global score, scroll_y
    player.x += dx * TILE_SIZE
    player.y += dy * TILE_SIZE

    # Empêcher de sortir de l'écran horizontalement
    if player.x < 0:
        player.x = 0
    if player.x > WIDTH - TILE_SIZE:
        player.x = WIDTH - TILE_SIZE

    if dy == -1:
        score += 1
        scroll_y += TILE_SIZE

        # Générer une nouvelle ligne
        generate_row()

        # Nettoyer les objets trop vieux
        for i in range(len(cars)):
            cars[i] = (cars[i][0].move(0, TILE_SIZE), cars[i][1])
        for i in range(len(logs)):
            logs[i] = (logs[i][0].move(0, TILE_SIZE), logs[i][1])
        for i in range(len(trains)):
            trains[i] = (trains[i][0].move(0, TILE_SIZE), trains[i][1])

        # Retirer objets hors écran
        cars[:] = [(c, s) for c, s in cars if c.y < HEIGHT]
        logs[:] = [(l, s) for l, s in logs if l.y < HEIGHT]
        trains[:] = [(t, s) for t, s in trains if t.y < HEIGHT]

def reset():
    global player, terrain_map, cars, logs, trains, score, scroll_y
    player.x = WIDTH // 2
    player.y = HEIGHT - TILE_SIZE * 2
    terrain_map = []
    cars = []
    logs = []
    trains = []
    score = 0
    scroll_y = 0

    for _ in range(20):
        generate_row()

def draw():
    # Fond
    for i, terrain in enumerate(terrain_map):
        y = i * TILE_SIZE - scroll_y
        if 0 <= y <= HEIGHT:
            pygame.draw.rect(screen, COLORS.get(terrain, (200, 200, 200)), (0, y, WIDTH, TILE_SIZE))

    # Objets
    for car, _ in cars:
        pygame.draw.rect(screen, RED, car.move(0, -scroll_y))

    for log, _ in logs:
        pygame.draw.rect(screen, BROWN, log.move(0, -scroll_y))

    for train, _ in trains:
        pygame.draw.rect(screen, (80, 0, 0), train.move(0, -scroll_y))

    # Joueur
    pygame.draw.rect(screen, WHITE, player)

    # Score
    text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(text, (10, 10))

# --- Démarrage ---
reset()

# Boucle principale
running = True
while running:
    clock.tick(30)
    screen.fill((0, 0, 0))
    draw()

    # Mouvements objets
    for i, (car, speed) in enumerate(cars):
        car.x += speed
        if car.right < 0:
            car.left = WIDTH
        if car.left > WIDTH:
            car.right = 0
        cars[i] = (car, speed)

    for i, (log, speed) in enumerate(logs):
        log.x += speed
        if log.right < 0:
            log.left = WIDTH
        if log.left > WIDTH:
            log.right = 0
        logs[i] = (log, speed)

    for i, (train, speed) in enumerate(trains):
        train.x += speed
        if train.left > WIDTH + 300:
            trains[i] = (pygame.Rect(-300, train.y, TILE_SIZE * 5, TILE_SIZE), speed)

    # Collision avec voitures
    for car, _ in cars:
        if player.colliderect(car.move(0, -scroll_y)):
            reset()

    # Collision avec trains
    for train, _ in trains:
        if player.colliderect(train.move(0, -scroll_y)):
            reset()

    # Collision avec rivière
    player_row = (player.y + scroll_y) // TILE_SIZE
    if 0 <= player_row < len(terrain_map):
        terrain = terrain_map[player_row]
        if terrain == "water":
            on_log = False
            for log, speed in logs:
                shifted_log = log.move(0, -scroll_y)
                if player.colliderect(shifted_log):
                    player.x += speed  # Le joueur glisse avec la bûche
                    on_log = True
            if not on_log:
                reset()

    # Événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_player(-1, 0)
            if event.key == pygame.K_RIGHT:
                move_player(1, 0)
            if event.key == pygame.K_UP:
                move_player(0, -1)
            if event.key == pygame.K_DOWN:
                move_player(0, 1)

    pygame.display.flip()

pygame.quit()
sys.exit()

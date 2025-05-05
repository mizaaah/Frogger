import pygame
import random
import sys

# Initialisation
pygame.init()
WIDTH, HEIGHT = 600, 700
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Frogger Simplifié")
CLOCK = pygame.time.Clock()
FONT = pygame.font.SysFont(None, 36)

# Couleurs
VERT = (0, 255, 0)
ROUGE = (255, 0, 0)
NOIR = (0, 0, 0)
BLANC = (255, 255, 255)

# Grenouille
frog = pygame.Rect(WIDTH // 2, HEIGHT - 50, 40, 40)
vitesse_frog = 5

# Voitures
cars = []
CAR_WIDTH, CAR_HEIGHT = 60, 40
for i in range(5):
    x = random.randint(0, WIDTH - CAR_WIDTH)
    y = i * 120 + 60
    speed = random.choice([3, 4, 5])
    cars.append({'rect': pygame.Rect(x, y, CAR_WIDTH, CAR_HEIGHT), 'speed': speed})

# Score
score = 0
previous_y = frog.y

# Boucle de jeu
running = True
while running:
    SCREEN.fill(NOIR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Contrôles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and frog.left > 0:
        frog.x -= vitesse_frog
    if keys[pygame.K_RIGHT] and frog.right < WIDTH:
        frog.x += vitesse_frog
    if keys[pygame.K_UP] and frog.top > 0:
        frog.y -= vitesse_frog
    if keys[pygame.K_DOWN] and frog.bottom < HEIGHT:
        frog.y += vitesse_frog

    # Score basé sur la montée
    if frog.y < previous_y:
        score += 1
    elif frog.y > previous_y:
        score -= 1
    previous_y = frog.y

    # Dessiner grenouille
    pygame.draw.rect(SCREEN, VERT, frog)

    # Dessiner et déplacer les voitures
    for car in cars:
        car['rect'].x += car['speed']
        if car['rect'].left > WIDTH:
            car['rect'].x = -CAR_WIDTH
        pygame.draw.rect(SCREEN, ROUGE, car['rect'])

        # Collision
        if frog.colliderect(car['rect']):
            frog.y = HEIGHT - 50
            score = 0

    # Gagner = atteindre le haut
    if frog.top <= 0:
        frog.y = HEIGHT - 50
        score += 50  # Bonus de réussite

    # Affichage du score
    score_text = FONT.render(f"Score : {score}", True, BLANC)
    SCREEN.blit(score_text, (10, 10))

    pygame.display.flip()
    CLOCK.tick(60)

pygame.quit()
sys.exit()

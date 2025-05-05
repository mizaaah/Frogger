import pygame
import sys

# Initialisation
pygame.init()
WIDTH, HEIGHT = 600, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Frogger avec fond défilant")
clock = pygame.time.Clock()

# Chargement et préparation du fond
background = pygame.image.load("IMAGES/FondRoute.jpg").convert()
background = pygame.transform.rotate(background, 90)  # Tourner si besoin
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Joueur (grenouille)
frog = pygame.Rect(WIDTH // 2 - 20, HEIGHT - 60, 40, 40)
frog_speed = 5
fixed_frog_y = HEIGHT // 2  # Position fixe à partir du milieu

# Fond (deux copies pour défilement continu)
bg_y1 = 0
bg_y2 = -HEIGHT
scroll_offset = 0  # Décalage vertical total et le score

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Gestion des mouvements gauche/droite
    if keys[pygame.K_LEFT] and frog.x > 0:
        frog.x -= frog_speed
    if keys[pygame.K_RIGHT] and frog.x + frog.width < WIDTH:
        frog.x += frog_speed

    # Mouvement haut/bas et défilement du fond
    if keys[pygame.K_UP]:
        if frog.y > fixed_frog_y:
            frog.y -= frog_speed
        else:
            scroll_offset += frog_speed
            bg_y1 += frog_speed
            bg_y2 += frog_speed
    if keys[pygame.K_DOWN]:
        if frog.y < HEIGHT - frog.height:
            frog.y += frog_speed
        elif scroll_offset > 0:
            scroll_offset -= frog_speed
            bg_y1 -= frog_speed
            bg_y2 -= frog_speed

    # Bouclage du fond
    if bg_y1 >= HEIGHT:
        bg_y1 = bg_y2 - HEIGHT
    if bg_y2 >= HEIGHT:
        bg_y2 = bg_y1 - HEIGHT

    # Affichage
    screen.blit(background, (0, bg_y1))
    screen.blit(background, (0, bg_y2))
    pygame.draw.rect(screen, (0, 255, 0), frog)  # Grenouille

    pygame.display.flip()
    clock.tick(60)

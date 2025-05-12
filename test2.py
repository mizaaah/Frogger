import pygame
import sys
import random

# Initialisation
pygame.init()
WIDTH, HEIGHT = 600, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Frogger")
clock = pygame.time.Clock()

# Fond
background = pygame.image.load("Frogger/IMAGES/FondRoute.jpg").convert()
background = pygame.transform.rotate(background, 90)
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Image de la grenouille
frog_img_size = 50
frog_img = pygame.image.load("Frogger/IMAGES/Perso.png").convert_alpha()
frog_img = pygame.transform.scale(frog_img, (frog_img_size, frog_img_size))

# Images des véhicules : voitures et camions
car_left_img1 = pygame.image.load("Frogger/IMAGES/VoitureGDgauche.png").convert_alpha()
car_right_img1 = pygame.image.load("Frogger/IMAGES/VoitureGDdroite.png").convert_alpha()
car_left_img2 = pygame.image.load("Frogger/IMAGES/VoitureRDgauche.png").convert_alpha()
car_right_img2 = pygame.image.load("Frogger/IMAGES/VoitureRDdroite.png").convert_alpha()

truck_left_img1 = pygame.image.load("Frogger/IMAGES/CamionGGauche.png").convert_alpha()
truck_right_img1 = pygame.image.load("Frogger/IMAGES/CamionGDdroite.png").convert_alpha()
truck_left_img2 = pygame.image.load("Frogger/IMAGES/CamionRDgauche.png").convert_alpha()
truck_right_img2 = pygame.image.load("Frogger/IMAGES/CamionRDdroite.png").convert_alpha()

# Redimensionner les véhicules
car_img_size = (120, 60)
truck_img_size = (180, 80)

car_left_img1 = pygame.transform.scale(car_left_img1, car_img_size)
car_right_img1 = pygame.transform.scale(car_right_img1, car_img_size)
car_left_img2 = pygame.transform.scale(car_left_img2, car_img_size)
car_right_img2 = pygame.transform.scale(car_right_img2, car_img_size)

truck_left_img1 = pygame.transform.scale(truck_left_img1, truck_img_size)
truck_right_img1 = pygame.transform.scale(truck_right_img1, truck_img_size)
truck_left_img2 = pygame.transform.scale(truck_left_img2, truck_img_size)
truck_right_img2 = pygame.transform.scale(truck_right_img2, truck_img_size)

# Couleurs
RED = (200, 0, 0)
WHITE = (255, 255, 255)

# Constantes joueur
frog_speed = 2.5
fixed_frog_y = HEIGHT // 2

# Voies de circulation
lanes_y = [510, 420, 260, 100]  # Tu remplaces l’ancienne liste par celle-ci

cars = []

# Créer une voiture ou un camion avec une hitbox basée sur l'image
def create_car():
    lane = random.choice(lanes_y)
    direction = random.choice(["left", "right"])
    vehicle_type = random.choice(["car", "truck"])
    car_variant = random.choice([1, 2])

    if vehicle_type == "car":
        size = car_img_size
        if direction == "left":
            image = car_left_img1 if car_variant == 1 else car_left_img2
        else:
            image = car_right_img1 if car_variant == 1 else car_right_img2
    else:
        size = truck_img_size
        if direction == "left":
            image = truck_left_img1 if car_variant == 1 else truck_left_img2
        else:
            image = truck_right_img1 if car_variant == 1 else truck_right_img2

    if direction == "left":
        x = WIDTH
        speed = random.randint(3, 6) * -1
    else:
        x = -size[0]
        speed = random.randint(2, 5)

    rect = image.get_rect(topleft=(x, lane))
    return {"rect": rect, "speed": speed, "image": image}

# Réinitialisation du jeu
def reset_game():
    global frog_rect, scroll_offset, bg_y1, bg_y2, cars
    frog_rect = frog_img.get_rect()
    frog_rect.centerx = WIDTH // 2
    frog_rect.bottom = HEIGHT - 10

    scroll_offset = 0
    bg_y1 = 0
    bg_y2 = -HEIGHT
    cars = [create_car() for _ in range(5)]

# Affichage du texte de fin
def show_game_over():
    font = pygame.font.SysFont(None, 60)
    text = font.render("💀 Nouvelle partie", True, WHITE)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))

# Démarrer
reset_game()
game_over = False
game_over_timer = 0

# Boucle principale
running = True
while running:
    dt = clock.tick(60)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if not game_over:
        # Mouvements latéraux
        if keys[pygame.K_LEFT] and frog_rect.left > 0:
            frog_rect.x -= frog_speed
        if keys[pygame.K_RIGHT] and frog_rect.right < WIDTH:
            frog_rect.x += frog_speed

        # Haut / Bas avec scrolling
        if keys[pygame.K_UP]:
            if frog_rect.top > fixed_frog_y:
                frog_rect.y -= frog_speed
            else:
                scroll_offset += frog_speed
                bg_y1 += frog_speed
                bg_y2 += frog_speed
                for car in cars:
                    car["rect"].y += frog_speed
        if keys[pygame.K_DOWN] and frog_rect.bottom < HEIGHT:
            frog_rect.y += frog_speed

        # Bouclage fond
        if bg_y1 >= HEIGHT:
            bg_y1 = bg_y2 - HEIGHT
        if bg_y2 >= HEIGHT:
            bg_y2 = bg_y1 - HEIGHT

        # Màj des voitures
        for car in cars:
            car["rect"].x += car["speed"]

        # Nettoyage + génération
        cars = [car for car in cars if -car["rect"].width < car["rect"].x < WIDTH + car["rect"].width]
        while len(cars) < 6:
            cars.append(create_car())

        # Collision
        for car in cars:
            if frog_rect.colliderect(car["rect"]):
                game_over = True
                game_over_timer = pygame.time.get_ticks()

    # Affichage
    screen.blit(background, (0, bg_y1))
    screen.blit(background, (0, bg_y2))

    # Afficher la grenouille
    screen.blit(frog_img, frog_rect)

    # Afficher les voitures et camions
    for car in cars:
        screen.blit(car["image"], car["rect"])
        # pygame.draw.rect(screen, RED, car["rect"], 2)  # décommenter pour voir les hitboxes

    # Game over
    if game_over:
        show_game_over()
        if pygame.time.get_ticks() - game_over_timer > 2000:
            reset_game()
            game_over = False

    for y in lanes_y:
        pygame.draw.line(screen, (255, 0, 0), (0, y), (WIDTH, y), 2)


    pygame.display.flip()  
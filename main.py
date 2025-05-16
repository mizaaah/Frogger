import pygame
import sys
import random
from config import *
import game

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Frogger")
clock = pygame.time.Clock()

# Maintenant que l'affichage est créé, on charge les images et sons
game.load_images()
game.load_sounds()

# Variables de jeu
frog_img = game.images["frog"]
frog_rect = frog_img.get_rect(center=(WIDTH // 2, HEIGHT - 10))
frog_speed = 3
fixed_frog_y = HEIGHT // 2

bg_y1 = 0
bg_y2 = -HEIGHT

cars = []
point_items = []

score = 0
best_score = 0
game_over = False
game_over_timer = 0
scroll_offset = 0

# Fonction pour créer une voiture ou un camion avec ses caractéristiques (position, vitesse, image)
def create_car():
    lane = random.choice(LANES_Y)
    direction = random.choice(["left", "right"])
    vehicle_type = random.choice(["car", "truck"])
    car_variant = random.choice([1, 2])

    if vehicle_type == "car":
        size = CAR_SIZE
        if direction == "left":
            image = game.images["car_left_1"] if car_variant == 1 else game.images["car_left_2"]
        else:
            image = game.images["car_right_1"] if car_variant == 1 else game.images["car_right_2"]
    else:
        size = TRUCK_SIZE
        if direction == "left":
            image = game.images["truck_left_1"] if car_variant == 1 else game.images["truck_left_2"]
        else:
            image = game.images["truck_right_1"] if car_variant == 1 else game.images["truck_right_2"]

    if direction == "left":
        x = WIDTH
        speed = -random.randint(3, 6)
    else:
        x = -size[0]
        speed = random.randint(2, 5)

    rect = image.get_rect(topleft=(x, lane))
    return {"rect": rect, "speed": speed, "image": image}

# Fonction pour réinitialiser l'état du jeu (position, voitures, objets, scores...)
def reset_game():
    global frog_rect, scroll_offset, bg_y1, bg_y2, cars, point_items, score, game_over, game_over_timer
    frog_rect.centerx = WIDTH // 2
    frog_rect.bottom = HEIGHT - 10

    scroll_offset = 0
    bg_y1 = 0
    bg_y2 = -HEIGHT
    cars = [create_car() for _ in range(5)]
    point_items = [game.PointItem() for _ in range(5)]
    score = 0
    game_over = False
    game_over_timer = 0

    #tentative de régler le problème de collision frontale (échouée)
    # def reset_game():
    # global frog_rect, scroll_offset, bg_y1, bg_y2, cars, point_items, score, game_over, game_over_timer
    # frog_rect.centerx = WIDTH // 2
    # frog_rect.bottom = HEIGHT - 10

    # scroll_offset = 0
    # bg_y1 = 0
    # bg_y2 = -HEIGHT
    # cars = []
    # for _ in range(5):
    #     cars.append(create_car(cars))
    # point_items = [game.PointItem() for _ in range(5)]
    # score = 0
    # game_over = False
    # game_over_timer = 0

# Fonction pour dessiner un bouton interactif à l'écran
def draw_button(surface, text, x, y, w, h, color, hover_color, font):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x < mouse[0] < x + w and y < mouse[1] < y + h:
        pygame.draw.rect(surface, hover_color, (x, y, w, h))
        if click[0]:
            return True
    else:
        pygame.draw.rect(surface, color, (x, y, w, h))
    text_surf = font.render(text, True, (0, 0, 0))
    surface.blit(text_surf, (x + (w - text_surf.get_width()) // 2, y + (h - text_surf.get_height()) // 2))
    return False

# Fonction pour afficher le score en haut à gauche
def draw_score():
    font = pygame.font.SysFont(None, 30)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

# Initialisation et lancement de la musique et des sons
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)
moteur_channel = game.moteur_sound.play(-1)
moteur_channel.set_volume(0.5)

reset_game()

# Variables d'état du jeu et polices
state = "menu"
font_big = pygame.font.SysFont(None, 60)
font_small = pygame.font.SysFont(None, 36)

# Boucle principale du jeu
while True:
    dt = clock.tick(60)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if state == "menu":
        screen.blit(game.images["bg"], (0, 0))
        title = font_big.render("FROGGER", True, (255, 255, 255))
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))
        best = font_small.render(f"Meilleur score : {best_score}", True, (255, 255, 0))
        screen.blit(best, (WIDTH // 2 - best.get_width() // 2, 200))

        # Bouton pour démarrer le jeu
        if draw_button(screen, "Jouer", WIDTH // 2 - 100, 350, 200, 60, (0, 200, 0), (0, 255, 0), font_small):
            reset_game()
            state = "jeu"
            pygame.time.wait(200)

        # Bouton pour quitter le jeu
        if draw_button(screen, "Quitter", WIDTH // 2 - 100, 430, 200, 60, (200, 0, 0), (255, 0, 0), font_small):
            pygame.quit()
            sys.exit()

    elif state == "jeu":
        keys = pygame.key.get_pressed()
        if not game_over:
            # Contrôles du joueur pour déplacer la grenouille
            if keys[pygame.K_LEFT] and frog_rect.left > 0:
                frog_rect.x -= frog_speed
            if keys[pygame.K_RIGHT] and frog_rect.right < WIDTH:
                frog_rect.x += frog_speed
            if keys[pygame.K_UP]:
                if frog_rect.top > fixed_frog_y:
                    frog_rect.y -= frog_speed
                else:
                    scroll_offset += frog_speed
                    bg_y1 += frog_speed
                    bg_y2 += frog_speed
                    for car in cars:
                        car["rect"].y += frog_speed
                    for item in point_items:
                        item.y += frog_speed
            if keys[pygame.K_DOWN] and frog_rect.bottom < HEIGHT:
                frog_rect.y += frog_speed

            # Gestion du scrolling infini du fond
            if bg_y1 >= HEIGHT:
                bg_y1 = bg_y2 - HEIGHT
            if bg_y2 >= HEIGHT:
                bg_y2 = bg_y1 - HEIGHT

            # Mise à jour de la position des voitures
            for car in cars:
                car["rect"].x += car["speed"]

            # Suppression des voitures hors écran et ajout de nouvelles
            cars = [car for car in cars if -car["rect"].width < car["rect"].x < WIDTH + car["rect"].width]
            while len(cars) < 6:
                cars.append(create_car())

            # Mise à jour des objets à ramasser et gestion des collisions avec la grenouille
            for item in point_items:
                item.update()
                if item.get_rect().colliderect(frog_rect):
                    score += 1
                    item.respawn()
                    game.piece_sound.play()

            # Détection des collisions entre la grenouille et les voitures
            for car in cars:
                if frog_rect.colliderect(car["rect"]):
                    game_over = True
                    game_over_timer = pygame.time.get_ticks()
                    game.collision_sound.play()

        # Dessin des éléments du jeu
        screen.blit(game.images["bg"], (0, bg_y1))
        screen.blit(game.images["bg"], (0, bg_y2))
        screen.blit(frog_img, frog_rect)
        for car in cars:
            screen.blit(car["image"], car["rect"])
        for item in point_items:
            item.draw(screen)
        draw_score()

        # Affichage des hitbox
        pygame.draw.rect(screen, (0, 255, 0), frog_rect, 2)  # Hitbox grenouille en vert
        for car in cars:
            pygame.draw.rect(screen, (255, 0, 0), car["rect"], 2)  # Hitbox voitures en rouge

        # Affichage écran de fin de partie
        if game_over:
            if score > best_score:
                best_score = score
            text = font_big.render("GAME OVER", True, (255, 0, 0))
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - 100))
            if pygame.time.get_ticks() - game_over_timer > 3000:
                state = "menu"

    pygame.display.flip()

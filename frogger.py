import pygame
import random

pygame.init()

WIDTH = 600
HEIGHT = 800
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Frogger")

#pour avoir une base
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

#joueur(quand la touche reste enfoncée, il se déplace à l'infini mais on veut pas ça)
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT - player_size
player_speed = 15  #15 ou 20 c'est bien

#liste voitures
cars = []

#variables
scroll_y = 0
car_spawn_timer = 0
score = 0
font = pygame.font.SysFont("Arial", 30)

clock = pygame.time.Clock()

#création de voiture
def spawn_car(y_pos):
    width = random.randint(60, 120)
    car = {
        'x': random.choice([-width, WIDTH]),
        'y': y_pos,
        'width': width,
        'height': player_size,
        'speed': random.choice([-5, -4, -3, 3, 4, 5])
    }
    cars.append(car)

#boucle principale
run = True
while run:
    clock.tick(60)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #déplacement
    if keys[pygame.K_LEFT] and player_x - player_speed >= 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x + player_speed <= WIDTH - player_size:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y - player_speed >= 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y + player_speed <= HEIGHT - player_size:
        player_y += player_speed

    #défilement de l'écran
    if player_y < HEIGHT // 2:
        scroll_amount = (HEIGHT // 2 - player_y)
        player_y = HEIGHT // 2
        scroll_y += scroll_amount

        #déplacement des voitures
        for car in cars:
            car['y'] += scroll_amount
        
        score += 1

    #spawn des voitures aléatoire
    car_spawn_timer += 1
    if car_spawn_timer > 30:
        spawn_car(random.randint(-100, 0))
        car_spawn_timer = 0

    # Mise à jour des voitures
    for car in cars:
        car['x'] += car['speed']
    
    #supprimer les voitures qui sortent du cadre
    cars = [car for car in cars if -200 < car['x'] < WIDTH + 200]

    #collision
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    for car in cars:
        car_rect = pygame.Rect(car['x'], car['y'], car['width'], car['height'])
        if player_rect.colliderect(car_rect):
            print("Game Over ! Score :", score)
            run = False

    #fond provisoire
    win.fill(WHITE)

    #joueur
    pygame.draw.rect(win, GREEN, (player_x, player_y, player_size, player_size))

    #voitures provisoire
    for car in cars:
        pygame.draw.rect(win, RED, (car['x'], car['y'], car['width'], car['height']))

    #affichage du score
    score_text = font.render("Score: " + str(score), True, BLACK)
    win.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()
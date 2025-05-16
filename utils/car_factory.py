import random
import pygame
from config import WIDTH, LANES_Y, CAR_SIZE, TRUCK_SIZE
from game import images

# Crée une voiture ou un camion avec position, vitesse et image adaptés
def create_car():
    # Choix aléatoire de la voie, direction, type et variante du véhicule
    lane = random.choice(LANES_Y)
    direction = random.choice(["left", "right"])
    vehicle_type = random.choice(["car", "truck"])
    variant = random.choice([1, 2])

    # Sélection de la taille et de l'image selon le type et la direction
    if vehicle_type == "car":
        size = CAR_SIZE
        if direction == "left":
            image = images["car_left_1"] if variant == 1 else images["car_left_2"]
        else:
            image = images["car_right_1"] if variant == 1 else images["car_right_2"]
    else:
        size = TRUCK_SIZE
        if direction == "left":
            image = images["truck_left_1"] if variant == 1 else images["truck_left_2"]
        else:
            image = images["truck_right_1"] if variant == 1 else images["truck_right_2"]

    # Positionnement horizontal selon la direction, vitesse avec signe adapté
    x = WIDTH if direction == "left" else -size[0]
    speed = random.randint(3, 6) * (-1 if direction == "left" else 1)
    rect = image.get_rect(topleft=(x, lane))

    # Retourne un dictionnaire représentant le véhicule
    return {"rect": rect, "speed": speed, "image": image}

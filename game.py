import pygame
import random
from config import *
from os.path import join

images = {}
collision_sound = None
moteur_sound = None
piece_sound = None

# Fonction utilitaire pour charger une image et la redimensionner à la taille donnée
def load_and_scale(path, size):
    return pygame.transform.scale(pygame.image.load(path).convert_alpha(), size)

# Charge toutes les images du jeu et les stocke dans le dictionnaire global 'images'
def load_images():
    global images
    images = {
        "bg": pygame.transform.scale(
            pygame.transform.rotate(
                pygame.image.load(join(IMG_PATH, "FondRoute.jpg")).convert(), 90),
            (WIDTH, HEIGHT)),
        "frog": load_and_scale(join(IMG_PATH, "Perso.png"), (FROG_SIZE, FROG_SIZE)),
        "piece": load_and_scale(join(IMG_PATH, "piece.png"), (30, 30)),
        "car_left_1": load_and_scale(join(IMG_PATH, "VoitureGDgauche.png"), CAR_SIZE),
        "car_right_1": load_and_scale(join(IMG_PATH, "VoitureGDdroite.png"), CAR_SIZE),
        "car_left_2": load_and_scale(join(IMG_PATH, "VoitureRDgauche.png"), CAR_SIZE),
        "car_right_2": load_and_scale(join(IMG_PATH, "VoitureRDdroite.png"), CAR_SIZE),
        "truck_left_1": load_and_scale(join(IMG_PATH, "CamionGGauche.png"), TRUCK_SIZE),
        "truck_right_1": load_and_scale(join(IMG_PATH, "CamionGDdroite.png"), TRUCK_SIZE),
        "truck_left_2": load_and_scale(join(IMG_PATH, "CamionRDgauche.png"), TRUCK_SIZE),
        "truck_right_2": load_and_scale(join(IMG_PATH, "CamionRDdroite.png"), TRUCK_SIZE),
    }

# Charge tous les sons du jeu et les stocke dans des variables globales
def load_sounds():
    global collision_sound, moteur_sound, piece_sound
    collision_sound = pygame.mixer.Sound(join(SND_PATH, "collision.flac"))
    moteur_sound = pygame.mixer.Sound(join(SND_PATH, "moteur.wav"))
    piece_sound = pygame.mixer.Sound(join(SND_PATH, "piece.ogg"))
    pygame.mixer.music.load(join(SND_PATH, "musique_fond.mp3"))

# Classe représentant un objet "point" à collecter dans le jeu
class PointItem:
    # Initialise un nouvel objet avec sa taille basée sur l'image et le place aléatoirement
    def __init__(self):
        self.width = images["piece"].get_width()
        self.height = images["piece"].get_height()
        self.respawn()

    # Positionne aléatoirement l'objet dans la zone définie
    def respawn(self):
        self.x = random.randint(50, WIDTH - 50)
        self.y = random.randint(120, 420)

    # Met à jour la position verticale pour créer un effet de déplacement vers le haut
    # et repositionne si l'objet sort de l'écran
    def update(self):
        self.y -= 0.5
        if self.y + self.height < 0 or self.y > HEIGHT:
            self.respawn()

    # Dessine l'objet sur la surface donnée
    def draw(self, window):
        window.blit(images["piece"], (self.x, self.y))

    # Renvoie le rectangle collision de l'objet pour détection des collisions
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

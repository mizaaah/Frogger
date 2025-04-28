import pygame

# Initialisation de Pygame
pygame.init()

# Taille de la fenêtre
LARGEUR, HAUTEUR = 600, 800
NB_COLONNES = 10
TAILLE_TUILE = LARGEUR // NB_COLONNES

# Couleurs utilisées
COULEUR_HERBE = (34, 177, 76)
COULEUR_ROUTE = (128, 128, 128)
COULEUR_EAU = (0, 162, 232)
COULEUR_RAIL = (100, 100, 100)
COULEUR_VIDE = (200, 200, 200)

COULEUR_ROUGE = (200, 0, 0)
COULEUR_MARRON = (139, 69, 19)
COULEUR_BLANCO = (255, 255, 255)
COULEUR_NOIR = (0, 0, 0)

COULEURS_TERRAIN = {
    "herbe": COULEUR_HERBE,
    "route": COULEUR_ROUTE,
    "eau": COULEUR_EAU,
    "rail": COULEUR_RAIL,
    "vide": COULEUR_VIDE,
}

import pygame
import random
from config import *

# Fenêtre principale
ecran = pygame.display.set_mode((LARGEUR, HAUTEUR))
horloge = pygame.time.Clock()
police = pygame.font.SysFont("Arial", 36)

# Joueur
joueur = pygame.Rect(LARGEUR // 2, HAUTEUR - TAILLE_TUILE * 2, TAILLE_TUILE, TAILLE_TUILE)

# Listes d'objets
liste_terrain = []
voitures = []
buches = []
trains = []

# Score
score = 0
defilement = 0

def generer_ligne():
    terrains = ["herbe", "route", "eau", "rail", "vide"]
    choix = random.choices(terrains, weights=[30, 30, 20, 10, 10])[0]
    liste_terrain.insert(0, choix)

    if choix == "route":
        for _ in range(random.randint(2, 4)):
            voiture = pygame.Rect(random.randint(0, LARGEUR), 0, TAILLE_TUILE, TAILLE_TUILE)
            voitures.append((voiture, random.choice([-5, 5])))
    elif choix == "eau":
        for _ in range(random.randint(2, 3)):
            buche = pygame.Rect(random.randint(0, LARGEUR), 0, TAILLE_TUILE * 3, TAILLE_TUILE)
            buches.append((buche, random.choice([-3, 3])))
    elif choix == "rail":
        if random.random() < 0.5:
            train = pygame.Rect(-300, 0, TAILLE_TUILE * 5, TAILLE_TUILE)
            trains.append((train, 10))

def deplacer_joueur(dx, dy):
    global score, defilement
    joueur.x += dx * TAILLE_TUILE
    joueur.y += dy * TAILLE_TUILE

    if joueur.x < 0:
        joueur.x = 0
    if joueur.x > LARGEUR - TAILLE_TUILE:
        joueur.x = LARGEUR - TAILLE_TUILE

    if dy == -1:
        score += 1
        defilement += TAILLE_TUILE
        generer_ligne()

        # Décale tout
        for i in range(len(voitures)):
            voitures[i] = (voitures[i][0].move(0, TAILLE_TUILE), voitures[i][1])
        for i in range(len(buches)):
            buches[i] = (buches[i][0].move(0, TAILLE_TUILE), buches[i][1])
        for i in range(len(trains)):
            trains[i] = (trains[i][0].move(0, TAILLE_TUILE), trains[i][1])

        # Nettoyage
        voitures[:] = [(v, vitesse) for v, vitesse in voitures if v.y < HAUTEUR]
        buches[:] = [(b, vitesse) for b, vitesse in buches if b.y < HAUTEUR]
        trains[:] = [(t, vitesse) for t, vitesse in trains if t.y < HAUTEUR]

def recommencer():
    global joueur, liste_terrain, voitures, buches, trains, score, defilement
    joueur.x = LARGEUR // 2
    joueur.y = HAUTEUR - TAILLE_TUILE * 2
    liste_terrain.clear()
    voitures.clear()
    buches.clear()
    trains.clear()
    score = 0
    defilement = 0

    for _ in range(20):
        generer_ligne()

def dessiner_jeu():
    for idx, terrain in enumerate(liste_terrain):
        y = idx * TAILLE_TUILE - defilement
        if 0 <= y <= HAUTEUR:
            pygame.draw.rect(ecran, COULEURS_TERRAIN.get(terrain, COULEUR_VIDE), (0, y, LARGEUR, TAILLE_TUILE))

    for voiture, _ in voitures:
        pygame.draw.rect(ecran, COULEUR_ROUGE, voiture.move(0, -defilement))
    for buche, _ in buches:
        pygame.draw.rect(ecran, COULEUR_MARRON, buche.move(0, -defilement))
    for train, _ in trains:
        pygame.draw.rect(ecran, (80, 0, 0), train.move(0, -defilement))

    pygame.draw.rect(ecran, COULEUR_BLANCO, joueur)
    score_texte = police.render(f"Score: {score}", True, COULEUR_NOIR)
    ecran.blit(score_texte, (10, 10))

import pygame
import random
<<<<<<< HEAD
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
=======
import sys

#DEF taille
LARGEUR_FENETRE = 600
HAUTEUR_FENETRE = 700
TAILLE_GRENOUILLE = 40
VERT = (0, 255, 0)


# Initialiser Pygame
pygame.init()


#class perso/Grenouille
class Frog:
    def __init__(self):
        self.reset()
        self.player = pygame.Rect(100, 300, 50, 50)  # Position de base du joueur

    def update(self):
        # Mise a jour de l'Etat du jeux
        pass
    
    def reinitialiser(self):
        self.x = LARGEUR_FENETRE // 2
        self.y = HAUTEUR_FENETRE - TAILLE_GRENOUILLE - 10
        self.taille = TAILLE_GRENOUILLE
        self.vitesse = 5

    def dessin(self, fenetre):
        pygame.draw.rect(fenetre, VERT, (self.x, self.y, self.taille, self.taille))


    def deplacer(self, keys):
        if keys[pygame.K_LEFT] and self.x -self.vitesse > 0: #Bordure gauche
            self.x -= self.vitesse # bouge gauche
        if keys[pygame.K_RIGHT] and self.x + self.vitesse + self.taille < LARGEUR_FENETRE: #Bordure droite
            self.x += self.vitesse # bouge droite
        if keys[pygame.K_UP] and self.y - self.vitesse > 0:
            self.x += self.vitesse # bouge haut
        if keys[pygame.K_DOWN] and self.y + self.vitesse + self.taille < HAUTEUR_FENETRE:
            self.x += self.vitesse # bouge bas




    def draw_score(self, screen, score):
        # Affiche le score en haut à gauche
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        
        
>>>>>>> 9dfa62cc78bc3f1a37816838a418073e0781f8c3

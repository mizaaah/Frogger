import pygame
import random
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

        
        
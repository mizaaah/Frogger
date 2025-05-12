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
        self.player = pygame.Rect(100, 300, TAILLE_GRENOUILLE, TAILLE_GRENOUILLE)  # Position de base du joueur

    def update(self):
        # Mise a jour de l'Etat du jeux
        pass
    
    def reinitialiser(self):
        self.x = LARGEUR_FENETRE // 2
        self.y = HAUTEUR_FENETRE - TAILLE_GRENOUILLE - 10
        self.taille = TAILLE_GRENOUILLE
        self.vitesse = 5

    def dessin(self, fenetre):
        pygame.draw.rect(fenetre, VERT, self.player)

    #Mouvement selon touche
    def deplacer(self, keys):
        # Déplacer le joueur (grenouille) selon les touches directionnelles
        if keys[pygame.K_LEFT] and self.player.x - self.vitesse > 0:  # Limite
            self.player.x -= self.vitesse  # Déplacement gauche
        if keys[pygame.K_RIGHT] and self.player.x + self.vitesse + self.taille < LARGEUR_FENETRE:  # Limite
            self.player.x += self.vitesse  # Déplacement droit
        if keys[pygame.K_UP] and self.player.y - self.vitesse > 0:  # Limite
            self.player.y -= self.vitesse  # Déplacement haut
        if keys[pygame.K_DOWN] and self.player.y + self.vitesse + self.taille < HAUTEUR_FENETRE:  # Limite
            self.player.y += self.vitesse  # Déplacement bas




    def draw_score(self, screen, score):
        # Affiche le score en haut à gauche
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        
        
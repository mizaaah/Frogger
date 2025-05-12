import pygame
<<<<<<< HEAD
import sys
from game import *  # On importe toutes les fonctions de game.py

# Démarrage
recommencer()

# Boucle principale
en_cours = True
while en_cours:
    horloge.tick(30)
    ecran.fill((0, 0, 0))
    dessiner_jeu()

    # Mouvements
    for i, (voiture, vitesse) in enumerate(voitures):
        voiture.x += vitesse
        if voiture.right < 0:
            voiture.left = LARGEUR
        if voiture.left > LARGEUR:
            voiture.right = 0
        voitures[i] = (voiture, vitesse)

    for i, (buche, vitesse) in enumerate(buches):
        buche.x += vitesse
        if buche.right < 0:
            buche.left = LARGEUR
        if buche.left > LARGEUR:
            buche.right = 0
        buches[i] = (buche, vitesse)

    for i, (train, vitesse) in enumerate(trains):
        train.x += vitesse
        if train.left > LARGEUR + 300:
            trains[i] = (pygame.Rect(-300, train.y, TAILLE_TUILE * 5, TAILLE_TUILE), vitesse)

    # Collisions
    for voiture, _ in voitures:
        if joueur.colliderect(voiture.move(0, -defilement)):
            recommencer()

    for train, _ in trains:
        if joueur.colliderect(train.move(0, -defilement)):
            recommencer()

    ligne_joueur = (joueur.y + defilement) // TAILLE_TUILE
    if 0 <= ligne_joueur < len(liste_terrain):
        terrain = liste_terrain[ligne_joueur]
        if terrain == "eau":
            flottant = False
            for buche, vitesse in buches:
                if joueur.colliderect(buche.move(0, -defilement)):
                    joueur.x += vitesse
                    flottant = True
            if not flottant:
                recommencer()

    # Événements
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            en_cours = False
        if evenement.type == pygame.KEYDOWN:
            if evenement.key == pygame.K_LEFT:
                deplacer_joueur(-1, 0)
            if evenement.key == pygame.K_RIGHT:
                deplacer_joueur(1, 0)
            if evenement.key == pygame.K_UP:
                deplacer_joueur(0, -1)
            if evenement.key == pygame.K_DOWN:
                deplacer_joueur(0, 1)

    pygame.display.flip()

pygame.quit()
sys.exit()
=======
from game import Frog  # Import de la classe qui sera def dans game.py


def main():
    # Initialisation de pygame
    pygame.init()

    #Une création de fentêtre du jeu à faire


    # Initialisation du jeu
    game = Frog()
    score = 0  # Initialisation du score


    #Boucle principal du jeu sera ici : 
    running = True
    while running:
        #boucle




        #Récup touches enfoncées
        keys = pygame.key.get_pressed()
        game.deplacer(keys)  # Déplacer la grenouille selon les touches appuyées

    
        # Mise à jour du jeu
        game.update()

        # Gestion du score : on vérifie si le joueur avance ou recule
        if game.player.y < previous_player_y:  # Le joueur avance
            score += 1  # Augmentation du score
        elif game.player.y > previous_player_y:  # Le joueur recule
            score -= 1  # Retrait de points


        # Affichage des éléments du jeu
        game.draw_score(screen, score)


    pygame.quit()

if __name__ == "__main__":
    main()
>>>>>>> 9dfa62cc78bc3f1a37816838a418073e0781f8c3

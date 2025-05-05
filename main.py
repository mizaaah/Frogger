import pygame
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

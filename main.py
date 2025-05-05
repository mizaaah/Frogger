import pygame
from game import Game  # Import de la classe qui sera def dans game.py


def main():
    # Initialisation de pygame
    pygame.init()


    # Initialisation du jeu
    game = Game()
    score = 0  # Initialisation du score


    #Boucle principal du jeu sera ici : 
    
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

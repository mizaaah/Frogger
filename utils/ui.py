import pygame
from config import WHITE

# Dessine un bouton cliquable avec changement de couleur au survol de la souris
def draw_button(surface, text, x, y, w, h, color, hover_color, font):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x < mouse[0] < x + w and y < mouse[1] < y + h:
        pygame.draw.rect(surface, hover_color, (x, y, w, h))
        if click[0]:
            return True
    else:
        pygame.draw.rect(surface, color, (x, y, w, h))
    text_surf = font.render(text, True, (0, 0, 0))
    surface.blit(text_surf, (x + (w - text_surf.get_width()) // 2, y + (h - text_surf.get_height()) // 2))
    return False

# Affiche le score dans le coin supérieur gauche de l'écran
def draw_score(surface, score):
    font = pygame.font.SysFont(None, 30)
    score_text = font.render(f"Score: {score}", True, WHITE)
    surface.blit(score_text, (10, 10))

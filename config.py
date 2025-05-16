import os

# Dossier de base (le dossier où est ce fichier)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Chemins vers les dossiers d'images et sons
IMG_PATH = os.path.join(BASE_DIR, "assets", "IMAGES")
SND_PATH = os.path.join(BASE_DIR, "assets", "SOUNDS")

# Dimensions de la fenêtre
WIDTH, HEIGHT = 600, 700

# Tailles perso et véhicules
FROG_SIZE = 50
CAR_SIZE = (120, 60)
TRUCK_SIZE = (180, 80)

# Voies pour la circulation (position verticale des voies)
LANES_Y = [510, 420, 260, 100]

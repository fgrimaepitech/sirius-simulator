"""
Configuration de la simulation
"""
# --- Config ---
from config.map_config import GRID, get_map_dimensions


GRID_SIZE = GRID['spacing']
TILE_SIZE = 10
SCREEN_WIDTH, SCREEN_HEIGHT = get_map_dimensions()
FPS = 60

# Configuration de la vitesse
SPEED_CONFIG = {
    'min': 0.1,  # 1 tick toutes les 10 secondes
    'max': 10.0,  # 10 ticks par seconde
    'default': 0.1,
    'step': 0.1
}

# Couleurs des entités
ENTITY_COLORS = {
    "empty": (30, 30, 30),
    "cell": (255, 255, 0),
}

# Constantes pour les types d'entités
EMPTY = 0
CELL = 1 
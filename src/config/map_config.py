"""
Configuration de la map pour le simulateur Sirius
"""

# Dimensions de la map
MAP_WIDTH = 1000  # Largeur en pixels
MAP_HEIGHT = 800  # Hauteur en pixels

# Échelle de la map (1 pixel = X mètres)
MAP_SCALE = 1.0  # 1 pixel = 1 mètre

# Couleurs
COLORS = {
    'background': (0, 0, 0),      # Noir
    'grid': (50, 50, 50),         # Gris foncé
    'border': (100, 100, 100),    # Gris moyen
    'text': (255, 255, 255),      # Blanc
}

# Configuration de la grille
GRID = {
    'enabled': True,
    'spacing': 50,  # Espacement entre les lignes de la grille en pixels
    'color': COLORS['grid'],
    'line_width': 1,
}

# Configuration des bordures
BORDER = {
    'enabled': True,
    'color': COLORS['border'],
    'width': 2,
}

# Configuration des marqueurs
MARKERS = {
    'size': 5,  # Taille des marqueurs en pixels
    'color': (255, 0, 0),  # Rouge
}

# Configuration du zoom
ZOOM = {
    'min': 0.1,
    'max': 5.0,
    'default': 1.0,
    'step': 0.1,
}

# Configuration de la caméra
CAMERA = {
    'default_x': MAP_WIDTH // 2,
    'default_y': MAP_HEIGHT // 2,
    'move_speed': 10,  # Pixels par frame
}

# Configuration des unités
UNITS = {
    'default_speed': 1.0,  # mètres par seconde
    'default_size': 10,    # pixels
    'default_color': (255, 255, 0) # jaune pck pourquoi pas
}

def get_map_dimensions():
    """Retourne les dimensions de la map"""
    return MAP_WIDTH, MAP_HEIGHT

def get_map_scale():
    """Retourne l'échelle de la map"""
    return MAP_SCALE

def get_grid_config():
    """Retourne la configuration de la grille"""
    return GRID

def get_camera_config():
    """Retourne la configuration de la caméra"""
    return CAMERA

def get_units_config():
    """Retourne la configuration des unités"""
    return UNITS 
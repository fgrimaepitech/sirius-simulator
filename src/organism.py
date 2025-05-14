import random
from config.map_config import (
    get_map_dimensions,
    get_units_config,
    UNITS
)

# Récupération des dimensions de la map
MAP_WIDTH, MAP_HEIGHT = get_map_dimensions()
GRID_SIZE = MAP_WIDTH // UNITS['default_size']

# Constantes pour les types d'entités
EMPTY = 0
CELL = 1
PLANT = 2
PREDATOR = 3

def random_color():
    """Génère une couleur aléatoire pour les organismes"""
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )

class Organism:
    def __init__(self, x, y, color=None, id="LUCA"):
        self.x = x
        self.y = y
        self.age = 0
        self.energy = 100
        self.reproduction_time = random.randint(20, 100)
        self.id = id
        self.color = color if color else UNITS['default_color']
        self.size = UNITS['default_size']
        self.speed = UNITS['default_speed']

    def update(self, organisms, grid):
        """Met à jour l'état de l'organisme"""
        self.age += 1
        self.energy -= 1  # Consommation d'énergie de base

        # Vérification de la mort
        if self.energy <= 0:
            grid[self.y][self.x] = EMPTY
            organisms.remove(self)
            return

        # Reproduction si conditions remplies
        if self.age >= self.reproduction_time and self.energy >= 50:
            self.reproduce(organisms, grid)

    def reproduce(self, organisms, grid):
        """Crée un nouvel organisme"""
        self.age = 0
        self.energy -= 30  # Coût de reproduction
        self.reproduction_time = random.randint(20, 100)

        # Recherche d'un emplacement vide adjacent
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        random.shuffle(directions)
        
        for dx, dy in directions:
            nx, ny = self.x + dx, self.y + dy
            if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and grid[ny][nx] == EMPTY:
                # Création d'un nouvel organisme avec des caractéristiques légèrement modifiées
                child = Organism(
                    nx, ny,
                    color=self.mutate_color(),
                    id=f"{self.id}_child"
                )
                organisms.append(child)
                grid[ny][nx] = CELL
                break

    def mutate_color(self):
        """Crée une couleur légèrement différente de celle du parent"""
        r, g, b = self.color
        return (
            max(0, min(255, r + random.randint(-20, 20))),
            max(0, min(255, g + random.randint(-20, 20))),
            max(0, min(255, b + random.randint(-20, 20)))
        )

    def move(self, grid):
        """Déplace l'organisme dans une direction aléatoire"""
        if random.random() < self.speed:  # Probabilité de mouvement basée sur la vitesse
            directions = [(0,1), (1,0), (-1,0), (0,-1)]
            random.shuffle(directions)
            
            for dx, dy in directions:
                nx, ny = self.x + dx, self.y + dy
                if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and grid[ny][nx] == EMPTY:
                    grid[self.y][self.x] = EMPTY
                    self.x, self.y = nx, ny
                    grid[ny][nx] = CELL
                    break

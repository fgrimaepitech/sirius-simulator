"""
Classe pour gérer les organismes
"""
import random
import numpy as np
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
    def __init__(self, x, y, color=None, id="LUCA", genealogy_id=None, parent_id=None):
        self.x = x
        self.y = y
        self.age = 0
        self.reproduction_time = random.randint(20, 100)
        self.parent_id = parent_id;
        self.id = id
        self.color = color if color else UNITS['default_color']
        self.size = UNITS['default_size']
        self.speed = UNITS['default_speed']
        self.genealogy_id = genealogy_id  # ID dans l'arbre généalogique

    def update(self, organisms, grid):
        """Met à jour l'état de l'organisme"""
        self.age += 1

        # # Vérification de la mort -> osef pour l'instant
        # if self.energy <= 0:
        #     grid[self.y][self.x] = EMPTY
        #     organisms.remove(self)
        #     return

        # Reproduction si conditions remplies
        if self.age >= self.reproduction_time:
            self.reproduce(organisms, grid)

    def reproduce(self, organisms, grid):
        """Crée un nouvel organisme"""
        self.age = 0
        self.reproduction_time = random.randint(20, 100)

        # Recherche d'un emplacement vide adjacent
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        random.shuffle(directions)
        
        for dx, dy in directions:
            nx, ny = self.x + dx, self.y + dy
            if self.is_valid_position(nx, ny, grid):
                # Création d'un nouvel organisme avec des caractéristiques légèrement modifiées
                child_id = f"{self.id}_child_{len(organisms)}"  # ID unique basé sur le nombre d'organismes
                child = Organism(
                    nx, ny,
                    color=self.mutate_color(),
                    id=child_id,
                    genealogy_id=None,  # Sera défini lors de l'ajout à la généalogie
                    parent_id=self.id
                )
                organisms.append(child)
                grid[ny, nx] = CELL  # Utilisation de la notation numpy
                break

    def mutate_color(self):
        """Crée une couleur légèrement différente de celle du parent"""
        r, g, b = self.color
        return (
            max(0, min(255, r + random.randint(-20, 20))),
            max(0, min(255, g + random.randint(-20, 20))),
            max(0, min(255, b + random.randint(-20, 20)))
        )

    def is_valid_position(self, x, y, grid):
        """Vérifie si une position est valide dans la grille"""
        try:
            return (0 <= x < GRID_SIZE and 
                    0 <= y < GRID_SIZE and 
                    grid[y, x] == EMPTY)  # Utilisation de la notation numpy
        except IndexError:
            return False

    def move(self, grid):
        """Déplace l'organisme dans une direction aléatoire"""
        if random.random() < self.speed:  # Probabilité de mouvement basée sur la vitesse
            directions = [(0,1), (1,0), (-1,0), (0,-1)]
            random.shuffle(directions)
            
            for dx, dy in directions:
                nx, ny = self.x + dx, self.y + dy
                if self.is_valid_position(nx, ny, grid):
                    grid[self.y, self.x] = EMPTY  # Utilisation de la notation numpy
                    self.x, self.y = nx, ny
                    grid[ny, nx] = CELL  # Utilisation de la notation numpy
                    break

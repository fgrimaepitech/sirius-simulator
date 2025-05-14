"""
Simulation principale
"""
import pygame
import numpy as np
import os
from config.map_config import (
    get_map_dimensions,
    get_grid_config,
    COLORS as MAP_COLORS,
    GRID
)
from config.simulation_config import (
    SPEED_CONFIG, ENTITY_COLORS, EMPTY, CELL,
)
from config.ui_config import FONT_PATH, FONTS
from organism import Organism
from ui.ui_manager import UIManager
from config.simulation_config import (
    GRID_SIZE,
    TILE_SIZE,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    FPS
)


def load_font(font_name: str, size: int) -> pygame.font.Font:
    """Charge une police avec gestion des erreurs"""
    try:
        font_path = os.path.join(FONT_PATH, FONTS[font_name])
        return pygame.font.Font(font_path, size)
    except (FileNotFoundError, KeyError):
        print(f"Police {font_name} non trouvée, utilisation de la police par défaut")
        return pygame.font.Font(None, size)


def create_initial_state():
    """Crée l'état initial avec un seul organisme LUCA"""
    grid = [[EMPTY for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    organisms = []
    
    # Création de LUCA au centre de la grille
    center_x = GRID_SIZE // 2
    center_y = GRID_SIZE // 2
    luca = Organism(center_x, center_y, color=(255, 255, 0), id="LUCA")
    organisms.append(luca)
    grid[center_y][center_x] = CELL
  
    return grid, organisms

def draw_button(screen: pygame.Surface, button: dict, mouse_pos: tuple):
    """Dessine un bouton avec effet de survol"""
    color = button['hover_color'] if button['rect'].collidepoint(mouse_pos) else button['color']
    pygame.draw.rect(screen, color, button['rect'])
    pygame.draw.rect(screen, MAP_COLORS['text'], button['rect'], 2)
    
    font = load_font('regular', 16)  # Taille réduite pour la police pixelisée
    text = font.render(button['text'], True, MAP_COLORS['text'])
    text_rect = text.get_rect(center=button['rect'].center)
    screen.blit(text, text_rect)

def run_simulation():
    # Initialisation de la simulation
    grid, organisms = create_initial_state()
    current_speed = SPEED_CONFIG['default']
    tick_counter = 0
    
    # Initialisation de l'interface
    ui_manager = UIManager()
    
    # Boucle principale
    running = True
    clock = pygame.time.Clock()
    
    while running:
        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Gestion des boutons
            button_id = ui_manager.handle_event(event)
            if button_id == 'slow':
                current_speed = max(SPEED_CONFIG['min'], current_speed - SPEED_CONFIG['step'])
            elif button_id == 'fast':
                current_speed = min(SPEED_CONFIG['max'], current_speed + SPEED_CONFIG['step'])
            elif button_id == 'reload':
                grid, organisms = create_initial_state()
                current_speed = SPEED_CONFIG['default']
                tick_counter = 0
            
            # Touche R pour recharger
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                grid, organisms = create_initial_state()
                current_speed = SPEED_CONFIG['default']
                tick_counter = 0
        
        # Mise à jour de la simulation
        tick_counter += current_speed
        if tick_counter >= 1.0:
            tick_counter = 0
            
            # Mise à jour des organismes
            for org in organisms:
                org.update(organisms, grid)
                org.move(grid)  # Ajout du mouvement
        
        # Mise à jour de l'interface
        ui_manager.update_text('title', f"ORGANISMES: {len(organisms)}")
        ui_manager.update_text('speed', f"VITESSE: {current_speed:.1f} ticks/s")
        
        # Dessin
        screen.fill(MAP_COLORS['background'])
        
        # Dessiner la grille
        if GRID['enabled']:
            for x in range(0, SCREEN_WIDTH, GRID['spacing']):
                pygame.draw.line(screen, GRID['color'], (x, 0), (x, SCREEN_HEIGHT), GRID['line_width'])
            for y in range(0, SCREEN_HEIGHT, GRID['spacing']):
                pygame.draw.line(screen, GRID['color'], (0, y), (SCREEN_WIDTH, y), GRID['line_width'])
        
        # Dessiner les organismes
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(screen, ENTITY_COLORS["empty"], rect)
                pygame.draw.rect(screen, MAP_COLORS['grid'], rect, 1)
        
        for org in organisms:
            rect = pygame.Rect(org.x * TILE_SIZE, org.y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(screen, org.color, rect)
        
        # Dessiner l'interface
        ui_manager.draw(screen)
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Simulation de Vie - LUCA")
    run_simulation()

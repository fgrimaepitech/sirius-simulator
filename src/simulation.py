"""
Simulation principale
"""
import pygame
import numpy as np
import os
from config.map_config import (
    get_map_dimensions,
    get_units_config,
    UNITS,
)
from config.simulation_config import ENTITY_COLORS, SPEED_CONFIG
from config.ui_config import BUTTONS, FONTS, FONT_PATH
from organism import Organism, EMPTY, CELL
from data.species.genealogy import Genealogy

# Initialisation de Pygame
pygame.init()

# Récupération des dimensions de la map
MAP_WIDTH, MAP_HEIGHT = get_map_dimensions()
GRID_SIZE = MAP_WIDTH // UNITS['default_size']

# Configuration de la fenêtre
screen = pygame.display.set_mode((MAP_WIDTH, MAP_HEIGHT))
pygame.display.set_caption("Simulation Évolutionnaire")

def load_font(style, size):
    """Charge une police avec gestion d'erreur"""
    try:
        font_path = os.path.join(FONT_PATH, FONTS[style])
        return pygame.font.Font(font_path, size)
    except:
        return pygame.font.Font(None, size)

def draw_button(screen, button_config, mouse_pos):
    """Dessine un bouton avec effet de survol"""
    color = button_config['hover_color'] if button_config['rect'].collidepoint(mouse_pos) else button_config['color']
    pygame.draw.rect(screen, color, button_config['rect'])
    pygame.draw.rect(screen, button_config['border_color'], button_config['rect'], 2)
    
    font = load_font('regular', 16)
    text = font.render(button_config['text'], True, (255, 255, 255))
    text_rect = text.get_rect(center=button_config['rect'].center)
    screen.blit(text, text_rect)

def create_initial_state():
    """Crée l'état initial de la simulation avec LUCA"""
    grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
    organisms = []
    
    # Création de LUCA au centre de la grille
    center_x = GRID_SIZE // 2
    center_y = GRID_SIZE // 2
    luca = Organism(center_x, center_y, id="LUCA", genealogy_id="LUCA")
    organisms.append(luca)
    grid[center_y, center_x] = CELL
    
    return grid, organisms

def reset_simulation():
    """Réinitialise la simulation"""
    return create_initial_state()

def run_simulation():
    """Boucle principale de la simulation"""
    grid, organisms = create_initial_state()
    genealogy = Genealogy()
    genealogy.load_data()
    
    # Ajout de LUCA à la généalogie
    luca = organisms[0]
    genealogy.add_organism(luca, None)
    
    clock = pygame.time.Clock()
    running = True
    current_speed = SPEED_CONFIG['default']
    tick_counter = 0
    is_paused = False

    # supprime les fichiers data
    if os.path.exists(os.path.join('src', 'data', 'species', 'genealogy.json')):
        os.remove(os.path.join('src', 'data', 'species', 'genealogy.json'))
    if os.path.exists(os.path.join('src', 'data', 'species', 'genealogy.dot')):
        os.remove(os.path.join('src', 'data', 'species', 'genealogy.dot'))
    if os.path.exists(os.path.join('src', 'data', 'species', 'genealogy.png')):
        os.remove(os.path.join('src', 'data', 'species', 'genealogy.png'))
    
    while running:
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Gestion des boutons
                for button_id, button_config in BUTTONS.items():
                    if button_config['rect'].collidepoint(mouse_pos):
                        if button_id == 'slow':
                            current_speed = max(SPEED_CONFIG['min'], 
                                             current_speed - SPEED_CONFIG['step'])
                        elif button_id == 'fast':
                            current_speed = min(SPEED_CONFIG['max'], 
                                             current_speed + SPEED_CONFIG['step'])
                        elif button_id == 'reload':
                            grid, organisms = reset_simulation()
                            genealogy = Genealogy()
                            genealogy.load_data()
                            genealogy.add_organism("LUCA", None, "LUCA")
                        elif button_id == 'pause':
                            is_paused = not is_paused
                            button_config['text'] = "RESUME" if is_paused else "PAUSE"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    grid, organisms = reset_simulation()
                    genealogy = Genealogy()
                    genealogy.load_data()
                    genealogy.add_organism("LUCA", None, "LUCA")
                elif event.key == pygame.K_SPACE:
                    is_paused = not is_paused
                    BUTTONS['pause']['text'] = "RESUME" if is_paused else "PAUSE"
        
        # Mise à jour de la simulation
        if not is_paused:
            tick_counter += current_speed
            if tick_counter >= 1:
                tick_counter = 0
                for organism in organisms[:]:
                    organism.move(grid)
                    organism.update(organisms, grid)
                    
                    # Si l'organisme vient de se reproduire, l'ajouter à la généalogie
                    if organism.genealogy_id is None:
                        # Le parent est l'organisme qui vient de se reproduire
                        parent = next((o for o in organisms if o.id == organism.id.split('_')[0] and o.genealogy_id is not None), None)
                        if parent:
                            genealogy.add_organism(organism, parent.id)
                            organism.genealogy_id = organism.id
        
        # Rendu
        screen.fill((0, 0, 0))
        
        # Dessin de la grille
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                color = ENTITY_COLORS["empty"]
                if grid[y, x] == CELL:
                    organism = next((o for o in organisms if o.x == x and o.y == y), None)
                    if organism:
                        color = organism.color
                pygame.draw.rect(screen, color, 
                               (x * UNITS['default_size'], 
                                y * UNITS['default_size'],
                                UNITS['default_size'], 
                                UNITS['default_size']))
        
        # Dessin des boutons
        for button_config in BUTTONS.values():
            draw_button(screen, button_config, mouse_pos)
        
        # Affichage des informations
        font = load_font('regular', 16)
        info_text = [
            f"Organismes: {len(organisms)}",
            f"Vitesse: {current_speed:.1f} ticks/s",
        ]
        
        for i, text in enumerate(info_text):
            text_surface = font.render(text, True, (255, 255, 255))
            screen.blit(text_surface, (10, 10 + i * 25))
        
        pygame.display.flip()
        clock.tick(60)
    
    # Sauvegarde de la généalogie avant de quitter
    genealogy.save_data()
    pygame.quit()

if __name__ == "__main__":
    run_simulation()

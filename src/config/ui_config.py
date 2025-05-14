"""
Configuration de l'UI
"""
import pygame
from config.map_config import COLORS as MAP_COLORS
import os

# Dimensions des boutons
BUTTON_WIDTH = 120
BUTTON_HEIGHT = 40
BUTTON_SPACING = 10

FONT_PATH = os.path.join('src', 'assets', 'fonts')

FONTS = {
    'regular': 'PressStart2P-Regular.ttf',
}

# Création des rectangles pour les boutons
BUTTONS = {
    'slow': {
        'text': "SLOWER",
        'color': (100, 100, 100),
        'hover_color': (150, 150, 150),
        'border_color': MAP_COLORS['text'],
        'position': (10, 50),
        'rect': pygame.Rect(10, 50, BUTTON_WIDTH, BUTTON_HEIGHT)
    },
    'fast': {
        'text': "FASTER",
        'color': (100, 100, 100),
        'hover_color': (150, 150, 150),
        'border_color': MAP_COLORS['text'],
        'position': (10 + BUTTON_WIDTH + BUTTON_SPACING, 50),
        'rect': pygame.Rect(10 + BUTTON_WIDTH + BUTTON_SPACING, 50, BUTTON_WIDTH, BUTTON_HEIGHT)
    },
    'reload': {
        'text': "RELOAD",
        'color': (100, 100, 100),
        'hover_color': (150, 150, 150),
        'border_color': MAP_COLORS['text'],
        'position': (10 + (BUTTON_WIDTH + BUTTON_SPACING) * 2, 50),
        'rect': pygame.Rect(10 + (BUTTON_WIDTH + BUTTON_SPACING) * 2, 50, BUTTON_WIDTH, BUTTON_HEIGHT)
    },
    'pause': {
        'text': "PAUSE",
        'color': (100, 100, 100),
        'hover_color': (150, 150, 150),
        'border_color': MAP_COLORS['text'],
        'position': (10 + (BUTTON_WIDTH + BUTTON_SPACING) * 3, 50),
        'rect': pygame.Rect(10 + (BUTTON_WIDTH + BUTTON_SPACING) * 3, 50, BUTTON_WIDTH, BUTTON_HEIGHT)
    }
}

TEXTS = {
    'title': {
        'text': "ORGANISMES: {}",
        'position': (10, 10),
        'color': MAP_COLORS['text']
    },
    'speed': {
        'text': "VITESSE: {:.1f} ticks/s",
        'position': (10, 100),
        'color': MAP_COLORS['text']
    },
} 
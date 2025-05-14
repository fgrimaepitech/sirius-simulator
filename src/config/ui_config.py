"""
Configuration de l'UI
"""
import pygame
from config.map_config import COLORS as MAP_COLORS
import os


FONT_PATH = os.path.join('src', 'assets', 'fonts')

FONTS = {
    'regular': 'PressStart2P-Regular.ttf',
}

BUTTONS = {
    'slow': {
        'text': "SLOWER",
        'color': (100, 100, 100),
        'hover_color': (150, 150, 150),
        'border_color': MAP_COLORS['text'],
        'position': (10, 50)
    },
    'fast': {
        'text': "FASTER",
        'color': (100, 100, 100),
        'hover_color': (150, 150, 150),
        'border_color': MAP_COLORS['text'],
        'position': (140, 50)
    },
    'reload': {
        'text': "RELOAD",
        'color': (100, 100, 100),
        'hover_color': (150, 150, 150),
        'border_color': MAP_COLORS['text'],
        'position': (270, 50)
    },
    'pause': {
        'text': "PAUSE",
        'color': (100, 100, 100),
        'hover_color': (150, 150, 150),
        'border_color': MAP_COLORS['text'],
        'position': (400, 50)
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
    'status': {
        'text': "STATUS: {}",
        'position': (10, 150),
        'color': MAP_COLORS['text']
    }
} 
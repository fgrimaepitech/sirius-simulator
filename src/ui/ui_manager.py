"""
Gestionnaire de l'interface utilisateur
"""
import pygame
from .button import Button
from .text import Text
from config.ui_config import BUTTONS, TEXTS

class UIManager:
    def __init__(self):
        self.buttons = {}
        self.texts = {}
        self._init_buttons()
        self._init_texts()
    
    def _init_buttons(self):
        """Initialise tous les boutons"""
        for button_id, config in BUTTONS.items():
            self.buttons[button_id] = Button(
                text=config['text'],
                position=config['position'],
                color=config['color'],
                hover_color=config['hover_color'],
                border_color=config['border_color']
            )
    
    def _init_texts(self):
        """Initialise tous les textes"""
        for text_id, config in TEXTS.items():
            self.texts[text_id] = Text(
                text=config['text'],
                position=config['position'],
                color=config['color']
            )
    
    def update_text(self, text_id, new_text):
        """Met à jour un texte spécifique"""
        if text_id in self.texts:
            self.texts[text_id].update_text(new_text)
    
    def handle_event(self, event):
        """Gère les événements pour tous les boutons"""
        for button_id, button in self.buttons.items():
            if button.handle_event(event):
                return button_id
        return None
    
    def draw(self, screen):
        """Dessine tous les éléments de l'interface"""
        # Dessiner les boutons
        for button in self.buttons.values():
            button.draw(screen)
        
        # Dessiner les textes
        for text in self.texts.values():
            text.draw(screen) 
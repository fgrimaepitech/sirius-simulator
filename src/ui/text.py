"""
Classe pour gérer les textes de l'interface
"""
import pygame
import os

class Text:
    def __init__(self, text, position, font_size=16, color=(255, 255, 255)):
        self.text = text
        self.position = position
        self.font_size = font_size
        self.color = color
        
        # Charger la police
        font_path = os.path.join('src', 'assets', 'fonts', 'PressStart2P-Regular.ttf')
        try:
            self.font = pygame.font.Font(font_path, font_size)
        except:
            self.font = pygame.font.SysFont('Arial', font_size)
        
        # Créer la surface du texte
        self.update_text(text)
    
    def update_text(self, new_text):
        """Met à jour le texte affiché"""
        self.text = new_text
        self.text_surface = self.font.render(str(new_text), True, self.color)
    
    def draw(self, screen):
        """Dessine le texte sur l'écran"""
        screen.blit(self.text_surface, self.position) 
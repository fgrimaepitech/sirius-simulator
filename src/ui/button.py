"""
Classe pour gérer les boutons de l'interface
"""
import pygame
import os

class Button:
    def __init__(self, text, position, font_size=16, color=(100, 100, 100), 
                 hover_color=(150, 150, 150), border_color=(255, 255, 255)):
        self.text = text
        self.position = position
        self.font_size = font_size
        self.color = color
        self.hover_color = hover_color
        self.border_color = border_color
        self.is_hovered = False
        
        # Charger la police
        font_path = os.path.join('src', 'assets', 'fonts', 'PressStart2P-Regular.ttf')
        try:
            self.font = pygame.font.Font(font_path, font_size)
        except:
            self.font = pygame.font.SysFont('Arial', font_size)
        
        # Calculer la taille du bouton en fonction du texte
        self.text_surface = self.font.render(text, True, (255, 255, 255))
        self.padding = 10
        self.width = self.text_surface.get_width() + (self.padding * 2)
        self.height = self.text_surface.get_height() + (self.padding * 2)
        
        # Créer le rectangle du bouton
        self.rect = pygame.Rect(position[0], position[1], self.width, self.height)
    
    def draw(self, screen):
        # Dessiner le fond du bouton
        color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(screen, color, self.rect)
        
        # Dessiner la bordure
        pygame.draw.rect(screen, self.border_color, self.rect, 2)
        
        # Centrer le texte dans le bouton
        text_x = self.rect.centerx - self.text_surface.get_width() // 2
        text_y = self.rect.centery - self.text_surface.get_height() // 2
        screen.blit(self.text_surface, (text_x, text_y))
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.is_hovered:
                return True
        return False 
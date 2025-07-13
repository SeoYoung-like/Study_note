import os

import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Alien(Sprite):
    def __init__(self, ai_game: "AlienInvasion"):
        super().__init__()
        self.screen = ai_game.screen

        BASE = os.path.dirname(__file__)
        img_path = os.path.join(BASE, "images", "alien.bmp")
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

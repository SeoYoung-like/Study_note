import os
import pygame
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion 

class Ship:
    """우주선을 관리하는 클래스"""

    def __init__(self, ai_game: "AlienInvasion"):
        """우주선을 초기화하고 시작 위치를 설정합니다"""
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        BASE = os.path.dirname(__file__)
        img_path = os.path.join(BASE, "images", "ship.bmp")
        self.image = pygame.image.load(img_path)
        
        if self.image.get_alpha() is not None:
            self.image = self.image.convert_alpha()
        else:
            self.image = self.image.convert()
            self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        """움직임 플래그를 바탕으로 우주선 위치를 업데이트합니다"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        """우주선을 현재 위치에 그립니다"""
        self.screen.blit(self.image, self.rect)
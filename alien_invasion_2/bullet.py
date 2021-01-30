import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """총알 클래스"""

    def __init__(self, ai_settings, screen, ship):
        """초기화"""
        super().__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)

        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.bullet_speed = ai_settings.bullet_speed_factor

    def update(self):
        """총알 위치를 업데이트 합니다."""
        self.y -= self.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """현재 위치에 총알을 그립니다."""
        pygame.draw.rect(self.screen, self.color, self.rect)
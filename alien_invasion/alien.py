import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """함대에 속한 외계인 하나를 나타내는 클래스"""

    def __init__(self, ai_settings, screen):
        """외계인을 초기화하고 시작 위치를 지정합니다."""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 외계인 이미지를 불러오고 rect 속성을 설정합니다.
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # 새 외계인은 화면 왼쪽 위에서 나타납니다.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 외계인의 정확한 위치를 저장합니다.
        self.x = float(self.rect.x)

    def blitme(self):
        """외계인의 현재 위치에 외계인을 그립니다."""
        self.screen.blit(self.image, self.rect)

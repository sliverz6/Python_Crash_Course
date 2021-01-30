import pygame


class Ship:
    """우주선 클래스"""

    def __init__(self, ai_settings, screen):
        """초기화"""
        self.screen = screen
        self.ai_settings = ai_settings

        # 이미지 불러오기
        self.image = pygame.image.load("images/ship.bmp")
        # rect 만들기
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        # 위치 조정
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        # 이동 플래그
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """우주선의 위치 정보를 업데이트 합니다."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        """우주선의 현재 위치에 우주선을 그립니다."""
        self.screen.blit(self.image, self.rect)

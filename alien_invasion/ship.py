import pygame


class Ship:
    """우주선 클래스"""

    def __init__(self, ai_settings, screen):
        """우주선을 초기화하고 시작 위치를 지정합니다."""
        self.screen = screen  # 화면 객체
        self.ai_settings = ai_settings  # 설정 객체

        # 이미지를 불러옵니다.
        self.image = pygame.image.load("images/ship.bmp")

        # rect 객체를 가져옵니다.
        self.rect = self.image.get_rect()  # 이미지의 rect
        self.screen_rect = self.screen.get_rect()  # 화면 객체의 rect

        # 우주선 위치를 설정합니다.
        self.rect.centerx = self.screen_rect.centerx  # 화면 중앙
        self.rect.bottom = self.screen_rect.bottom  # 화면 아래

        # 우주선 중앙의 가로 좌표를 부동소수점 숫자로 저장합니다.
        self.center = float(self.rect.centerx)

        # 이동 플래그
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """이동 플래그에 따라 위치를 업데이트합니다."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # rect 객체를 self.center에 따라 업데이트합니다.
        self.rect.centerx = self.center

    def blitme(self):
        """우주선의 현재 위치에 우주선을 그립니다."""
        self.screen.blit(self.image, self.rect)

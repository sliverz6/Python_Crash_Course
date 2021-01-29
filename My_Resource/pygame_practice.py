import pygame
import sys


class Ship:
    """우주선 클래스"""
    def __init__(self, settings, screen):
        """초기화"""
        self.screen = screen
        self.settings = settings
        
        # 이미지 불러오기
        self.image = pygame.image.load("ship.bmp")

        # rect 속성 만들기
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # 위치 정하기
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)  # 위치 증감 임시 변수

        # 이동 플래그
        self.moving_right = False
        self.moving_left = False

    def update_position(self):
        """이동 플래그에 따라 우주선의 위치를 수정합니다."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.settings.ship_speed_factor

        self.rect.centerx = self.center

    def draw(self):
        """현재 위치에 우주선을 그립니다."""
        self.screen.blit(self.image, self.rect)


class Bullet:
    """총알 클래스"""
    def __init__(self, settings, screen, ship):
        """초기화"""
        self.screen = screen
        self.color = settings.bullet_color
        self.speed = settings.bullet_speed_factor

        # Rect 생성
        self.rect = pygame.Rect(0, 0, settings.bullet_width,
                                settings.bullet_height)
        # 위치 조절
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

    def moving(self):
        """총알을 발사하는 경로로 움직인다."""
        self.rect.y -= self.speed

    def draw(self):
        """총알의 현재 위치에 총알을 그린다."""
        pygame.draw.rect(self.screen, self.color, self.rect)


class Settings:
    """설정 클래스"""
    def __init__(self):
        """초기화"""
        # 화면 설정
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 우주선 설정
        self.ship_speed_factor = 1.5

        # 총알 설정
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_speed_factor = 1
        self.bullet_allowed = 3


def main():
    """메인 함수"""
    pygame.init()  # 파이게임 초기화
    
    settings = Settings()  # 설정 객체 만들기

    # 화면 객체 만들기
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height)
    )  
    pygame.display.set_caption("Alien Invasion")  # 화면 타이틀 만들기


    ship = Ship(settings, screen)  # 우주선 객체 만들기
    bullets = []

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = True
                elif event.key == pygame.K_SPACE:
                    if len(bullets) < settings.bullet_allowed:
                        new_bullet = Bullet(settings, screen, ship)
                        bullets.append(new_bullet)

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = False

        screen.fill(settings.bg_color)  # 배경 칠하기
        ship.update_position()  # 우주선 위치 업데이트
        for bullet in bullets:  # 총알 위치 업데이트
            bullet.moving()
        
        ship.draw()  # 우주선 그리기
        for bullet in bullets: # 총알 그리기 
            bullet.draw()

        for bullet in bullets.copy():
            if bullet.rect.bottom < 0:
                bullets.remove(bullet)
        
        pygame.display.flip()  # 화면 다시 그리기

main()

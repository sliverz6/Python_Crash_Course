import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group


def run_game():
    pygame.init()  # 파이게임 초기화

    ai_settings = Settings()  # 설정 객체

    screen = pygame.display.set_mode((
        ai_settings.screen_width, ai_settings.screen_height
    ))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings, screen)  # 우주선 객체
    
    bullets = Group()  # 총알 그룹

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)  # 이벤트 탐지
        ship.update()  # 우주선 위치 정보를 업데이트
        gf.update_bullets(bullets)  # 총알 정보를 업데이트
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()

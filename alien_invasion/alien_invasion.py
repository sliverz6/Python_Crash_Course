import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf


def run_game():
    pygame.init()  # 파이게임 초기화
    ai_settings = Settings()  # 게임 설정을 모아둔 객체
    screen = pygame.display.set_mode(  # 화면 생성
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")  # 화면 타이틀 생성

    # 우주선을 만듭니다.
    ship = Ship(ai_settings, screen)
    # 탄환을 저장할 그룹을 만듭니다.
    bullets = Group()
    # 외계인을 만듭니다.
    alien = Alien(ai_settings, screen)

    while True:  # 게임 메인 루프
        gf.check_events(ai_settings, screen, ship, bullets)  # 이벤트 관리
        ship.update()  # 우주선 위치 업데이트
        gf.update_bullets(bullets)  # 탄환 위치 업데이트
        gf.update_screen(ai_settings, screen, ship, alien, bullets)  # 화면 그리기


run_game()


# TODO 1. 화면 만들기
# TODO 2. 우주선 그리기
# TODO 3. 사용자 입력을 받아 우주선 움직이기
# TODO 4. 탄환 발사하기

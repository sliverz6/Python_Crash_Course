import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # 게임을 초기화하고 화면 객체를 만듭니다.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    # 우주선을 만듭니다.
    ship = Ship(ai_settings, screen)
    # 탄환을 저장할 그룹을 만듭니다.
    bullets = Group()
    # 외계인 그룹을 만듭니다.
    aliens = Group()

    # 외계인 함대를 만듭니다.
    gf.create_fleet(ai_settings, screen, aliens)

    # 게임의 메인 루프를 시작합니다.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()

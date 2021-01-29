import sys

import pygame
from bullet import Bullet
from alien import Alien


def fire_bullet(ai_settings, screen, ship, bullets):
    """아직 제한에 걸리지 않았다면 탄환을 발사합니다."""
    # 새 탄환을 만들고 bullets 그룹에 추가합니다.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """키를 누르는 이벤트에 응답합니다."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    """키에서 손을 떼는 이벤트에 응답합니다."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """키보드와 마우스 이벤트에 응답합니다."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """화면에 있는 이미지를 업데이트하고 새 화면에 그립니다."""
    # 루프를 실행할 때마다 화면을 다시 그립니다.
    screen.fill(ai_settings.bg_color)
    # 탄환을 먼저 그립니다.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # 가장 최근에 그린 화면을 표시합니다.
    pygame.display.flip()


def update_bullets(bullets):
    """탄환 위치를 업데이트하고 화면에서 사라진 탄환을 제거합니다."""
    # 탄환 위치를 업데이트합니다.
    bullets.update()

    # 화면에서 사라진 탄환을 제거합니다.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def get_number_alien_x(ai_settings, alien_width):
    """한 줄에 들어갈 외계인 숫자를 계산합니다."""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number):
    """외계인을 만들고 줄 안에 넣습니다."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)


def create_fleet(ai_settings, screen, aliens):
    """외계인 함대 전체를 만듭니다."""
    # 외계인을 하나 만들고 한 줄에 표시할 외계인 숫자를 결정합니다.
    # 외계인 사이의 공간은 외계인 하나가 들어갈 너비입니다.
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_alien_x(ai_settings, alien.rect.width)

    # 외계인 한 줄을 만듭니다.
    for alien_number in range(number_aliens_x):
        create_alien(ai_settings, screen, aliens, alien_number)

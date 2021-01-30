import sys
import pygame

from bullet import Bullet


def fire_bullet(ai_settings, screen, ship, bullets):
    """아직 제한에 걸리지 않았다면 탄환을 발사합니다."""
    # 새 탄환을 만들고 bullets 그룹에 추가합니다.
    if len(bullets) < ai_settings.bullets_allowed:  # 탄환 수가 3 이하라면?
        new_bullet = Bullet(ai_settings, screen, ship)  # 탄환 객체 생성
        bullets.add(new_bullet)  # 탄환 그룹에 추가


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """키를 누르는 이벤트에 응답합니다."""
    if event.key == pygame.K_RIGHT:  # 오른쪽인가?
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:  # 왼쪽인가?
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)  # 탄환 발사
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    """키에서 손을 떼는 이벤트에 응답합니다."""
    if event.key == pygame.K_RIGHT:  # 오른쪽인가?
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:  # 왼쪽인가?
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """키보드와 마우스 이벤트에 응답합니다."""
    for event in pygame.event.get():  # 이벤트 주시
        if event.type == pygame.QUIT:  # 닫기를 눌렀는가?
            sys.exit()  # 프로그램 종료
        elif event.type == pygame.KEYDOWN:  # 키를 눌렀는가?
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:  # 키를 뗐는가?
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, alien, bullets):
    """화면에 있는 이미지를 업데이트하고 새 화면에 그립니다."""
    # 루프를 실행할 때마다 화면을 다시 그립니다.
    screen.fill(ai_settings.bg_color)  # 배경색 채우기
    # 탄환은 우주선이나 외계인보다 먼저 그립니다.
    for bullet in bullets.sprites():  # 탄환 그룹 리스트 반복
        bullet.draw_bullet()
    ship.blitme()  # 우주선 그리기
    alien.blitme()

    # 가장 최근에 그린 화면을 표시합니다.
    pygame.display.flip()  # 화면 그리기


def update_bullets(bullets):
    """탄환 위치를 업데이트하고 화면에서 사라진 탄환을 제거합니다."""
    # 탄환 그룹 위치를 업데이트합니다.
    bullets.update()

    # 화면에서 사라진 탄환을 제거합니다.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

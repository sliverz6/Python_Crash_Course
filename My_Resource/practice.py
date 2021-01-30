import pygame
import sys

from pygame.sprite import Sprite, Group


class Rect():
    def __init__(self, screen, x, y, length, color):
        # super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(x, y, length, length)
        self.color = color

        self.x = float(self.rect.x)

    def update(self):
        self.x += 0.1
        self.rect.x = self.x

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


# 게임 실행 함수
def main():
    pygame.init()  # 설정 초기화
    
    # 화면 만들기
    screen = pygame.display.set_mode((600, 600))
    # 화면 타이틀 만들기
    pygame.display.set_caption("Practice")

    # 배경색
    bg_color = (230, 230, 230)

    # 우주선 이미지 가져오기
    ship = pygame.image.load("ship.bmp")
    # 우주선 이미지 rect 속성 만들기
    ship_rect = ship.get_rect()
    ship_rect.x = 100
    ship_rect.y = 200

    rect_group = Group()

    # 이미지 없이 rect 속성 만들기
    # rect = pygame.Rect(300, 300, 50, 50)
    # rect_color = (50, 50, 250)
    #
    # rect2 = pygame.Rect(200, 200, 50, 50)
    # rect2_color = (250, 50, 50)

    rect1 = Rect(screen, 300, 300, 50, (50, 50, 250))
    rect2 = Rect(screen, 200, 200, 50, (250, 50, 50))

    # rect_group.add(rect1)
    # rect_group.add(rect2)
    
    while True:
        
        for event in pygame.event.get():  # 이벤트 감지
            if event.type == pygame.QUIT:  # 닫기를 클릭했다면?
                sys.exit()  # 프로그램 종료

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ship_rect.x += 20
                elif event.key == pygame.K_LEFT:
                    ship_rect.x -= 20
                elif event.key == pygame.K_SPACE:
                    pass
                    # rect_group.remove(rect1)
                    # rect1.

        # 화면 배경색 칠하기
        screen.fill(bg_color)

        # 우주선 그리기
        screen.blit(ship, ship_rect)

        # rect 위치 업데이트
        # rect_group.update()

        # rect 그리기
        # for rect in rect_group.sprites():
        #     rect.draw()
        rect1.update()
        rect1.draw()

        # 화면 새로 그리기
        pygame.display.update()
    
    
main()

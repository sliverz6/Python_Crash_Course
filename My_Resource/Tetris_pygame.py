import pygame
import sys


data = [
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]   


class Square:
    """사각형 클래스"""
    def __init__(self, screen, x_pos, y_pos, color):
        """초기화"""
        self.screen = screen
        self.length = 25
        self.x = x_pos
        self.y = y_pos
        self.color = color

        self.rect = pygame.Rect(self.x * (self.length + 5),
                                self.y * (self.length + 5),
                                self.length, self.length)

    def draw(self):
        """현재 위치에 사각형을 그린다."""
        pygame.draw.rect(self.screen, self.color, self.rect)


class Block:
    """블록 클래스"""
    def __init__(self):
        """초기화"""
        pass
    

def draw_wall(screen):
    """벽을 그린다."""
    walls = []
    for y in range(21):
        for x in range(12):
            if data[y][x] == 1:
                Square(screen, x, y, "white").draw()


def main():
    """메인 함수"""
    pygame.init()  # 초기화

    screen = pygame.display.set_mode((600, 700))
    pygame.display.set_caption("Tetris")

    draw_wall(screen)  # 벽 그리기 

    while True:
        # 이벤트 탐지
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
        
        pygame.display.flip()  # 화면 그리기

main()

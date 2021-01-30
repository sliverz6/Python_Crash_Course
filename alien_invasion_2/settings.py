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
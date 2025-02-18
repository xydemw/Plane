import pygame
from pygame.sprite import Sprite
import self
class Ship(Sprite):
    """管理⻜船的类"""
    def __init__(self, ai_game):
        """初始化⻜船并设置其初始位置"""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        # 加载⻜船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # 每艘新⻜船都放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom
        # 在⻜船的属性 x 中存储⼀个浮点数
        self.x = float(self.rect.x)
        # 在⻜船的属性 y 中存储⼀个浮点数
        self.y = float(self.rect.y)


        # 移动标志（⻜船⼀开始不移动）
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # 根据 self.x 更新 rect 对象
        self.rect.x = self.x
        # 根据 self.y 更新 rect 对象
        self.rect.y = self.y
    def blitme(self):
        """在指定位置绘制⻜船"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """将⻜船放在屏幕底部的中央"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
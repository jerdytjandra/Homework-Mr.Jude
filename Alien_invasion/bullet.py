import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, setting, ship, screen):
        super(Bullet, self).__init__()
        self.screen = screen

        #initialize the bullet to rect 0,0 and set the width and height
        self.rect = pygame.Rect(0, 0, setting.bullet_width, setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.bottom = ship.rect.top

        self.y = float(self.rect.y)
        self.color = setting.bullet_color
        self.speed = setting.bullet_speed

    def update(self):
        #moving the bullet forward
        self.y -= self.speed
        #changing the bullet's position
        self.rect.y = self.y
        # print(self.rect.y)

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


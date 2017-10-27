import pygame

class Ship():
    def __init__(self, screen, setting):
        self.screen = screen
        self.moving_right = False
        self.moving_left = False
        self.setting = setting

        #Load the image of the ship
        self.image = pygame.image.load("ship.bmp")

        #We would like to have the size of the ship image
        self.rect = self.image.get_rect() #This is the function of the pygame
        self.screen_rect = self.screen.get_rect()


        #Now that we have all of the size ( the screen and the image)
        #We want to set the image of the ship at the center bottom of the ship
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.screen_rect.centerx)
        self.rect.centerx = self.center

    def blitme(self):
        #Now we want to show the image on the screen
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center +=self.setting.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.center -=self.setting.ship_speed

        self.rect.centerx = self.center

    def center_ship(self):
        self.centerx = self.screen_rect.centerx
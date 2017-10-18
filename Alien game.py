import pygame
from setting import Setting
from pygame.sprite import Group
from ship import Ship
from alien import Alien
from game_stats import GameStats
import game_function as gf
from button import Button
from scoreboard import Scoreboard

def run_game():
    pygame.init()
    setting = Setting()
    screen = pygame.display.set_mode([setting.width,setting.height])

    #Now create the object of the ship
    ship = Ship(screen, setting)
    pygame.display.set_caption("Alien Games")

    # Make the Play button
    play_button = Button(setting, screen, "Play")

    #create an instance of gameStats
    stats = GameStats(setting)
    sb = Scoreboard(setting, screen, stats)

    #store a bullet in a list
    bullets = Group()
    aliens = Group()
    gf.create_fleet(setting, screen, aliens, ship)

    while True:
        gf.check_event(setting, screen, stats, play_button, sb, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullet(setting, screen, stats, sb, ship, bullets, aliens)
            gf.update_alien(setting, stats, screen, ship, aliens, bullets)
        gf.update_screen(screen,setting, sb, ship, stats, bullets, aliens, play_button)


run_game()

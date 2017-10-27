import sys
from alien import Alien
import pygame
from time import sleep

from bullet import Bullet


def check_keydown(event, ship, setting, screen, bullets):
    if event.key == pygame.K_d:
        ship.moving_right = True
    elif event.key == pygame.K_a:
        ship.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_SPACE:
       fire_bullet(ship, setting, screen, bullets)

def fire_bullet(ship, setting, screen, bullets):
    if len(bullets) < setting.bullets_allowed:
        new_bullet = Bullet(setting, ship, screen)
        bullets.add(new_bullet)

def update_bullet(setting, screen, stats, sb, ship, bullets, aliens):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_allien_collisions(setting, screen, stats, sb, ship, aliens, bullets)

def check_bullet_allien_collisions(setting, screen, stats, sb, ship, aliens, bullets):
    collision = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collision:
        for aliens in collision.values():
            stats.score += setting.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        bullets.empty()
        setting.increase_speed()
        create_fleet(setting, screen, aliens, ship)

def update_alien(setting, stats, screen, ship, aliens, bullets):
    check_fleet_edges(setting, aliens)
    aliens.update()
    check_aliens_bottom(setting, stats, screen, ship, aliens, bullets)

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(setting, stats, screen, ship, aliens, bullets)

def check_keyup(event, ship):
    if event.key == pygame.K_d:
        ship.moving_right = False
    elif event.key == pygame.K_a:
        ship.moving_left = False

def check_event(setting, screen, stats, play_button, sb, ship, aliens, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown(event, ship, setting, screen, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(setting, screen, stats, play_button, sb, ship, aliens, bullets, mouse_x, mouse_y)

def check_play_button(setting, screen, stats, play_button, sb, ship, aliens, bullets, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        setting.initialize_dynamic_settings()

        pygame.mouse.set_visible(False)

        stats.reset_stats()
        sb.prep_score()
        sb.show_score()

        stats.game_active = True

        aliens.empty()
        bullets.empty()

        create_fleet(setting, screen, aliens, ship)
        ship.center_ship()

def update_screen(screen, setting, sb, ship, stats, bullets, aliens, play_button):
    screen.fill(setting.color)
    ship.blitme()
    aliens.draw(screen)
    for bullet in bullets:
        bullet.draw_bullet()

    sb.show_score()

    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()


def get_number_aliens_x(setting,alien_width):
    available_space = setting.width - (2 * alien_width)
    num_alien_x = int(available_space / (2 * alien_width))
    return num_alien_x

def get_number_rows(setting, ship_height, alien_height):
    available_space_y = setting.height - (3*alien_height) - ship_height
    number_rows = int(available_space_y/(2*alien_height))
    return number_rows

def create_alien(setting, screen, aliens, alien_number, row_number):
    alien = Alien(setting, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number
    aliens.add(alien)

def create_fleet(setting, screen, aliens, ship):
    alien = Alien(setting, screen)
    number_aliens_x = get_number_aliens_x(setting, alien.rect.width)
    for row_number in range(get_number_rows(setting, ship.rect.height, alien.rect.height)):
        for alien_number in range(number_aliens_x):
            create_alien(setting, screen, aliens, alien_number, row_number)

def check_fleet_edges(setting, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(setting, aliens)
            break

def change_fleet_direction(setting, aliens):
    for alien in aliens.sprites():
        alien.rect.y +=setting.drop_speed
    setting.fleet_direction*=-1

def ship_hit(setting, stats, screen, ship, aliens, bullets):
    #Decrement the life of the ship
    if stats.ship_left > 0:
        stats.ship_left-=1
        aliens.empty()
        bullets.empty()
        create_fleet(setting, screen, aliens, ship)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(setting, stats, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom > screen_rect.bottom:
            ship_hit(setting, stats, screen, ship, aliens, bullets)
            break

def check_high_score(stats, sb):
    if stats.score>stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

import pygame
from pygame.sprite import Group
import sys
from settings_game import SettingsGame
import snake_functions as sf
from player_snake import SnakeHead

def run_game():
    fps_clock = pygame.time.Clock()
    ui_settings = SettingsGame()
    pygame.init()
    screen = pygame.display.set_mode((
        ui_settings.screen_width,
        ui_settings.screen_height
    ))

    pygame.display.set_caption("Snake")
    snake = SnakeHead(ui_settings, screen)
    apples = Group()
    sf.loading_apples(ui_settings, screen, apples)

    while True:
        sf.check_control_game(ui_settings, screen, snake, apples)
        sf.check_if_lost_game(ui_settings, snake)

        if ui_settings.status_game:
            snake.update()
            sf.draw_elements(ui_settings, screen, snake, apples)
            sf.update_apples(ui_settings, screen, snake, apples)
            fps_clock.tick(ui_settings.FPS)

run_game()
import pygame
import random
from pygame.sprite import Sprite


class Apple(Sprite):
    def __init__(self, ui_settings, screen):
        super(Apple, self).__init__()

        self.screen = screen
        self.ui_settings = ui_settings
        self.image = pygame.image.load("sprite/apple.bmp")
        self.rect = self.image.get_rect()
        #self.rect = pygame.Rect(0, 0, ui_settings.square_size, ui_settings.square_size)
        self.random_spawn()

        self.color = ui_settings.red_color

    def random_spawn(self):
        y = random.randint(0, self.ui_settings.height_square_number-1) * self.ui_settings.square_size
        x = random.randint(0, self.ui_settings.width_square_number-1) * self.ui_settings.square_size
        self.rect.y = y
        self.rect.x = x

    def draw_apple(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
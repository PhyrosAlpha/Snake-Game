import pygame
import random
from pygame.sprite import Sprite


class SnakeMember(Sprite):
    def __init__(self, ui_settings, screen):
        super().__init__()
        self.screen = screen
        self.ui_settings = ui_settings
        self.rect = pygame.Rect(0, 0, ui_settings.square_size, ui_settings.square_size)
        self.color = ui_settings.blue_color

    def draw_snake(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class SnakeHead(SnakeMember):
    def __init__(self, ui_settings, screen):
        super().__init__(ui_settings, screen)
        self.members = []
        self.random_spawn()
        self.loading_members()
        self.color = ui_settings.white_color
        self.direction = ui_settings.start_direction

    def update(self):
        new_member = SnakeMember(self.ui_settings, self.screen)

        if self.direction == self.ui_settings.up:
            self.rect.y -= self.ui_settings.square_size
            new_member.rect.y = self.rect.y + self.ui_settings.square_size
            new_member.rect.x = self.rect.x

        elif self.direction == self.ui_settings.down:
            self.rect.y += self.ui_settings.square_size
            new_member.rect.y = self.rect.y - self.ui_settings.square_size
            new_member.rect.x = self.rect.x

        elif self.direction == self.ui_settings.right:
            self.rect.x += self.ui_settings.square_size
            new_member.rect.y = self.rect.y
            new_member.rect.x = self.rect.x - self.ui_settings.square_size

        elif self.direction == self.ui_settings.left:
            self.rect.x -= self.ui_settings.square_size
            new_member.rect.y = self.rect.y
            new_member.rect.x = self.rect.x + self.ui_settings.square_size

        self.members.insert(0, new_member)

    def random_spawn(self):
        y = random.randint(0, self.ui_settings.height_square_number-1) * self.ui_settings.square_size
        x = random.randint(0, self.ui_settings.width_square_number-1) * self.ui_settings.square_size
        self.rect.y = y
        self.rect.x = x

    def loading_members(self):
        for member_number in range(0, self.ui_settings.number_members-1):
            member = SnakeMember(self.ui_settings, self.screen)
            member.rect.x = self.rect.x - (member_number + 1) * self.ui_settings.square_size
            member.rect.y = self.rect.y
            self.members.append(member)

    def reset_snake(self):
        self.members = []
        self.random_spawn()
        self.loading_members()
        self.direction = "Right"
import pygame
import sys
from apple import Apple
from player_snake import SnakeHead


def check_control_keydown(ui_settings, screen, event, snake, apples):
    if (event.key == pygame.K_RIGHT) and snake.direction != ui_settings.left:
        snake.direction = ui_settings.right

    elif (event.key == pygame.K_LEFT) and snake.direction != ui_settings.right:
        snake.direction = ui_settings.left

    elif (event.key == pygame.K_UP) and snake.direction != ui_settings.down:
        snake.direction = ui_settings.up

    elif (event.key == pygame.K_DOWN) and snake.direction != ui_settings.up:
        snake.direction = ui_settings.down

    elif (event.key == pygame.K_q) and ui_settings.status_game is False:
        snake.reset_snake()
        apples.empty()
        loading_apples(ui_settings, screen, apples)
        ui_settings.status_game = True


def check_control_game(ui_settings, screen, snake, apples):
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_control_keydown(ui_settings, screen, event, snake, apples)


def draw_screen(settings, screen):
    """It build the game grids on the screen, vertical and horizontal"""
    for vertical_line in range(0,
                               settings.screen_width,
                               settings.square_size):
        pygame.draw.line(screen,
                         settings.black_color,
                         (vertical_line, 0),
                         (vertical_line, settings.screen_height))

    for horizontal_line in range(0,
                                 settings.screen_height,
                                 settings.square_size):
        pygame.draw.line(screen,
                         settings.black_color,
                         (0, horizontal_line),
                         (settings.screen_width, horizontal_line))


def create_apples(ui_settings, screen, apples):
    apple = Apple(ui_settings, screen)
    apples.add(apple)


def loading_apples(ui_settings, screen, apples):
    for apple in range(ui_settings.number_apples):
        create_apples(ui_settings, screen, apples)


def update_apples(ui_settings, screen, snake, apples):
    apple = pygame.sprite.spritecollideany(snake, apples)
    if apple is not None:
        apples.remove(apple)
        create_apples(ui_settings, screen, apples)
        return
    del snake.members[-1]


def collision_wall(ui_settings, snake):
    if snake.rect.x <= -1 or snake.rect.right >= ui_settings.screen_width or snake.rect.y <= -1 or snake.rect.bottom >= ui_settings.screen_height:
        ui_settings.status_game = False


def check_itself_collision(ui_settings, snake):
    for number in range(0, len(snake.members)):
        collision = pygame.sprite.collide_rect(snake, snake.members[number])
        if collision != 0:
            ui_settings.status_game = False
            break


def check_if_lost_game(ui_settings, snake):
    collision_wall(ui_settings, snake)
    check_itself_collision(ui_settings, snake)


def draw_elements(ui_settings, screen, snake, apples):
    screen.fill(ui_settings.green_color)
    snake.draw_snake()
    apples.draw(screen)
    for member in snake.members:
        member.draw_snake()
    draw_screen(ui_settings, screen)
    pygame.display.update()
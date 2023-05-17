import pygame
from pygame.locals import *
import random

# Инициализация Pygame
pygame.init()

# Размеры окна
width = 800
height = 400

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Скорость движения ракеток
PADDLE_SPEED = 5

# Создание окна
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Пинг-понг")

# Создание ракеток
paddle_width = 10
paddle_height = 60
paddle1_x = 20
paddle1_y = height // 2 - paddle_height // 2
paddle2_x = width - paddle_width - 20
paddle2_y = height // 2 - paddle_height // 2

# Создание мяча
ball_radius = 10
ball_x = width // 2
ball_y = height // 2
ball_speed_x = random.choice([-2, 2])
ball_speed_y = random.choice([-2, 2])

# Главный цикл игры
running = True
clock = pygame.time.Clock()
while running:
    clock.tick(60)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Обработка нажатий клавиш
    keys = pygame.key.get_pressed()
    if keys[K_w] and paddle1_y > 0:
        paddle1_y -= PADDLE_SPEED
    if keys[K_s] and paddle1_y < height - paddle_height:
        paddle1_y += PADDLE_SPEED
    if keys[K_UP] and paddle2_y > 0:
        paddle2_y -= PADDLE_SPEED
    if keys[K_DOWN] and paddle2_y < height - paddle_height:
        paddle2_y += PADDLE_SPEED

    # Обновление координат мяча
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Отскок мяча от ракеток
    if ball_x <= paddle1_x + paddle_width and paddle1_y <= ball_y <= paddle1_y + paddle_height:
        ball_speed_x = abs(ball_speed_x)
    if ball_x >= paddle2_x - ball_radius and paddle2_y <= ball_y <= paddle2_y + paddle_height:
        ball_speed_x = -abs(ball_speed_x)

    # Отскок мяча от верхней и нижней стенок
    if ball_y <= 0 or ball_y >= height - ball_radius:
        ball_speed_y = -ball_speed_y

    # Проверка на окончание игры
    if ball_x < 0 or ball_x > width:
        running = False

    # Отрисовка объектов на экране
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (paddle1_x, paddle1_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, WHITE, (paddle2_x, paddle2_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), ball_radius)

    # Обновление экрана
    pygame.display.flip()

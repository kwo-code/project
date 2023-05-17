import pygame
import random

# Инициализация Pygame
pygame.init()

# Размеры окна
width = 800
height = 600

# Создание окна
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Процедурно сгенерированная карта")

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Размер ячейки карты
cell_size = 50

# Создание карты
map_width = width // cell_size
map_height = height // cell_size
map_data = [[random.choice([0, 1]) for _ in range(map_width)] for _ in range(map_height)]

# Позиция игрока
player_x = random.randint(0, map_width - 1)
player_y = random.randint(0, map_height - 1)

# Основной цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обработка клавиш управления
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= 1
    if keys[pygame.K_DOWN] and player_y < map_height - 1:
        player_y += 1
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= 1
    if keys[pygame.K_RIGHT] and player_x < map_width - 1:
        player_x += 1

    # Очистка экрана
    screen.fill(BLACK)

    # Отрисовка карты
    for y in range(map_height):
        for x in range(map_width):
            if map_data[y][x] == 1:
                pygame.draw.rect(screen, GREEN, (x * cell_size, y * cell_size, cell_size, cell_size))

    # Отрисовка игрока
    pygame.draw.rect(screen, WHITE, (player_x * cell_size, player_y * cell_size, cell_size, cell_size))

    # Обновление экрана
    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()

import pygame
import random

# Инициализация Pygame
pygame.init()

# Размеры окна
width = 800
height = 600

# Создание окна
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Задний фон с линиями")

# Создание списка для хранения линий
lines = []

# Определение класса для линий
class Line:
    def __init__(self, x, y, length):
        self.x = x
        self.y = y
        self.length = length
        self.color = (54, 49, 49)
        self.speed = random.randint(1, 3)

    def move(self):
        self.y += self.speed

    def draw(self):
        pygame.draw.line(screen, self.color, (self.x, self.y), (self.x, self.y + self.length), 1)

# Основной цикл программы
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Очистка экрана
    screen.fill((0, 0, 0))

    # Генерация новых линий
    if len(lines) < 50:
        x = random.randint(0, width)
        y = 0
        length = random.randint(100, 200)
        new_line = Line(x, y, length)
        lines.append(new_line)

    # Движение и отрисовка линий
    for line in lines:
        line.move()
        line.draw()

    # Удаление линий, вышедших за пределы экрана
    lines = [line for line in lines if line.y < height]

    # Обновление экрана
    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()

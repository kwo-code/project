import pygame
import random

# Инициализация Pygame
pygame.init()

# Размер окна
width = 800
height = 600

# Создание экрана
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Эффекты частиц")

# Цвета
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

# Класс для представления частицы
class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.size = random.randint(1, 5)
        self.speed_x = random.uniform(-1, 1)
        self.speed_y = random.uniform(-1, 1)

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.size -= 0.1

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.size))

# Создание частиц
particles = []

# Главный цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заливка экрана белым цветом
    screen.fill(WHITE)

    # Создание новых частиц
    mouse_position = pygame.mouse.get_pos()
    particles.append(Particle(mouse_position[0], mouse_position[1], ORANGE))

    # Обновление и отрисовка частиц
    for particle in particles:
        particle.update()
        particle.draw()

    # Удаление старых частиц
    particles = [particle for particle in particles if particle.size > 0]

    # Обновление экрана
    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()
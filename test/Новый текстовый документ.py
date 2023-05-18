import pygame

# Инициализация Pygame
pygame.init()

# Создание экрана
screen = pygame.display.set_mode((640, 480))

# Создание объекта шрифта
font = pygame.font.Font(None, 36)

# Переменные для управления миганием
show_text = True
blink_interval = 500  # Интервал в миллисекундах между сменой видимости текста
last_blink_time = pygame.time.get_ticks()

# Основной игровой цикл
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Очистка экрана
    screen.fill((255, 255, 255))

    # Проверка интервала для мигания текста
    current_time = pygame.time.get_ticks()
    if current_time - last_blink_time >= blink_interval:
        show_text = not show_text  # Инвертируем видимость текста
        last_blink_time = current_time

    # Рисование текста
    if show_text:
        text_surface = font.render("Мигающий текст", True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(320, 240))
        screen.blit(text_surface, text_rect)

    # Обновление экрана
    pygame.display.flip()

# Завершение игры
pygame.quit()
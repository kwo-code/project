import pygame

# Инициализация Pygame
pygame.init()

# Размеры окна
width = 800
height = 600

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Создание окна
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Пример меню")

# Шрифты
font_title = pygame.font.Font(None, 60)
font_options = pygame.font.Font(None, 40)

# Флаг для отображения меню
show_menu = True

# Основной цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if show_menu:
        screen.fill(BLACK)

        # Отрисовка заголовка меню
        title_text = font_title.render("Меню", True, WHITE)
        title_rect = title_text.get_rect(center=(width / 2, height / 4))
        screen.blit(title_text, title_rect)

        # Отрисовка пунктов меню
        option1_text = font_options.render("Начать игру", True, WHITE)
        option1_rect = option1_text.get_rect(center=(width / 2, height / 2))
        screen.blit(option1_text, option1_rect)

        option2_text = font_options.render("Настройки", True, WHITE)
        option2_rect = option2_text.get_rect(center=(width / 2, height / 2 + 50))
        screen.blit(option2_text, option2_rect)

        option3_text = font_options.render("Выйти", True, WHITE)
        option3_rect = option3_text.get_rect(center=(width / 2, height / 2 + 100))
        screen.blit(option3_text, option3_rect)

        # Обработка кликов мыши
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        if option1_rect.collidepoint(mouse_pos) and mouse_click[0] == 1:
            show_menu = False
            # Здесь можно добавить логику для начала игры

        if option2_rect.collidepoint(mouse_pos) and mouse_click[0] == 1:
            show_menu = False
            # Здесь можно добавить логику для открытия настроек

        if option3_rect.collidepoint(mouse_pos) and mouse_click[0] == 1:
            running = False
            # Здесь можно добавить логику для выхода из программы

    else:
        # Здесь можно добавить логику для основной игры или другого экрана

        screen.fill(GREEN)  # Пример: зеленый фон для основной игры

    # Обновление экрана
    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()
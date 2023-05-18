from pygame import *
import random

from data import config as c

init()
font.init()
mixer.init()

display.set_icon(image.load("data/images/ico.bmp"))
display.set_caption(c.caption)

balls = sprite.Group()
particles = []

medium_font  = font.Font('data/fonts/BarcadeBrawlRegular.ttf', 10) 
pause_text   = medium_font.render('press space', True, (c.main_color))

background = transform.scale(image.load('data/images/background.jpg'),(c.screen_w, c.screen_h))
screen = display.set_mode((c.screen_w, c.screen_h))
clock = time.Clock()

show_text = True
blink_interval = 500 
last_blink_time = time.get_ticks()

rebound_1 = mixer.Sound('data/sfx/rebound_1.wav')
rebound_2 = mixer.Sound('data/sfx/rebound_2.wav')
rebound_1.set_volume(0.7)
rebound_2.set_volume(0.6)

class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.size = random.randint(1, 4)
        self.speed_x = random.uniform(-1, 1)
        self.speed_y = random.uniform(-1, 1)

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.size -= 0.1

    def draw(self):
        draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.size))

class GameSprite(sprite.Sprite):
    def __init__(self, image, x, y, speed):
        super().__init__()
        self.image    = image
        self.speed    = speed
        self.rect     = self.image.get_rect()
        self.rect.x   = x
        self.rect.y   = y
    def reset(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Ball(GameSprite):
    def update(self):
        global speed_bonus,p_y_1, p_y_2, rebound_1
        if c.b_left == True and c.pause == False and c.restart == False:
            self.rect.x -= 2+speed_bonus
        if c.b_left == False and c.pause == False and c.restart == False:
            self.rect.x += 2+speed_bonus
        if c.b_up == True and c.pause == False and c.restart == False:
            self.rect.y -= 2+speed_bonus
        if c.b_up == False and c.pause == False and c.restart == False:
            self.rect.y += 2+speed_bonus

        if sprite.spritecollide(player, balls, False):
            c.b_up = True
            speed_bonus += 0.001
            rebound_2.play()
            self.create_particles()
        if sprite.spritecollide(bot, balls, False):
            c.b_up = False
            speed_bonus += 0.001
            rebound_2.play()
            self.create_particles()

        if p_y_2 > (self.rect.x + random.randint(0, 7)) and p_y_2>0 and c.pause == False and self.rect.y < 200:
            p_y_2 -= 2+speed_bonus
        if p_y_2 < (self.rect.x + random.randint(0, 7)) and p_y_2<360 and c.pause == False and self.rect.y < 200:
            p_y_2 += 2+speed_bonus
        if self.rect.x <= 0:
            c.b_left = False
            rebound_1.play()
            self.create_particles()
        if self.rect.x >= c.screen_w-15:
            c.b_left = True
            rebound_1.play()
            self.create_particles()

        if self.rect.y <= 0:
            c.restart = True                
            c.score_2 += 1
        if self.rect.y >= c.screen_h:
            c.restart = True
            c.score_1 += 1
        if c.restart:
            self.rect.x = c.screen_w/2-5
            self.rect.y = c.screen_h/2

    def create_particles(self):
        for x in range(0, random.randint(2, 6)):
                particles.append(Particle(self.rect.x, self.rect.y,c.main_color))

p_y_1,p_y_2 = c.screen_w/2-15,c.screen_w/2-15

ball = balls.add(Ball(transform.scale(image.load('data/images/block.jpg'),(10, 10)), c.screen_w/2-5, c.screen_h/2, 15))

while True:
    player = GameSprite(transform.scale(image.load('data/images/block.jpg'),(35, 5)), p_y_1, c.screen_h-50, 15)
    bot = GameSprite(transform.scale(image.load('data/images/block.jpg'),(35, 5)), p_y_2, 50, 15)

    keys_pressed = key.get_pressed()
    screen.blit(background,(0, 0))
    for e in event.get():
        if e.type == QUIT:
            exit()
        if e.type == KEYDOWN and e.key == K_ESCAPE:
            exit()
        if e.type == KEYDOWN and e.key == K_SPACE:
            if c.pause == False and c.restart == False:
                c.pause = True
            else:
                pause = False
            if c.restart == True:
                c.restart = False

    current_time = time.get_ticks()
    if current_time - last_blink_time >= blink_interval:
        show_text = not show_text  # Инвертируем видимость текста
        last_blink_time = current_time

    if not c.pause:
        balls.update()
    
    if  keys_pressed[K_a] and p_y_1>0 and c.pause == False:
        p_y_1 -= 5+speed_bonus
    if keys_pressed[K_d] and p_y_1<360 and c.pause == False:
        p_y_1 += 5+speed_bonus

    if c.restart:
        c.pause = False
        speed_bonus = 0
        p_y_1,p_y_2 = c.screen_w/2-15,c.screen_w/2-15
        if show_text:
            text_rect = pause_text.get_rect(center=(c.screen_w/2,c.screen_h-25))
            screen.blit(pause_text, text_rect)

    if c.pause:
        if show_text:
            text_rect = pause_text.get_rect(center=(c.screen_w/2,c.screen_h-25))
            screen.blit(pause_text, text_rect)


    statistic = medium_font.render(f'{c.score_1} : {c.score_2}', True, (c.main_color))
    screen.blit(statistic, (20,20))

    for particle in particles:
        particle.update()
        particle.draw()

    particles = [particle for particle in particles if particle.size > 0]

    player.reset()
    bot.reset()
    balls.draw(screen)
    
    display.update()
    clock.tick(c.FPS)
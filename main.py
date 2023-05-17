from pygame import *

display.set_icon(image.load("data/images/ico.bmp"))
display.set_caption('Pin Pong')

init()
font.init()

b_left, b_up = True, True
speed_bonus = 0

balls = sprite.Group()

score_1,score_2 = 0,0
medium_font  = font.Font('data/fonts/BarcadeBrawlRegular.ttf', 10) 
pause_text   = medium_font.render('press space', True, (255,255,255))

screen_w,screen_h = 400,550
background = transform.scale(image.load('data/images/background.jpg'),(screen_w, screen_h))
screen = display.set_mode((screen_w, screen_h))
clock = time.Clock()
FPS = 60

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
        global b_left, b_up, speed_bonus, restart, score_1, score_2, p_y_1, p_y_2
        if b_left == True and pause == False and restart == False:
            self.rect.x -= 2+speed_bonus
        if b_left == False and pause == False and restart == False:
            self.rect.x += 2+speed_bonus
        if b_up == True and pause == False and restart == False:
            self.rect.y -= 2+speed_bonus
        if b_up == False and pause == False and restart == False:
            self.rect.y += 2+speed_bonus
        if sprite.spritecollide(player, balls, False):
            b_up = True
            speed_bonus += 0.001
        if sprite.spritecollide(bot, balls, False):
            b_up = False
            speed_bonus += 0.001
        if p_y_2 > self.rect.x and p_y_2>0 and pause == False and self.rect.y < 200:
            p_y_2 -= 2+speed_bonus
        if p_y_2 < self.rect.x and p_y_2<360 and pause == False and self.rect.y < 200:
            p_y_2 += 2+speed_bonus
        if self.rect.x <= 0:
            b_left = False
        if self.rect.x >= screen_w-15:
            b_left = True
        if self.rect.y <= 0:
            restart = True                
            score_2 += 1
        if self.rect.y >= screen_h:
            restart = True
            score_1 += 1
        if restart:
            self.rect.x = screen_w/2-5
            self.rect.y = screen_h/2

pause,restart = False,True

p_y_1,p_y_2 = screen_w/2-15,screen_w/2-15

ball = balls.add(Ball(transform.scale(image.load('data/images/block.jpg'),(10, 10)), screen_w/2-5, screen_h/2, 15))

while True:
    player = GameSprite(transform.scale(image.load('data/images/block.jpg'),(35, 5)), p_y_1, screen_h-50, 15)
    bot = GameSprite(transform.scale(image.load('data/images/block.jpg'),(35, 5)), p_y_2, 50, 15)

    keys_pressed = key.get_pressed()
    screen.blit(background,(0, 0))
    for e in event.get():
        if e.type == QUIT:
            exit()
        if e.type == KEYDOWN and e.key == K_ESCAPE:
            exit()
        if e.type == KEYDOWN and e.key == K_SPACE:
            if pause == False and restart == False:
                pause = True
            else:
                pause = False
            if restart == True:
                restart = False

    if not pause:
        balls.update()
    
    if  keys_pressed[K_a] and p_y_1>0 and pause == False:
        p_y_1 -= 5+speed_bonus
    if keys_pressed[K_d] and p_y_1<360 and pause == False:
        p_y_1 += 5+speed_bonus

    if restart:
        b_left, b_up = True, False
        pause = False
        speed_bonus = 0
        screen.blit(pause_text, (screen_w/2-55,screen_h-25))
        p_y_1,p_y_2 = screen_w/2-15,screen_w/2-15

    if pause:
        screen.blit(pause_text, (screen_w/2-55,screen_h-25)) 

    statistic = medium_font.render(f'{score_1} : {score_2}', True, (255,255,255))
    screen.blit(statistic, (20,20))

    player.reset()
    bot.reset()
    balls.draw(screen)
    
    display.update()
    clock.tick(FPS)
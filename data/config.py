import random
caption = 'Pin Pong'
FPS = 60
main_color = (255,255,255)
screen_w = 400
screen_h = 550
myappid = "Pin pong"

player1_y = screen_w/2-15
player2_y = screen_w/2-15

ball_speed = 2
ball_x = screen_w/2-5
ball_y = screen_h/2

pause = False
restart = True

speed_bonus = 0
sped_up = 0.01
score_1 = 0
score_2 = 0

b_left = random.choice([True, False])
b_up = random.choice([True, False])

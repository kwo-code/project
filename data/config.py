import random
caption = 'Pin Pong'
FPS = 60
main_color = (255,255,255)
screen_w = 400
screen_h = 550

player1_y = screen_w/2-15
player2_y = screen_w/2-15

ball_x = screen_w/2-5
ball_y = screen_h/2

pause = random.choice([True, False])
restart = random.choice([True, False])

speed_bonus = 0
score_1 = 0
score_2 = 0

b_left = False
b_up = False
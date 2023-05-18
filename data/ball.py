from pygame import *
import random

from .. import main as m
from . import config as c

class Ball(m.GameSprite):
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

        if sprite.spritecollide(m.player, m.balls, False):
            c.b_up = True
            speed_bonus += 0.001
            m.rebound_2.play()
            self.create_particles()
        if sprite.spritecollide(m.bot, m.balls, False):
            c.b_up = False
            speed_bonus += 0.001
            m.rebound_2.play()
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
                m.particles.append(m.Particle(self.rect.x, self.rect.y,c.main_color))

#   have function for drawing background, text, players, and enemys, etc
#   call each functions when needed

import pygame
from pygame import mixer
#from game import Game # import game the object not game the class

# draw score
# draw enemy
# draw player
# refresh background



class Create_Screens(object):
    def __init__(self, width=800, height=600, font_type='assets/FreeSansBold.ttf'):
        self.over_font = pygame.font.Font(font_type, 84)
        self.font = pygame.font.Font(font_type, 28)

    def draw_enemies(screen, enemy_list):
        for enemies in enemy_list: # draws each enemy 
            enemies.draw(screen)

    def draw_lasers(screen, enemy_list):
        for lasers in laser_list: # draws each laser
            lasers.draw(screen)

    
        # draws background and entities!
    def draw_all(self, background, el_player, screen, enemy_list, laser_list):
        screen.blit(background, (0, 0))
        el_player.draw(screen) # draws player using the entity draw method
        #draw_enemies(screen, enemy_list)
        for enemies in enemy_list: # draws each enemy 
            enemies.draw(screen)
        #draw_lasers(screen, laser_list)
        for lasers in laser_list: # draws each laser
            lasers.draw(screen)

    def show_score(self, screen, score_value):
        score = self.font.render("Score :" + str(score_value), True, (255, 255, 255))
        screen.blit(score, (10, 10))


    def scoreboard(self, screen, score_value):
        score = self.font.render("Score :" + str(score_value), True, (255, 255, 255))
        screen.blit(score, (100, 100))
        over_text = self.over_font.render("GAME OVER!", True, (10, 240, 13))
        screen.blit(over_text, (170, 300))
        #score_data = 

print('yay')
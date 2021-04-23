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
    def __init__(self, width=800, height=600, font_type='FreeSansBold.ttf'):
        pass


        # draws background and entities!
    def draw_all(game, background, el_player, screen, enemy_list, laser_list):
        game.screen.blit(background, (0, 0)) # draws screen
        el_player.draw(screen) # draws player using the entity draw method
        for enemies in enemy_list: # draws each enemy 
            enemies.draw(screen)
        for lasers in laser_list: # draws each laser
            lasers.draw(screen)


    def Title_Screen():
        pass
    def Game_Screen():
        #self.draw_all():
        pass
    def GameOver_Screen():
        pass

        # Score
    def Score():
        score_value = 0
        font = pygame.font.Font('FreeSansBold.ttf', 28)
        textX = 10
        textY = 10

        # Game Over Text
    def GameOver():
        self.over_font = pygame.font.Font('FreeSansBold', 84)

    def show_score(x, y):
        score = font.render("Score :" + str(score_value), True, (255, 255, 255))
        screen.blit(score, (x, y))

    def game_over_text():
        over_text = over_font.render("GAME OVER!", True, (10, 240, 13))
        screen.blit(over_text, (170, 300))


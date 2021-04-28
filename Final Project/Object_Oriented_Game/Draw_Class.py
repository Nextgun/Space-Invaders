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
    def __init__(self, width=800, height=600):
        pygame.init()

        #screen and background and font
        screen = pygame.display.set_mode((width, height))
        self.background = pygame.image.load('assets/spacebg.png')
        self.font = pygame.font.Font('assets/FreeSansBold.ttf', 28)

        # Background Sound
        mixer.music.load('assets/background.wav')
        mixer.music.set_volume(0.04)
        mixer.music.play(-1)

        # Changes the Title and Icon
        pygame.display.set_caption("Group's Space Invaders")
        icon = pygame.image.load('assets/alien.png')
        pygame.display.set_icon(icon)



        # draws background and entities!
    def draw_all( el_player, el_enemy_list, el_laser_list):
        bg = pygame.image.load('assets/spacebg.png')
        sc = pygame.display.set_mode((800, 600))
        sc.blit(bg , (0, 0)) # draws screen
        el_player.draw(sc) # draws player using the entity draw method
        for enemies in el_enemy_list: # draws each enemy 
            enemies.draw(sc)
        for lasers in el_laser_list: # draws each laser
            lasers.draw(sc)


    def Title_Screen():
        pass
    def Game_Screen():
        #self.draw_all():
        pass
    def GameOver_Screen():
        pass

        # Score
    def Draw_Score(Font ):
        screen.blit(Font).render(("i just did this!", True, (255, 0, 0)), (180,350))


        pass
        #score_value = 0
        #font = pygame.font.Font('FreeSansBold.ttf', 28)
        #textX = 10
        #textY = 10



        # Game Over Text
    def GameOver():
        self.over_font = pygame.font.Font('FreeSansBold', 84)

    def show_score(x, y):
        score = font.render("Score :" + str(score_value), True, (255, 255, 255))
        screen.blit(score, (x, y))

    def game_over_text():
        over_text = over_font.render("GAME OVER!", True, (10, 240, 13))
        screen.blit(over_text, (170, 300))


print("yellow")
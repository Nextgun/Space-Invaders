#   have function for drawing background, text, players, and enemys, etc
#   call each functions when needed

import pygame
from pygame import mixer
pygame.font.init()
#from game import Game # import game the object not game the class

# draw score
# draw enemy
# draw player
# refresh background



class Create_Screens(object):
    def __init__(self, width=800, height=600):
        self.over_font = pygame.font.Font('assets/FreeSansBold.ttf', 84)
        self.font = pygame.font.Font('assets/FreeSansBold.ttf', 28)
        self.width = 800
        self.height = 600

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


    def end_screen(self, background, screen, score_value):
        screen.blit(background, (0, 0))
        x = self.width * 0.16666667
        y = self.height * 0.16666667
        over_text = self.over_font.render("GAME OVER!", True, (10, 240, 13))
        screen.blit(over_text, (x, y))

    def add_score(self, name, score): # here i need to write new score into files
        new_score = name + " " + str(score) 
        f = open("Score_info", "a") # opens file that contains name and score data
        f.write(new_score +"                                                                                                                                                                  "+ "\n")
        f.close()

        f = open("Just_score", "a") # opens file that contains score data
        f.write(str(score) + "\n")
        f.close()

    def scoreboard(self, screen, score_value): 
        x = self.width * 0.015625
        y = self.height * 0.33333333
        open_file = open("Score_info",'r')
        for score in open_file:
            score_text = self.font.render(score, True, (255, 255, 255))
            screen.blit(score_text, (x, y))
            y = y + 30 

    def average(self, screen):
        open_file = open("Just_score", 'r')
        ScoresList = []
        for score in open_file:
            ScoresList.append(int(score))
        # write code to calculate average
        Average = sum(ScoresList) / len(ScoresList)
        int(Average)
        x = self.width * 0.015625
        y = self.height * 0.015625
        text = self.font.render("Average Score: " + str(Average), True, (255, 255, 255))
        screen.blit(text, (x,y+30))


    def sumOfEnemies(self, screen, enemyKilled):
        sum = 0
        for enemy in enemyKilled:
            sum = sum + enemy
        # write code to draw amount of enemies killed
        x = self.width * 0.015625
        y = self.height * 0.015625
        text = self.font.render("Number of Enemies Killed: " + str(sum), True, (255, 255, 255))
        screen.blit(text, (x,y))





print('yay') 

# figure out hidden character in the scoreinfo file 4/30/21 - c 
# 
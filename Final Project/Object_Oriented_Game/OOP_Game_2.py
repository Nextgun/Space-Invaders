import Entity_Class
import pygame
import random
import math
from pygame import mixer

class Game:
    def __init__(self):
        pygame.init()

        #screen and background and font
        self.screen = pygame.display.set_mode((800, 600))
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

        #object creation
        self.player1 = Entity_Class.Player(370, 480)
        self.enemy_Ties = []
        self.enemy_creation()
        self.laser_list = []
        #self.laser1 = Entity_Class.Laser(self.player1.entityX, self.player1.entityY)
        
        self.run = True # bool for main loop to start
        
        self.mainLoop() # runs the main loop function

    # draws background and entities!
    def draw(self):
        self.screen.blit(self.background, (0, 0)) # draws screen
        self.player1.draw(self.screen) # draws player using the entity draw method
        for enemies in self.enemy_Ties: # draws each enemy 
            enemies.draw(self.screen)
        for lasers in self.laser_list: # draws each laser
            lasers.draw(self.screen)
        #self.laser1.laser_draw(self.screen)
        #self.laser2.draw(self.screen)
        

    # checks for the keypresses
    def event_manager(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player1.entityX_change = -0.3
                if event.key == pygame.K_RIGHT:
                    self.player1.entityX_change = 0.3
                if event.key == pygame.K_UP:
                    self.player1.entityY_change = -0.3
                if event.key == pygame.K_DOWN:
                    self.player1.entityY_change = 0.3
                if event.key == pygame.K_SPACE:
                    self.laser_list.append(Entity_Class.Laser(self.player1.entityX, self.player1.entityY))                    #self.laser2 = Entity_Class.Laser(self.player1.entityX,self.player1.entityY)
                     
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player1.entityX_change = 0
                if event.key == pygame.K_RIGHT:
                    self.player1.entityX_change = 0
                if event.key == pygame.K_UP:
                    self.player1.entityY_change = 0
                if event.key == pygame.K_DOWN:
                    self.player1.entityY_change = 0

    def update_Movement(self):
        self.player1.movement() # updates player movement
        for enemies in self.enemy_Ties: # updates enemy movement for each enemy
            enemies.enemy_movement()
        for lasers in self.laser_list:
            lasers.laser_draw(self.screen)
        #self.laser1.laser_move()

            
    def mainLoop(self):
        while self.run:
            self.draw()
            self.event_manager()
            self.update_Movement()
            pygame.display.flip()
        pygame.quit()


    def enemy_creation(self):
        for i in range(12):
            self.enemy_Ties.append(Entity_Class.Enemy(random.randint(0, 735), random.randint(50, 150)))
            




#creates obj of class to run game
if __name__ == "__main__":
    game = Game()

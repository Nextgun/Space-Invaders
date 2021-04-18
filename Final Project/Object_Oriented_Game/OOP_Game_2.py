import Entity_Class
import pygame
import random
import math
from pygame import mixer

class final_project:
    def __init__(self):
        pygame.init()

        #screen and background
        self.screen = pygame.display.set_mode((800, 600))
        self.background = pygame.image.load('assets/spacebg.png')

        # Background Sound
        mixer.music.load('assets/background.wav')
        mixer.music.set_volume(0.04)
        mixer.music.play(-1)

        # Changes the Title and Icon
        pygame.display.set_caption("Group's Space Invaders")
        icon = pygame.image.load('assets/alien.png')
        pygame.display.set_icon(icon)


        #object creation
        self.player = Entity_Class.Player(370, 480)
        self.enemy_Ties = []
        self.enemy_creation()
        #bool for main loop
        self.run = True

        #runs the main loop function
        self.mainLoop()


    def mainLoop(self):
        while self.run:
            self.draw()
            self.event_manager()
            self.update_Movement()
            pygame.display.flip()
        pygame.quit()

    def enemy_creation(self):
        for i in range(6):
            self.enemy_Ties.append(Entity_Class.Enemy(random.randint(0, 735), random.randint(50, 150)))
            




    def update_Movement(self):
        self.player.movement()
        for x in self.enemy_Ties:
            x.enemy_movement()



    #draws background and entities!
    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.player.draw(self.screen)
        for x in self.enemy_Ties:
            x.draw(self.screen)

    #checks for the keypresses
    def event_manager(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.entityX_change = -0.3
                if event.key == pygame.K_RIGHT:
                    self.player.entityX_change = 0.3
                if event.key == pygame.K_UP:
                    self.player.entityY_change = -0.3
                if event.key == pygame.K_DOWN:
                    self.player.entityY_change = 0.3
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player.entityX_change = 0
                if event.key == pygame.K_RIGHT:
                    self.player.entityX_change = 0
                if event.key == pygame.K_UP:
                    self.player.entityY_change = 0
                if event.key == pygame.K_DOWN:
                    self.player.entityY_change = 0


#creates obj of class to run game
if __name__ == "__main__":
    game = final_project()


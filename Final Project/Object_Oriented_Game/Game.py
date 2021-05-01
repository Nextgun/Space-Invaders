import Entity_Class
import pygame
import random
from pygame import mixer
from Draw_Class import Create_Screens 
import easygui

# todo list
# music not working come back later
#
# need to create different "screens" to draw, and change screens depending on game state
# i.e. game over = screen3, game = screen2, title screen = screen1


# do while # do the gaem loop # while the character is alive
# enemies killed # sum number of enemies
# average the scores

#  game class should hold all the game logic,
#   ie spawing enemies etc, movement checks, no drawing
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
        self.score = 0
        self.player_name = "default"

        self.player_list = [] # i want to throw players in a list as well, to have players 1, 2, 3, 4
        self.player1 = Entity_Class.Player(370, 480)
        self.enemy_list = []
        self.laser_list = []
        self.draw_stuff = Create_Screens()

        self.movement_list = [False, False, False, False] # [left, right, up, down] if true move in direction :)
        self.player_speed = 1.5
        self.enemy_speed = 0.3

        self.playingGame = True # bool for main loop to start
        self.GameOver = False

        self.laser_state = True
        
        self.mainLoop() # runs the main loop function

    
    def read_file(self):
        # read a file into the game
        list = []
        pass
   
    def write_file(self):
        # write the new score into file
        pass
        
        
    # trying to get a delay to work for laser
    def thelaserstate(self):
        laser_state = True
    
    # checks for the keypresses
    def event_manager(self):
        # trying to get a delay to work for laser
        laser_state = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.GameOver = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.movement_list[0] = True
                if event.key == pygame.K_RIGHT:
                    self.movement_list[1] = True
                if event.key == pygame.K_UP:
                    self.movement_list[2] = True
                if event.key == pygame.K_DOWN:
                    self.movement_list[3] = True
                if event.key == pygame.K_SPACE:
                    
                    self.laser_list.append(Entity_Class.Laser(self.player1.entityX, self.player1.entityY))

                    # i want to cry
                    #if laser_state == True:
                        #(self.laser_list.append(Entity_Class.Laser(self.player1.entityX, self.player1.entityY)))
                        #laser_state = False
                        #L = Timer(2.0,thelaserstate)              
                        #L.start() # want to add delay between laser to prevent spam, but delays whole game
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.movement_list[0] = False
                if event.key == pygame.K_RIGHT:
                    self.movement_list[1] = False
                if event.key == pygame.K_UP:
                    self.movement_list[2] = False
                if event.key == pygame.K_DOWN:
                    self.movement_list[3] = False
           

    def update_Movement(self):
        #fixed movement bug, pretty ugly code tho..
        if self.movement_list[0]:
            self.player1.entityX_change = -self.player_speed
        elif not self.movement_list[0]:
            self.player1.entityX_change = 0

        if self.movement_list[1]:
            self.player1.entityX_change = self.player_speed
        elif not self.movement_list[1] and not self.movement_list[0]:
            self.player1.entityX_change = 0

        if self.movement_list[0] and self.movement_list[1]:
            self.player1.entityX_change = 0

        if self.movement_list[2]:
            self.player1.entityY_change = -self.player_speed
        elif not self.movement_list[2]:
            self.player1.entityY_change = 0

        if self.movement_list[3]:
            self.player1.entityY_change = self.player_speed
        elif not self.movement_list[3] and not self.movement_list[2]:
            self.player1.entityY_change = 0

        if self.movement_list[2] and self.movement_list[3]:
            self.player1.entityY_change = 0

        self.player1.movement() # updates player movement
        for enemies in self.enemy_list: # updates enemy movement for each enemy
            enemies.enemy_movement()
        for lasers in self.laser_list:
            lasers.laser_move()

    def collision_detection(self):
        for The_enemy in self.enemy_list:
            for The_laser in self.laser_list:
                if The_enemy in self.enemy_list: # check in the enemy exists in enemy list
                    if (The_enemy.detect_collision(The_laser)):
                        self.enemy_list.remove(The_enemy)
                        self.laser_list.remove(The_laser)
                        self.score = self.score + 1 
        for The_enemy in self.enemy_list: 
            if The_enemy.detect_collision(self.player1): 
                self.game_over()


        
        
    def game_over(self):
        print("you lose")
        print(self.score)
        self.GameOver = True
        
    def draw_everything(self):
        self.draw_stuff.draw_all(self.background, self.player1, self.screen, self.enemy_list, self.laser_list)
        self.draw_stuff.show_score(self.screen, self.score)

    def enemy_creation(self):
        if not self.enemy_list:
            for i in range(12):
                self.enemy_list.append(Entity_Class.Enemy(random.randint(0, 735), random.randint(50, 150), self.enemy_speed))
            self.enemy_speed += 0.1
            
    def mainLoop(self):
        while self.playingGame == True:
            if self.GameOver == False:
                if self.player_name == "default":
                    self.player_name = easygui.enterbox("Enter player name: ")
                
                 
                self.collision_detection()
                self.draw_everything()
                self.event_manager()
                self.update_Movement()
            
                if not self.enemy_list: # checks if enemy list is empty
                    # write some code here to either spawn more enemies or make them harder to kill or both.
                    self.enemy_creation() # creates new enemies
                for The_laser in self.laser_list:
                    if The_laser.entityY < 0:
                        self.laser_list.remove(The_laser)

                pygame.display.flip()

            if self.GameOver == True: 
                self.draw_stuff.add_score (self.player_name, self.score)  # write new score into score info 
                self.event_manager()
                self.draw_everything()
                self.draw_stuff.end_screen(self.background, self.screen, self.score)
                self.draw_stuff.scoreboard(self.screen, self.score)
                pygame.display.flip()
        pygame.quit()

            
#creates obj of class to run game
if __name__ == "__main__":
    game1 = Game()

   # the_game  = idk


# while
#   title screen code
#   if player presses play
#       break out of loop
    def Title_Screen():
        pass

# while game == play
#   game loop
#   if game == over
#       break


#       write score into score data




# while game == over
#   draw "you lose"
#   "your score was ", score
#   leaderboard is 
#   l = open()
#   for score in l:
#       print(score)
#   highscore is
#   print(highscore)
    def GameOver_Screen():
        pass



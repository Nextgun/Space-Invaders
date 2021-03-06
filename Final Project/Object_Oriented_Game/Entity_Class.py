import pygame
#from game import *

#   this code is working
#   but i need to check the logic for it

# use to create sub-classes in player and enemy

class Entity(object):
    # 8. Use parameters in functions. 
    def __init__(self, entityX, entityY, image, health,  entityX_change, entityY_change, size): #   all of the attributes for entities
        self.image = pygame.image.load(image)
        self.health = health
        self.entityX = entityX
        self.entityY = entityY
        self.entityX_change = entityX_change
        self.entityY_change = entityY_change
        self.size = size

        # 7 Create different types of functions.  void or return value
        # returns boolean value of true or false
    def detect_collision(self, other): 
        if (other.entityX >= self.entityX and other.entityX < (self.entityX + self.size)) or (self.entityX >= other.entityX and self.entityX < (other.entityX + other.size)):
            if (other.entityY >= self.entityY and other.entityY < (self.entityY + self.size)) or (self.entityY >= other.entityY and self.entityY < (other.entityY +other.size)):
                return True
        return False
    
    def enemy_movement(self): # moves enemies
        self.entityX += self.entityX_change
        if self.entityX <= 0:
            self.entityX_change *= -1
            self.entityY += self.entityY_change
        if self.entityX >= 736:
            self.entityX_change *= -1
            self.entityY += self.entityY_change

    def draw(self, screen):
        screen.blit(self.image, (self.entityX, self.entityY)) # draws our entity

#   player is a subclass of the entity class
class Player(Entity):
    #   initializes the player, and player number
    def __init__(self, entityX, entityY): 
        #   initializes the entity attributes
        super().__init__(entityX, entityY, image='assets/plane.png', health=3,  entityX_change=0, entityY_change=0, size=30)
        
    def movement(self): # moves player
        if self.entityX + self.entityX_change <= 0:
            self.entityX == 0
        elif self.entityX + self.entityX_change >= 736:
            self.entityX == 736
        else:
            self.entityX += self.entityX_change

        if self.entityY + self.entityY_change <= 0:
            self.entityY == 0
        elif self.entityY + self.entityY_change + self.image.get_height() >= 600:
            self.entityY == 600
        else:
            self.entityY += self.entityY_change

class Enemy(Entity):
    def __init__(self, entityX, entityY, enemy_speed): 
        #   initializes the entity attributes
        Entity.__init__(self, entityX, entityY, image='assets/tie.png', health=1,  entityX_change=enemy_speed, entityY_change=20, size=50)

class Laser(Entity):
    def __init__(self, entityX, entityY):
        super().__init__(entityX, entityY, image='assets/laser.png', health=0, entityX_change=0, entityY_change=1, size=25)
        self.laser_state = True
        
    def laser_draw(self, screen):
        screen.blit(self.image, (self.entityX, self.entityY))

    def laser_move(self):
        self.entityY -= self.entityY_change
        
   
            
    
        

print("i worked")

                       
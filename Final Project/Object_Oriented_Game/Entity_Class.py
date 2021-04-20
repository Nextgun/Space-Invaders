import pygame
from OOP_Game_2 import Game

#   this code is working
#   but i need to check the logic for it

# use to create sub-classes in player and enemy

class Entity(object):
    def __init__(self, entityX, entityY, image, health,  entityX_change, entityY_change, size): #   all of the attributes for entities
        self.image = pygame.image.load(image)
        self.health = health
        self.entityX = entityX
        self.entityY = entityY
        self.entityX_change = entityX_change
        self.entityY_change = entityY_change
        self.size = size

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
        self.entityX += self.entityX_change
        self.entityY += self.entityY_change

class Enemy(Entity):
    def __init__(self, entityX, entityY): 
        #   initializes the entity attributes
        Entity.__init__(self, entityX, entityY, image='assets/tie.png', health=1,  entityX_change=0.3, entityY_change=20, size=50)

class Laser(Entity):
    def __init__(self, entityX, entityY):
        super().__init__(entityX, entityY, image='assets/laser.png', health=0, entityX_change=0, entityY_change=1, size=25)
        self.laser_state = True
        
    def laser_draw(self, screen):
        screen.blit(self.image, (self.entityX, self.entityY))

    def laser_move(self):
        self.entityY -= self.entityY_change

    def shoot_laser(self, playerX, playerY):
        self.laser1.shoot_laser(self.player1.entityX, self.player1.entityY)
        pass
            
    
    # if laser collides with enemy = pop enemy from enemylist 
    # (enemy = self, laser (laser is now a list of many lasers) = other)
    # 
    # if enemy collides with player = game over                 
    # (enemy = self, player = other)
        

print("i worked")

                       
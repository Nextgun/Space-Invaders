import pygame
#   this code is working
#   but i need to check the logic for it

# use to create sub-classes in player and enemy

class Entity(object):
    def __init__(self, image, health, entityX, entityY, entityX_change, entityY_change, size): #   all of the attributes for entities
        self.image = pygame.image.load(image)
        self.health = health
        self.entityX = entityX
        self.entityY = entityY
        self.entityX_change = entityX_change
        self.entityY_change = entityY_change
        self.size = size

    #    return super().__init__(*args, **kwargs)
    def detect_collision(self, other):
        if (other.entityX >= self.entityX and other.entityX < (self.entityX + self.size)) or (self.entityX >= other.entityX and self.entityX < (other.entityX + other.size)):
            if (other.entityY >= self.entityY and other.entityY < (self.entityY + self.size)) or (self.entityY >= other.entityY and self.entityY < (other.entityY +other.size)):
                return True
        return False
    
    def movement(self):
        self.entityX += self.entityX_change
        self.entityY += self.entityY_change

    def enemy_movement(self):
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
    def __init__(self, entityX, entityY): # *args, **kwargs):
        #   initializes the entity attributes
        super().__init__('assets/plane.png', 3, entityX, entityY, 0, 0, 30)

class Enemy(Entity):
    def __init__(self, entityX, entityY, *args,  **kwargs):
        #   initializes the entity attributes
        Entity.__init__(self, 'assets/tie.png', 1, entityX, entityY, 0.3, 20, 50)


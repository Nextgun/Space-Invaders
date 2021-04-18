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

    def draw(self, screen):
        screen.blit(self.image, self.entityX, self.entityY) # draws our entity

    def laser():
        # create function to fire laser
        # Ready - you cant see the laser on the screen
        # Fire - the laser is currently moving

        # make laser have its own hit box using the collision function
        laserImg = pygame.image.load('laser.png')
        laserX = 0
        laserY = 480
        laserX_change = 0
        laserY_change = .5
        
                #   laser state is for the player
                def PlayerLaser(self):
                    self.laser_state = "ready"
                    return self.laser_state
                
                def fire_laser(x, y):   #   fire laser for player using laser state
                    global laser_state
                    laser_state = "fire"
                    screen.blit(laserImg, (x + 16, y + 10))

        #   this code is working
#   but i need to check the logic for it

#   player is a subclass of the entity class
class Player(Entity):
    #   initializes the player, and player number
    def __init__(self, entityX, entityY): # *args, **kwargs):
        #   initializes the entity attributes
        super().__init__(self, 'plane.png', health=3, entityX, entityY, entityX_change=0, entityY_change=0, size=30)
        # Checking player boundaries
        entityX += entityX_change
        entityY += entityY_change
        
        if entityX <= 0:        entityX = 0
        elif entityX >= 736:    entityX = 736
        if entityY <= 0:        entityY = 0
        elif entityY >= 536:    entityY = 536
    
    #   something
    def SpawnPlayer():
        #   add code here that spawns the players in
        pass

#   list with the arguments to be passed to the player class
player_info = [370, 480]





class Enemy(Entity):
    def __init__(self, entityX, entityY, *args,  **kwargs):
        #   initializes the entity attributes
        Entity.__init__(self, 'tie.png', health=1, entityX, entityY, entityX_change=0, entityY_change=0, size=50)
        # Enemy
        tieImg = []
        tieX = []
        tieY = []
        tieX_change = []
        tieY_change = []
        num_of_tie = 6
    
    # not sure what this code does
    #
    # return super().__init__(*args, **kwargs)
    #

    def SpawnEnemy():
        #   write code that spawns the enemies in
        pass

#   old code for spawning enemies, rewrite in class
#
##how the enemy spawns
#for i in range(num_of_tie):
#    tieImg.append(pygame.image.load('tie.png'))
#    tieX.append(random.randint(0, 735))  # had enemy tie randomly spawn in different places on the x axis
#    tieY.append(random.randint(50,
#                               150))  # had enemy tie randomly spawn in different places on the y axis between set parameters
#    tieX_change.append(0.3)
#    tieY_change.append(20)
print("it worked")

enemy_info = [370, 180]

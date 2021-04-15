import pygame



#
#   this code is working
#   but i need to check the logic for it
#




# entitys will have collision
# use to create sub-classes in player and enemy


class Entity(object):

    #   all of the attributes for entities
    def __init__(self, image, health, entityX, entityY, 
                 entityX_change, entityY_change):
        self.image = pygame.image.load(image)
        self.health = health
        self.entityX = entityX
        self.entityY = entityY
        self.entityX_change = entityX_change
        self.entityY_change = entityY_change






 #       return super().__init__(*args, **kwargs)
    def Collision():
        def isCollision(tieX, tieY, laserX, laserY):
            distance = math.sqrt(math.pow(tieX - laserX, 2) + (math.pow(tieY - laserY, 2)))  # Distance Formula = square root of (x2-x1)^2 + (y2-y1)^2
            if distance < 30:
                return True
            else:
                return False


        def collide(tieX, tieY, playerX, playerY):
            player_distance = math.sqrt(math.pow(tieX - playerX, 2) + (math.pow(tieY - playerY, 2)))
            if player_distance < 30:
                return True
            else:
                return False
                pass

    def laser():
        # Laser
        # create function to fire laser
        # Ready - you cant see the laser on the screen
        # Fire - the laser is currently moving
        #
        # make laser have its own hit box using the collision function
        laserImg = pygame.image.load('laser.png')
        laserX = 0
        laserY = 480
        laserX_change = 0
        laserY_change = .5

   


        #**************************************#
        #                                      #
        #   rewrite to draw the entity         #
        #                                      #
        #**************************************#
#def DrawPlayer(x, y):
#    screen.blit(playerImg, (x, y))  # draws the player at set coord


def tie(x, y, i):
    screen.blit(tieImg[i], (x, y))  # draws the enemy at set coord


    pass



        #**************************************#
        #                                      #
        #   rewrite collision for entity that  #
        #    works with enemy and player       #
        #                                      #
        #**************************************#






print ("i work")
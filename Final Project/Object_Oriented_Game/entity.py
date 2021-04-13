# entitys will have collision
# use to create sub-classes in player and enemy


class entity(object):
    def __init__(self, image, health, entityX, entityY, entityX_change, entityY_change, *args, **kwargs):
        self.image = pygame.image.load(image)
        self.health = health
        self.entityX = entityX
        self.entityY = entityY
        self.entityX_change = entityX_change
        self.entityY_change = entityY_change






        return super().__init__(*args, **kwargs)
    def collision():
        pass
    def laser():
        # Laser
        # create function to fire laser
        # Ready - you cant see the laser on the screen
        # Fire - the laser is currently moving
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
def player(x, y):
    screen.blit(playerImg, (x, y))  # draws the player at set coord


def tie(x, y, i):
    screen.blit(tieImg[i], (x, y))  # draws the enemy at set coord


    pass



        #**************************************#
        #                                      #
        #   rewrite collision for entity that  #
        #    works with enemy and player       #
        #                                      #
        #**************************************#

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


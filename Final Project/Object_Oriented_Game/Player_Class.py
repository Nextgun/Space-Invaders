
#
#   this code is working
#   but i need to check the logic for it
#





from Entity_Class import *

            #   player is a subclass of the entity class
class Player(Entity):
    #   initializes the player, and player number
    def __init__(self,player_num, list, *args, **kwargs):
        #   initializes the entity attributes
        Entity.__init__(self, list[0], list[1], list[2], list[3], 
                        list[4], list[5])
        #   player number (1,2,3,4)
        self.player_num = player_num

    #   sets a string message 
    def __str__(self):  
        msg = "This is player" + str(self.player_num)
        return msg
    
    def CheckBoundary(self):
        # Checking player boundaries
        entityX += entityX_change
        entityY += entityY_change
        
        if entityX <= 0:        entityX = 0
        elif entityX >= 736:    entityX = 736
        if entityY <= 0:        entityY = 0
        elif entityY >= 536:    entityY = 536
        


    #   fire laser for player using laser state
    def fire_laser(x, y):
        global laser_state
        laser_state = "fire"
        screen.blit(laserImg, (x + 16, y + 10))

    #   something
    def SpawnPlayer():
        #   add code here that spawns the players in
        pass

    #   laser state is for the player
    def PlayerLaser(self):
        self.laser_state = "ready"
        return self.laser_state


#   list with the arguments to be passed to the player class



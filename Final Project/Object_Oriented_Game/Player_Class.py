
#
#   this code is working
#   but i need to check the logic for it
#





from Entity_Class import *

            #   player is a subclass of the entity class
class Player(Entity):
    #   initializes the player, and player number
    def __init__(self,player_num, *args, **kwargs):
        #   initializes the entity attributes
   #     Entity.__init__(self, image, health, entityX, entityY, 
    #                    entityX_change, entityY_change)
        #   player number (1,2,3,4)
        self.player_num = player_num

    #   sets a string message 
    def __str__(self):  
        msg = "This is player" + str(self.player_num)
        return msg
    
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
player_info = ['plane.png', 3, 370, 480, 0, 0]

#   creates player 1
player1 =Player(1,player_info)

#   creates player 2
player2 = Player(2,player_info)


print(player1)
print(player1.PlayerLaser())
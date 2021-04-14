            #   player is a subclass of the entity class
class Player(entity):
    #   initializes the player, and player number
    def __init__(self,player_num, *args, **kwargs):
        #   initializes the entity attributes
        Entity.__init__(self, image, health, entityX, entityY, 
                        entityX_change, entityY_change)


        self.player_num = player_num
        pass

    #   sets a string message 
    def __str__():  
        msg = "This is player" + str(self.player_num)
        return msg
    
    #   fire laser for player using laser state
    def fire_laser(x, y):
        global laser_state
        laser_state = "fire"
        screen.blit(laserImg, (x + 16, y + 10))

    #   something
    def something():
        pass

    #   laser state is for the player
    laser_state = "ready"
    return super().__init__(*args, **kwargs)
    pass


#   list with the arguments to be passed to the player class
player_info = ['plane.png', 3, 370, 480, 0, 0]

#   creates player 1
player1 = player(1,player_info)

#   creates player 2
player2 = player(2,player_info)



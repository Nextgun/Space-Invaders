
#
#   this code is working
#   but i need to check the logic for it
#




from Entity_Class import *

#object oriented programming
class Enemy(Entity):

    def __init__(self, list, *args,  **kwargs):
        #   initializes the entity attributes
        Entity.__init__(self, list[0], list[1], list[2], list[3], 
                        list[4], list[5])

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

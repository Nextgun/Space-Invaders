#object oriented programming
class Enemy(Entity):

    def __init__(self, *args,  **kwargs):
        #   initializes the entity attributes
        Entity.__init__(self, image, health, entityX, entityY, 
                        entityX_change, entityY_change)

        # Enemy
        tieImg = []
        tieX = []
        tieY = []
        tieX_change = []
        tieY_change = []
        num_of_tie = 6

    return super().__init__(*args, **kwargs)
    def thecollosion:
        #collision code
        pass




#how the enemy spawns
for i in range(num_of_tie):
    tieImg.append(pygame.image.load('tie.png'))
    tieX.append(random.randint(0, 735))  # had enemy tie randomly spawn in different places on the x axis
    tieY.append(random.randint(50,
                               150))  # had enemy tie randomly spawn in different places on the y axis between set parameters
    tieX_change.append(0.3)
    tieY_change.append(20)

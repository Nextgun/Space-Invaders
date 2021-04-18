#   have function for drawing background, text, players, and enemys, etc
#   call each functions when needed

import pygame
from pygame import mixer


# draw score
# draw enemy
# draw player
# refresh background



class Draw(object):
    def __init__(self, width=800, height=600, font_type='FreeSansBold.ttf'):
        self.screen = pygame.display.set_mode((width, height)) # create the screen
        
        screen.fill((0, 0, 0))  # Changes the screen color or background
        
        self.font = pygame.font.Font(font_type, 28)

    def Screen_info():
       
        
        background = pygame.image.load('spacebg.png') # Background
        screen.blit(background, (0, 0))  # Background image

        # Background Sound
        mixer.music.load('background.wav')
        mixer.music.set_volume(0.04)
        mixer.music.play(-1)
    
        # Changes the Title and Icon
        pygame.display.set_caption("Group's Space Invaders")
        icon = pygame.image.load('alien.png')
        pygame.display.set_icon(icon)

        # Score
    def Score():
        score_value = 0
        font = pygame.font.Font('FreeSansBold.ttf', 28)
        textX = 10
        textY = 10

        # Game Over Text
    def GameOver():
        self.over_font = pygame.font.Font('FreeSansBold', 84)

    def show_score(x, y):
        score = font.render("Score :" + str(score_value), True, (255, 255, 255))
        screen.blit(score, (x, y))

    def game_over_text():
        over_text = over_font.render("GAME OVER!", True, (10, 240, 13))
        screen.blit(over_text, (170, 300))

    def draw_player(self, screen):
        Player.draw(self, screen)

    def draw_enemies(): # draw enemies in draw class
        for enemy_list:
            Enemy.draw(self, screen)
            pass
        pass

def tie(x, y, i):
    screen.blit(tieImg[i], (x, y))  # draws the enemy at set coord
    pass


def update_screen():
    Draw.draw_player()
    Draw.draw_enemies()



print("i work and draw things")
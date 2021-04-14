



def draw():
    screen = pygame.display.set_mode((800, 600))    # create the screen

    # Background
    background = pygame.image.load('C:\Hector School\Del Mar Sring 2021 Semester\Programming Fundamentals 1\C++ Code\GitHub Collab\Final Project\graphic_files\spacebg.png')

    # Background Sound
    mixer.music.load('background.wav')
    mixer.music.set_volume(0.04)
    mixer.music.play(-1)
    
    # Changes the Title and Icon
    pygame.display.set_caption("Group's Space Invaders")
    icon = pygame.image.load('alien.png')
    pygame.display.set_icon(icon)

# Score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 28)

textX = 10
textY = 10

# Game Over Text
over_font = pygame.font.Font('freesansbold.ttf', 84)


def show_score(x, y):
    score = font.render("Score :" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER!", True, (10, 240, 13))
    screen.blit(over_text, (170, 300))




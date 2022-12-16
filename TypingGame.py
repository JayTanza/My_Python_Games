#importing modules
import pygame
import random
import time
import sys

#initialize window
pygame.init()

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
black=(0,0,0)
gameDisplay = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #SETTINGS GAME DISPLAY SIZE
pygame.display.set_caption("Typing Game")
background = pygame.image.load('Images/Helmet-heroesBG.jpg')
background = pygame.transform.scale(background, (SCREEN_WIDTH,SCREEN_HEIGHT)) #SCALE IMAGE
icon = pygame.image.load('img/icons/favicon.ico')
pygame.display.set_icon(icon)
font = pygame.font.Font('comic.ttf',40)

# add background music
pygame.mixer.init()
pygame.mixer.music.load("BGMusic/Helmet Heroes Soundtrack - 02 - Heaths Training Ground.mp3")
pygame.mixer.music.play(loops=0)

#FUNCTION to get words randomly
word_speed = 0.5
score = 0

def new_word():
    global displayword, yourword,y_cor, x_cor, text, word_speed
    x_cor = random.randint(300,700) #randomly choose X coordinate between 300 and 700
    y_cor = 200 # Y coordinate
    word_speed += 0.10
    yourword = ''
    words = open("words.txt").read().split(', ')
    displayword = random.choice(words)
new_word()

#function to draw text
font_name = pygame.font.match_font('comic.ttf')
def draw_text(display,text,size,x,y):
    font = pygame.font.Font(font_name,size)
    text_surface = font.render(text,True, black)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    gameDisplay.blit(text_surface, text_rect)

#function to show front screen and gameover screen
def game_front_screen():
    gameDisplay.blit(background, (0,0))
    if not game_over:
        draw_text(gameDisplay, "GAME OVER!", 90, SCREEN_WIDTH/2, SCREEN_HEIGHT/4)
        draw_text(gameDisplay,"Score : " + str(score),70, SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    else:
        draw_text(gameDisplay, "PRESS ANY KEY TO BEGIN!", 54, SCREEN_WIDTH/2, 500)
    pygame.display.flip()
    waiting = True
    while waiting:

        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
            if(event.type == pygame.KEYUP):
                waiting = False

#mainloop
game_over = True
game_start = True
while True:
    if(game_over):
        if(game_start):
            game_front_screen()
        game_start = False
    game_over = False

    background = pygame.image.load('Images/Helmet-heroesBG.jpg')
    background = pygame.transform.scale(background, (SCREEN_WIDTH,SCREEN_HEIGHT))
    character = pygame.image.load('Images/Green_Bouncer.jpeg')
    character = pygame.transform.scale(character, (50,50))

    wood = pygame.image.load('Images/wood.png')
    wood = pygame.transform.scale(wood,(90,50))

    gameDisplay.blit(background, (0,0))
    y_cor += word_speed
    gameDisplay.blit(wood,(x_cor-50,y_cor+15))
    gameDisplay.blit(character,(x_cor-100,y_cor))
    draw_text(gameDisplay, str(displayword),40, x_cor, y_cor)
    draw_text(gameDisplay, 'Score:'+str(score), 40, SCREEN_WIDTH/2, 5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            yourword += pygame.key.name(event.key)

            if(displayword.startswith(yourword)):
                if(displayword == yourword):
                    score += len(displayword)
                    new_word()
            else:
                game_front_screen()
                time.sleep(2)
                pygame.quit()
                sys.exit()
        if(y_cor < SCREEN_HEIGHT-5):
            pygame.display.update()
        else:
            game_front_screen()


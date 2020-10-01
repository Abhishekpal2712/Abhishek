import pygame
import random
import os
pygame.mixer.init()


pygame.init()
# Colours
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
sscreen_width=600
sscreen_height=400
snakeWindow=pygame.display.set_mode((sscreen_width,sscreen_height))
pygame.display.set_caption("Snake")




pygame.display.update()
clock=pygame.time.Clock()
font=pygame.font.SysFont(None,25)


def scorer(text,color,x,y):
    screen_text=font.render(text,True,color)
    snakeWindow.blit(screen_text,[int(x),int(y)])
def plotsnake(snakeWindow,color,snakelist,snake_size):
    for x,y in snakelist:
        pygame.draw.rect(snakeWindow,color,[x,y,snake_size,snake_size])
def welcome():
    exit_game=False
    while not exit_game:
        snakeWindow.fill((250,120,220))
        scorer('Welcome',white,250,150)
        scorer('Press Space to play',white,220,200)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    pygame.mixer.music.load('back.mp3')
                    pygame.mixer.music.play()
                    gameloop()

        pygame.display.update()
        clock.tick(45)

def gameloop():
    if not os.path.exists('highscore.txt'):
        with open('highscore.txt','w') as f:
            f.write('0')
    with open('highscore.txt','r') as f:
        highscore=f.read()
        print(highscore)
    exit_game=False
    gave_over=False
    snake_x=50
    snake_y=50
    snake_size=10
    velocity_x=0
    velocity_y=0
    score=0
    fps=40
    foodx=random.randint(10,sscreen_width/2)
    foody=random.randint(10,sscreen_height/2)
    snake_velocity=4
    snakelist=[]
    snakelength=1
    while not exit_game:
        if gave_over:
            with open('highscore.txt','w') as f:
                f.write(str(highscore))
            snakeWindow.fill(white)
            svar='GAME OVER !!!!!!!!! PRESS ENTER TO CONTINUE'+' Highscore ' +str(highscore)
            scorer(svar,red,sscreen_width/3/4,sscreen_height/2)

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        pygame.mixer.music.load('back.mp3')
                        pygame.mixer.music.play()
                        gameloop()
                        
        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_d:
                        velocity_x=snake_velocity
                        velocity_y=0
                    if event.key==pygame.K_a:
                        velocity_x=-snake_velocity
                        velocity_y=0
                    if event.key==pygame.K_s:
                        velocity_y=snake_velocity
                        velocity_x=0
                    if event.key==pygame.K_w:
                        velocity_y=-snake_velocity
                        velocity_x=0
                    if event.key==pygame.K_q:
                        score+=15
                    if event.key==pygame.KMOD_SHIFT:
                        snake_velocity=snake_velocity-2
            snake_x=snake_x+velocity_x
            snake_y=snake_y+velocity_y
            if abs(snake_x-foodx)<9 and abs(snake_y-foody)<9:
                score+=10
                pygame.mixer.music.load('beep.mp3')
                pygame.mixer.music.play()
                pygame.mixer.music.load('back.mp3')
                pygame.mixer.music.play()
                if score>int(highscore):
                    highscore=score
                    print(highscore)
                foodx=random.randint(10,sscreen_width/2)
                foody=random.randint(10,sscreen_height/2)
                snakelength+=3
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snakelist.append(head)
            if len(snakelist)>snakelength:
                del snakelist[0]
            
            if head in snakelist[:-1]:
                gave_over=True
                pygame.mixer.music.load('boom.mp3')
                pygame.mixer.music.play()
                
            if snake_x<0 or snake_x>sscreen_width or snake_y<0 or snake_y>sscreen_height:
                gave_over=True
                pygame.mixer.music.load('boom.mp3')
                pygame.mixer.music.play()
            snakeWindow.fill((250,210,212))
            texttoput='CURRENT SCORE : '+str(score)
            scorer(texttoput,red,6,6)
            pygame.draw.rect(snakeWindow,black,[foodx,foody,snake_size,snake_size])
            plotsnake(snakeWindow,red,snakelist,snake_size)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit
welcome()
#gameloop()

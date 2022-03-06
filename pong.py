import pygame
import sys
import random
from time import sleep
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

start_game = False


screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

ball = pygame.Rect(screen_width/2 - 15,screen_height/2 - 15,30,30)
player = pygame.Rect(screen_width - 20, screen_height/2 -70, 10, 100)
opponent = pygame.Rect(10 , screen_height/2 -70, 10, 100)

bg_color = pygame.Color("grey12")
light_grey = (200,200,200)
#text_screen(f"Press Space to Start", light_grey, screen_width/2 - 50, 20)
#text_screen(f"Left Player - S/X Keys", light_grey, screen_width/2 - 50, 50)
#text_screen(f"Right Player - Up/Down Keys", light_grey, screen_width/2 - 50, 80)
wel_image = pygame.image.load("./Res/Welcome.jpg")
wel_image = pygame.transform.scale(wel_image, (800,600)).convert_alpha()

ball_speed_x = 7 * random.choice((1,-1)) 
ball_speed_y = 7 * random.choice((1,-1)) 
player_speed = 0
opponent_speed = 0
player_score = 0
opponent_score = 0
font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    screen.blit(screen_text, [x,y])

def ball_function():
    global ball_speed_x, ball_speed_y, opponent_score, player_score
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *=  -1
    if ball.left <= 0:
        opponent_score +=10
        ball_restart()
        sleep(2)
    if ball.right >= screen_width:
        player_score +=10
        ball_restart()
        sleep(2)
        
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def player_function():
    player.y += player_speed
    if player.top <=0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height 
    
def opponent_function():
    opponent.y += opponent_speed
    if opponent.top <=0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height 

def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2 , screen_height/2)
    ball_speed_x *= random.choice((1,-1)) 
    ball_speed_y *= random.choice((1,-1)) 

def main_game():
    ball_function()   
    player_function()
    opponent_function()
        
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2 , 0), (screen_width/2, screen_height))
    pygame.draw.circle(screen, light_grey,(int(screen_width/2), int(screen_height/2)), 100,1)
    text_screen(f"{player_score}", light_grey, screen_width/2 - 50, 20)
    text_screen(f"{opponent_score}", light_grey, screen_width/2 + 10, 20)
    
exitgame = False
    
while not exitgame:

    screen.blit(wel_image,(0,0))
    clock.tick(60)    
    if start_game:
        main_game()

        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exitgame = True            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
            if event.key == pygame.K_x:
                opponent_speed += 7
            if event.key == pygame.K_s:
                opponent_speed -= 7
            if event.key == pygame.K_SPACE:
                start_game = True 
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7            
            if event.key == pygame.K_x:
                opponent_speed -= 7
            if event.key == pygame.K_s:
                opponent_speed += 7 
                
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        pygame.display.set_mode((screen_width, screen_height))
    if keys[K_f]:
        screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
            
                
    pygame.display.update()
    pygame.display.flip()
pygame.quit()

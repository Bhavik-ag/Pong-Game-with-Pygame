import random
from time import sleep

def text_screen(screen, font, text, color, x, y):
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
        ball_restart(ball, screen_height, screen_width)
        sleep(2)
    if ball.right >= screen_width:
        player_score +=10
        ball_restart(ball, screen_height, screen_width)
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
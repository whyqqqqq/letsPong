# Implementation of classic arcade game Pong

import simplegui
import random
import math

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [300, 200]
#ball_vel = [1, -1]
#ball_vel = [ (random.randrange(120, 240)/60),  -1 * (random.randrange(120, 240)/60) ]

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [300, 200]
    ball_vel = [ (random.randrange(120, 240)/60),  -1 * (random.randrange(60, 180)/60) ]
    if direction == LEFT:   
        ball_vel = [-1, - 1]
    
    if direction == RIGHT:
        ball_vel = [1, -1]
     

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    spawn_ball(LEFT)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel # added the last one
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    
    ball_pos[0] = ball_pos[0] + ball_vel[0]
    ball_pos[1] = ball_pos[1] + ball_vel[1]   
    
      # bounce off top wall
    if ball_pos[1] <= 20:
        ball_vel[1] =- ball_vel[1]
      # bounce off bottom wall
    if ball_pos[1] >= 380:
        ball_vel[1] =- ball_vel[-1]
      # bounce off right gutter
    if ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS:
        #ball_vel[0] =- ball_vel[0]
        score1 += 1
        spawn_ball(LEFT)
        # bounce off left wall gutter
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
        #ball_vel[0] =- ball_vel[0]
        score2 += 1
        spawn_ball(RIGHT)
        
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 4, 'White', "White")
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_vel = 0
    paddle2_vel = 0
    paddle1_pos = (HEIGHT /2) + paddle1_vel
    paddle2_pos = (HEIGHT /2) + paddle2_vel
    
    # if paddle goes too high, stop
    #if paddle1_pos >= 
    # if paddle goes too low, stop
    
    # draw paddles
        #paddle2:
    canvas.draw_polygon([(WIDTH - PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT), (WIDTH - PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT), (WIDTH+1, paddle2_pos - HALF_PAD_HEIGHT), (WIDTH+1, paddle2_pos + HALF_PAD_HEIGHT)], 1, "White", "White")
        #paddle1:    
    canvas.draw_polygon([(PAD_WIDTH, paddle1_pos+ HALF_PAD_HEIGHT), (PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT), (-1, paddle1_pos- HALF_PAD_HEIGHT), (-1, paddle1_pos + HALF_PAD_HEIGHT)], 1, "White", "White")
    
    # draw scores
    canvas.draw_text((str(score1)), [200, 100], 65, "White")
    canvas.draw_text((str(score2)), [400, 100], 65, "White")
    
        
def keydown(key):
    global paddle1_vel, paddle2_vel, paddle1_pos  #add paddle1_pos
    paddle1_vel = 0
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= 1
        
        
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel += 1
        
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel -= 1
    if key==simplegui.KEY_MAP["down"]:
        paddle2_vel += 1
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    paddle1_vel = 0
    paddle2_vel = 0
    
def restart_button_handler():
    new_game()


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", restart_button_handler)


# start frame
new_game()
frame.start()

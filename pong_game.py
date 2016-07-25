######################################################################################################
##      ********HOW TO RUN THIS CODE************
##
##      1. COPY OR DOWNLOAD THE FILE
##      2. GO TO www.codeskulpter.org, DELETE THE DEFAULT CONTENT AND PASTE THIS CODE.
##      3. CLICK RUN BUTTON
##      NOTE:  DO NOT USE INTERNET EXPLORER OR EDGE BROWSER TO RUN THIS CODE. IT HAS COMPATABLITY ISSIES
##
##      __author__ Temesgen
######################################################################################################

import simplegui
import random

#First initialize globals - position and velocity and vertical info for paddles
WIDTH = 700
HALF_WIDTH = WIDTH / 2
HEIGHT = 500   
HALF_HEIGHT = HEIGHT / 2
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 100
LEFT = False
RIGHT = True

#paddles
paddle1_pos = HEIGHT / 2.5
paddle2_pos = HEIGHT / 2.5
paddle1_vel = 0
paddle2_vel = 0
paddle_vel = 5


# initialize ball_pos and ball_vel for new bal in middle of table
ball_pos = [HALF_WIDTH, HALF_HEIGHT]
ball_vel = [0,1]

# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [HALF_WIDTH, HALF_HEIGHT]	
    ball_vel[0] = -random.randrange(120,240) / 100 
    if direction == True:
        ball_vel[0] *= -1
    ball_vel[1] = -random.randrange(60, 180) / 100

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    spawn_ball(0)
    paddle1_pos = HEIGHT / 2.5
    paddle2_pos = HEIGHT / 2.5
    

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([HALF_WIDTH, 0],[HALF_WIDTH, HEIGHT], 1, "white")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "white")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "white")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    if ball_pos[0] <= (BALL_RADIUS + PAD_WIDTH) or ball_pos[0] >= (WIDTH - PAD_WIDTH - BALL_RADIUS):        
        ball_vel[0] *= -1
        
        if (ball_pos[0] > HALF_WIDTH):             
            if (ball_pos[1] < paddle2_pos or ball_pos[1] > paddle2_pos + PAD_HEIGHT):
                score1 += 1 
                spawn_ball(LEFT) 
            else: ball_vel[0] += .1 * ball_vel[0]
            
        if (ball_pos[0] < HALF_WIDTH):
            if (ball_pos[1] < paddle1_pos or ball_pos[1] > paddle1_pos + PAD_HEIGHT ):
                score2 += 1
                spawn_ball(RIGHT)
            else: ball_vel[0] += .1 * ball_vel[0]
        
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= (HEIGHT - BALL_RADIUS):
        ball_vel[1] *= -1
 
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "white")
    
    # update paddle's vertical position, keep paddle on the screen
    global paddle1_vel, paddle2_vel
    
    if (paddle1_pos <= HEIGHT - PAD_HEIGHT and paddle1_vel > 0) or (paddle1_pos >= 0 and paddle1_vel < 0) :
        paddle1_pos += paddle1_vel    
    elif (paddle2_pos <= HEIGHT - PAD_HEIGHT and paddle2_vel > 0) or (paddle2_pos >= 0 and paddle2_vel < 0) :
        paddle2_pos += paddle2_vel  
    
    # draw paddles
    canvas.draw_polygon([[0, paddle1_pos], [PAD_WIDTH, paddle1_pos],[PAD_WIDTH, (paddle1_pos) +PAD_HEIGHT ],[0, (paddle1_pos) + PAD_HEIGHT]],1, "white", "white") 
    canvas.draw_polygon([[WIDTH, paddle2_pos], [WIDTH - PAD_WIDTH, paddle2_pos], [WIDTH - PAD_WIDTH, paddle2_pos + PAD_HEIGHT], [WIDTH, paddle2_pos + PAD_HEIGHT]],1, "white", "white")
    # draw scores
    canvas.draw_text(str(score1), [250, 100], 60, "Green")    
    canvas.draw_text(str(score2), [400, 100], 60, "Green")
        
def keydown(key):
    global paddle1_vel, paddle2_vel, paddle_vel
    
    #PLAYER ONE   
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -paddle_vel     
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = paddle_vel  
    
    #PLAYER TWO
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = paddle_vel    
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -paddle_vel 
      
def keyup(key):
    global paddle1_vel, paddle2_vel, paddle_vel
    
    #PLAYER ONE
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
        
    #PLAYER TWO
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
      
# create frame
f = simplegui.create_frame("Pong Game", WIDTH, HEIGHT)
f.set_draw_handler(draw)
f.set_keydown_handler(keydown)
f.set_keyup_handler(keyup)
f.add_button("RESTART", new_game, 150)


# start frame
f.start()
new_game()

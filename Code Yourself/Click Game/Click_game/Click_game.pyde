now_time = 0
ran_xpos = 0
ran_ypos = 0
game_start = False
time = 0
def setup():
    global now_time
    size(800, 600)
    now_time = millis()
    
def draw():
    global now_time, ran_xpos, ran_ypos, time, game_start
    background(255)
    textSize(24)
    fill(0) # Fill the color
    text(time, width/2, 100)
    if game_start == True:
        if (mousePressed == True) and (dist(mouseX, mouseY, ran_xpos, ran_ypos) < 25) :
            game_start = False
        else:
            time = (millis()-now_time)/1000.0
            
    ellipse(ran_xpos, ran_ypos, 50, 50)
    
    
def mousePressed():
    global now_time, ran_xpos, ran_ypos, game_start
    if game_start == False:
        ran_xpos = random(width)
        ran_ypos = random(height)
        now_time = millis()
        game_start = True
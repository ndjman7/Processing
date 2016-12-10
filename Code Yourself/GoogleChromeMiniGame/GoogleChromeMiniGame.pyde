from class_wall import Wall
x = 100
y = 0
speed = 2
now_time = 0
interval = 3000

walls = []

score = 0

def setup():
    global now_time
    now_time = millis()
    size(800, 600)
    
def draw():
    global y, interval, speed, now_time, score, game_over

    background(0)
    
    fill(255)
    textSize(24)
    text(score, 700, 100)
    
    if millis() - now_time > interval:
        walls.append(Wall())
        now_time = millis()
        interval = int(random(2000,3000))
    

    ellipse(x, y, 30, 30)
    if y+speed < height/2:
        y += speed
        speed += 0.5
    stroke(255)
    line(0, height/2, width, height/2)
    
    for myWall in walls:
        myWall.display(x,y)
        if not Wall.game_over:
            myWall.move()
        if myWall.del == True:
            walls.remove(myWall)
        if myWall.xpos < x and myWall.up == False:
            score += 1
            myWall.up = True
    
            
def keyPressed():
    global speed, game_over, score
    speed = -10
    if Wall.game_over == True:
        Wall.game_over = False
        score = 0 
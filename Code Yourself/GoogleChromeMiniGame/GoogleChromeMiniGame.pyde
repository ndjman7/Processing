from class_wall import Wall
x = 100
y = 0
speed = 2
now_time = 0
interval = 3000
game_over = False
walls = []
def setup():
    global now_time
    now_time = millis()
    size(800, 600)
    
def draw():
    global y, interval, speed, now_time
    
    background(0)
    if millis() - now_time > interval:
        walls.append(Wall())
        now_time = millis()
        interval = random(2000,3000)
    
    
    background(0)
    ellipse(x, y, 30, 30)
    if y+speed < height/2:
        y += speed
        speed += 0.5
    stroke(255)
    line(0, height/2, width, height/2)
    for myWall in walls:
        myWall.display(x, y)
        if not game_over:
            myWall.move()
        if myWall.del == True:
            walls.remove(myWall)
    
def keyPressed():
    global speed
    speed = -10
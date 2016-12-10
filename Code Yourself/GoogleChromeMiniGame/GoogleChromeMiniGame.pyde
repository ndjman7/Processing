x = 100
y = 0
speed = 1
def setup():
    size(800, 600)
    
def draw():
    global y
    global speed
    background(0)
    ellipse(x, y, 50, 50)
    if y+speed < height/2:
        y += speed
        speed += 0.5
    stroke(255)
    line(0, height/2, width, height/2)
    
def keyPressed():
    global speed
    speed = -10
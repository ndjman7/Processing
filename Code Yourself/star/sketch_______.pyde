s_num = 500
myStar = []

def setup():
    size(800, 600, P3D)
    for i in range(s_num):
        myStar.append(Star())
    smooth(8)
    
def draw():
    background(0)
    for i in range(s_num):
        myStar[i].display()
        myStar[i].move()
    
class Star():
    def __init__(self):
        self.xpos = random(width)
        self.ypos = random(height)
        self.zpos = random(-200,400)
        self.speed = random(3,5)
        self.w = random(3,5)
    
    def display(self):
        noStroke()
        fill(255)
        pushMatrix()
        translate(self.xpos, self.ypos, self.zpos)
        ellipse(self.xpos, self.ypos, self.w, self.w)
        popMatrix()
        
    def move(self):
        self.zpos = self.zpos + self.speed
        if self.zpos > 500:
            self.zpos = -200
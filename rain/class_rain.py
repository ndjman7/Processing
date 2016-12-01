class Rain():
    
    def __init__(self,xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.speed = random(5,10)
        self.h = random(10,20)
        self.gravity = 0.1
    
    def display(self):
        stroke(255)
        line(self.xpos, self.ypos, self.xpos, self.ypos+self.h)
        
    def move(self):
        self.ypos = self.ypos + (self.speed + self.gravity)
        self.gravity += 0.1
        if self.ypos > height:
            self.ypos = 0
            self.xpos = random(width)
            self.gravity = 0
            
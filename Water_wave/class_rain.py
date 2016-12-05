class Rain():
    def __init__(self, temp_xpos, temp_ypos):
        self.xpos = temp_xpos
        self.ypos = temp_ypos
        self.r = 0
        self.speed = 1.0
        self.max_r = random(200, 400)
        self.del = False
        self.r_random = random(0.2, 0.8)
        self.alpha = 255
        
    def display(self):
        noFill()
        stroke(255, self.alpha)
        ellipse (self.xpos, self.ypos, self.r, self.r)
        ellipse (self.xpos, self.ypos, self.r * self.r_random, self.r * self.r_random)
        ellipse (self.xpos, self.ypos, self.r * (self.r_random * 2), self.r * (self.r_random * 2))
    
    def move(self):
        self.r += self.speed
        self.alpha = ((self.max_r - self.r) / 400) * 255
        print(self.alpha)
        if self.max_r < self.r:
            self.del = True

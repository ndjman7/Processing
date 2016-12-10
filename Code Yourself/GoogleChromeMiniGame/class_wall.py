class Wall():
    game_over = False
    def __init__(self):
        self.h = random(10,30)
        self.xpos = width
        self.ypos = height/2
        self.del = False
        self.speed = 4
        self.up = False
    def display(self, x, y):
        rect(self.xpos, self.ypos - self.h, 5, self.h)
        
        if dist(x, y, self.xpos, self.ypos) < 15:
            Wall.game_over = True
        
    def move(self):
        self.xpos -= self.speed
        if self.xpos < -5:
            self.del = True
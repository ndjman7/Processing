from class_rain import Rain
num = 500
myRain = []
def setup():
    size(800,600)
    for i in range(num):
        myRain.append(Rain(random(width), random(height)))
def draw():
    background(0)
    for i in range(num):
        myRain[i].display()
        myRain[i].move()
        W
from class_rain import Rain

rains = []
def setup():
    size(800, 600, FX2D)
def draw():
    background(0)
    
    for rain in rains:
        rain.display()
        rain.move()
        if rain.del == True:
            rains.remove(rain)
            
            
            
            
def mouseReleased():
    rains.append(Rain(mouseX, mouseY))
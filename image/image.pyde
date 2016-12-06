def setup(): #한
    global sample
    size(800,800)
    sample = loadImage("sample.jpg")
    
def draw():
    background(255)
    image(sample, 0 , 0 , mouseX, mouseY)
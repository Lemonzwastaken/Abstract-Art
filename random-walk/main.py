import turtle
import random
from PIL import Image
import os

#CONSTANTS(FOR CUSTOMIZABILITY)
WALKS = 200 #How many random walks do you want him to perform
DISTANCE = 30 #How much distance should he travel per walk
SAVE_PATH = r"random-walk\generated_Images\randomwalk.png" # Where do you want to save the image
PENSIZE = 15 #PENSIZE





timmy = turtle.Turtle()
screen = turtle.Screen()
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r,g,b)

timmy.pensize(PENSIZE)

timmy.speed("fast")

directions = [90,180,270,360]

for i in range(WALKS):
    
    timmy.forward(DISTANCE)

    timmy.right(random.choice(directions))

    timmy.color(random_color())

timmy.penup()
timmy.goto(1000,1000)#takes him out the map



# Save as EPS first, then convert to PNG and removes the eps
EPS_PATH = "randomwalk.eps" #leave empty unless you wanna store the .eps as well somewhere
canvas = screen.getcanvas()
canvas.postscript(file=EPS_PATH)

print("EPS saved:", os.path.exists(EPS_PATH))

img = Image.open(EPS_PATH)
img.load()
img_copy = img.copy()
img.close()

print("Image size:", img_copy.size)
print("Image mode:", img_copy.mode)

img_copy.save(SAVE_PATH)
print("PNG saved:", os.path.exists(SAVE_PATH))
print("Saved to:", os.path.abspath(SAVE_PATH))

os.remove(EPS_PATH)


screen.exitonclick()
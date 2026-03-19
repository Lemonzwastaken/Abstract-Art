import turtle
import random
import os
from PIL import Image

#CONSTANTS (Customizable)
RADIUS = 150 #How big the circle should be
INCREMENT = 1 #How much increment do you want between the circles(in rotation)
SAVE_PATH = r"spirograph\generated_images\spirograph.png" # Where do you want to save the image
PENSIZE = 15 #PENSIZE



timmy = turtle.Turtle()
screen = turtle.Screen()
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r,g,b)

timmy.color('LimeGreen')
timmy.speed(0)


for rad in range(int(360/INCREMENT)):

    timmy.circle(RADIUS)
    timmy.right(INCREMENT)
    timmy.color(random_color())

timmy.penup()
timmy.goto(1000,1000)
# Save as EPS first, then convert to PNG and removes the eps
eps_path = "randomwalk.eps"

canvas = screen.getcanvas()
canvas.postscript(file=eps_path)

print("EPS saved:", os.path.exists(eps_path))

img = Image.open(eps_path)
img.load()
img_copy = img.copy()
img.close()

print("Image size:", img_copy.size)
print("Image mode:", img_copy.mode)

img_copy.save(SAVE_PATH)
print("PNG saved:", os.path.exists(SAVE_PATH))
print("Saved to:", os.path.abspath(SAVE_PATH))

os.remove(eps_path)




screen.exitonclick()
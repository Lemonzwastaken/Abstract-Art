#CONSTANTS

LINES = 10 #How many lines of dots do you want(still not optimised to fit screen)
DOTS = 10 #How many dots you want per line(still not optimised to fit screen)
COLOR_EXTRACTION_PATH = r'hirst-dotted-art\reference_image.jpg' #Path of the image where you want to extract the colors from
RADIUS = 25 #Radius of the dot
DISTANCE = 50 #Distance between the dots
SAVE_PATH = r"hirst-dotted-art\generated_Images\hirst-dotted-art.png" #Path where you want to save the image

#EXTRACTS COLOR FROM A COLOR PALLET WE LIKE
import colorgram
rgb_colors = []
colors = colorgram.extract(COLOR_EXTRACTION_PATH, 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    rgb_colors.append((r,g,b))

import turtle
import random
from PIL import Image
import os

#Setting timmy up
timmy = turtle.Turtle()
screen = turtle.Screen()
turtle.colormode(255)
timmy.speed(0)
timmy.penup()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

def draw_dots():
    for _ in range(DOTS):
        timmy.dot(RADIUS, random.choice(rgb_colors))
        timmy.forward(DISTANCE)
        
def change_line():
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(180)
    timmy.forward(DISTANCE*DOTS)
    timmy.setheading(0)


for dots in range(LINES):
    draw_dots()
    change_line()


timmy.goto(1000,1000)

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
import turtle
import random
# import colorgram

# colors = colorgram.extract("painting.jpg",30)

# rgb_values = []

# for rgb in range(len(colors)):
#     r = colors[rgb].rgb.r
#     g = colors[rgb].rgb.g
#     b = colors[rgb].rgb.b
#     color_group = (r,g,b)
#     rgb_values.append(color_group)
# print(rgb_values)

"""creation of the turtle object"""
thomas = turtle.Turtle()

"""Creation of the screen object"""
Screen = turtle.Screen()

"""Changes the default colormode from floating point numbers"""
turtle.colormode(255)

# print(Screen.window_width()) #- used to print out the width of our window.
# print(Screen.window_height()) #- used to print out the height of our window.

"""Designating the starting coordinates of our turtle object. """
def paint_params(dot_size):
    gap_distance = dot_size * 2
    x_start = (-Screen.window_width()/2) + gap_distance
    y_start = (-Screen.window_height()/2) + gap_distance
    return [x_start, y_start]

"""setting intital coordinates of our turtle object"""
intial_x_cord = thomas.teleport(x=paint_params(20)[0])
intial_y_cord = thomas.teleport(y=paint_params(20)[1])

color_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (39, 216, 69), 
(238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), 
(61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), 
(73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51)]

current_x_cord = thomas.xcor()
current_y_cord = thomas.ycor()

print(Screen.window_height())
print(Screen.window_width())

while thomas.xcor() <= 600: 
    print(thomas.position())
    thomas.dot(20,(random.choice(color_list)))
    thomas.teleport(x=thomas.xcor()+ 40)
    

Screen.exitonclick()
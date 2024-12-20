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

dot_size = 20
start_pos = (-Screen.window_width()/2) + (dot_size*2)
thomas.teleport(x= start_pos)

color_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (39, 216, 69), 
(238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), 
(61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), 
(73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51)]

for x in range(10):
    thomas.dot(dot_size,(random.choice(color_list)))
    start_pos += 30
    thomas.teleport(x=start_pos)

Screen.exitonclick()
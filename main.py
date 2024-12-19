import colorgram

colors = colorgram.extract("painting.jpg",6)

rgb_values = []

for rgb in range(len(colors)):
    r = colors[rgb].rgb.r
    g = colors[rgb].rgb.g
    b = colors[rgb].rgb.b
    color_group = (r,g,b)
    rgb_values.append(color_group)
print(rgb_values)
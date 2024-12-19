import colorgram

colors = colorgram.extract("painting.jpg",6)

color_values = []

for rgb in range(len(colors)):
    color_group = ((colors[rgb].rgb.r), (colors[rgb].rgb.g), (colors[rgb].rgb.b))
    color_values.append(color_group)
print(color_values)
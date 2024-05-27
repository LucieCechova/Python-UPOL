"""Separating string of points to list of named coordinates."""

text = "10,20"
coords = text.split(";")
print(coords)
output = []
for pair in coords:
    print(pair)
    x, y = pair.split(",")
    x, y = float(x), float(y)
    point = {"x": x, "y": y}
    output.append(point)
print(output)

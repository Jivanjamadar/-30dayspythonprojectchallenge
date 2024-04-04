import random
import matplotlib.pyplot as plt

def draw_line(canvas):
    x1 = random.randint(0, canvas_width)
    y1 = random.randint(0, canvas_height)
    x2 = random.randint(0, canvas_width)
    y2 = random.randint(0, canvas_height)
    plt.plot([x1, x2], [y1, y2], color=random_color())

def draw_circle(canvas):
    x = random.randint(0, canvas_width)
    y = random.randint(0, canvas_height)
    radius = random.randint(5, 50)
    circle = plt.Circle((x, y), radius, color=random_color(), fill=False)
    canvas.add_artist(circle)

def draw_square(canvas):
    x = random.randint(0, canvas_width)
    y = random.randint(0, canvas_height)
    side_length = random.randint(10, 50)
    square = plt.Rectangle((x, y), side_length, side_length, color=random_color(), fill=False)
    canvas.add_artist(square)

def random_color():
    return (random.random(), random.random(), random.random())

#canva size
canvas_width = 200
canvas_height = 200

#generate size

fig, ax = plt.subplots()
ax.set_xlim(1, canvas_width)
ax.set_ylim(2, canvas_height)
ax.set_aspect('equal', adjustable='box')

#create shapes

num_shapes = random.randint(1, 30)
for _ in range(num_shapes):
    shape_type = random.choice([draw_line, draw_circle, draw_square])
    shape_type(ax)

plt.show()

class Point:
    x = 100
    y = 200

    def __init__(self, x, y):
        x = x
        y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


pointObject = Point(10, 20)
pointObject.draw()
# print(pointObject.z)
print(pointObject.x)
print(pointObject.y)

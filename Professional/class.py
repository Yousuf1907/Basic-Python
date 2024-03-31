class Point:
    def __init__(self,x,y) -> None:
        self.x=x
        self.y=y


    def draw(self):
        print('draw')

    def move(self):
        print('move')

# point1=Point()
# point1.x=19
# point1.y=7
# point1.draw()

point2=Point(10,20)
# Point.draw()
print(point2.x)
class Rectangle:
   def __init__(self, color="blue", width=100, height=100):
       self.color = color
       self.width = width
       self.height = height

   def square(self):
       return self.width * self.height
rect1 = Rectangle()
print(rect1.color)
print(rect1.square())
rect1 = Rectangle("white", 23, 34)
print(rect1.color)
print(rect1.square())


def get_color(self):
       return self.color
clr=Rectangle()
print(clr.color)

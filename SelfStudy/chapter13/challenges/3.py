class Shape:
    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self,w,l):
        self.width=w
        self.len=l

class Square(Shape):
    def __init__(self,l):
        self.len=l



a_rectangle=Rectangle(20,10)
a_rectangle.what_am_i()
a_square=Square(30)
a_square.what_am_i()
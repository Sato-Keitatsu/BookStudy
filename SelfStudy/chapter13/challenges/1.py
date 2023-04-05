class Rectangle:
    def __init__(self,w,l):
        self.width=w
        self.len=l
    
    def circumference(self):
        return self.width*2+self.len*2

class Square:
    def __init__(self,l):
        self.len=l
    
    def circumference(self):
        return self.len*4

a_rectangle=Rectangle(20,10)
print(a_rectangle.circumference())
a_square=Square(30)
print(a_square.circumference())
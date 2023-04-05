class Triangle:
    def __init__(self,b,h):
        self.botton=b
        self.height=h
    
    def area(self):
        return self.botton*self.height/2

triangle=Triangle(10,4)
print(triangle.area())
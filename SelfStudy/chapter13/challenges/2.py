class Square:
    def __init__(self,l):
        self.len=l
    
    def change_size(self,n):
        self.len=+n

a_square=Square(10)
print(a_square.len)
a_square.change_size(20)
print(a_square.len)
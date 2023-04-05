class Square:

    list=[]
    def __init__(self,l):
        self.len=l
        self.list.append(self.len)

s1=Square(10)
s2=Square(20)
s3=Square(30)

print(Square.list)
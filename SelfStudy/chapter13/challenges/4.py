class Horse:
    def __init__(self,name,owner):
        self.name=name
        self.owner=owner

class Rider:
    def __init__(self,name):
        self.name=name

kchan=Rider("keitatsu")
a_horse=Horse("pochi",kchan)
print(a_horse.owner.name)
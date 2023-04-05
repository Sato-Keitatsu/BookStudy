s="   THE    "
s=s.strip()
print(s)

equ = "All animals are equal."
equ=equ.replace("a","@")
print(equ)

print("animals".index("m"))
try:
    "animals".index("z")
except:
    print("Not found.")

print("Cat" in "Cat in the hat.")
print("Bat" in "Cat in the hat.")
print("Bat" not in "Cat in the hat.")
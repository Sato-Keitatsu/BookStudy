#例外処理
a=int(input("Type a number:"))
b=int(input("Type anotyher:"))
try:
    print(a/b)
except ZeroDivisionError:
    print("b cannot be zero.")

#例外処理2つ
try:
    a=int(input("Type a number:"))
    b=int(input("Type anotyher:"))
    print(a/b)
except(ZeroDivisionError,ValueError):
    print("Invalid input.")
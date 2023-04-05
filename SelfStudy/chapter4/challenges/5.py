def math_float():
    try:
        x=float(input("type a number:"))
        return x
    except ValueError:
        print("type a number!!")

print(math_float())
import random
a=random.randint(1,101)
print(a)
if a<=10:
    print("aは10以上だ")
elif 10<a<=25:
    print("aは10より大きいが25以下だ")
else:
    print("aは25よりも大きい")
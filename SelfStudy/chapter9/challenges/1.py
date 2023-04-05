with open("test_1.txt","w",encoding="utf-8") as f:
    f.write("これはテストです。")
with open("test_1.txt","r",encoding="utf-8") as f:
    print(f.read())

with open("test_2.txt","r",encoding="utf-8") as h:
    print(h.read())
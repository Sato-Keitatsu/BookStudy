answers=[4,10,25]

while True:
    answer=input("数字を入力してください:")
    if answer=="q":
        break
    try:
        answer=int(answer)
    except ValueError:
        print("数字を入力するか、qで終了します")
    if answer in answers:
        print("正解")
    elif answer not in answers:
        print("不正解")

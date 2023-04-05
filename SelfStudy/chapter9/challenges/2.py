q=input("あなたの好きな食べ物は何ですか?")
with open("test_3.txt","w",encoding="utf-8") as f:
    f.write(q)
k_personality={"height":"167","favorite_color":"black","favo_author":"Eiichiro Oda"}
a=input("任意のキーを入力してください。")
if a in k_personality:
    print(k_personality[a])
else:
    print("キーが確認できません。")
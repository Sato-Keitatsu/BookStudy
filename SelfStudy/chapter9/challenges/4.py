import csv

list=[
    ["トップガン","卒業白書","マイノリティ・リポート"],
    ["タイタニック","レヴェナント","インセプション"],
    ["トレーニング デイ","マイ・ボディガード","フライト"]
    ]

with open("test_5.csv","w",newline="",encoding="utf-8") as f:
    w=csv.writer(f,delimiter=",")
    w.writerow(["トップガン","卒業白書","マイノリティ・リポート"])
    w.writerow(["タイタニック","レヴェナント","インセプション"])
    w.writerow(["トレーニング デイ","マイ・ボディガード","フライト"])

with open("test_5.csv","r",encoding="utf-8") as f:
    r=csv.reader(f,delimiter=",")
    for row in r:
        print(",".join(row))
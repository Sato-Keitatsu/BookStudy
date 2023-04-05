import csv

list=[
    ["Top Gun","Risky Business","Minority Report"],
    ["Titanic","The Revenant","Inception"],
    ["Training Day","Man on Fire","Flight"]
    ]

with open("test_4.csv","w",newline="") as f:
    w=csv.writer(f,delimiter=",")
    w.writerow(["Top Gun","Risky Business","Minority Report"])
    w.writerow(["Titanic","The Revenant","Inception"])
    w.writerow(["Training Day","Man on Fire","Flight"])

with open("test_4.csv","r") as f:
    r=csv.reader(f,delimiter=",")
    for row in r:
        print(",".join(row))

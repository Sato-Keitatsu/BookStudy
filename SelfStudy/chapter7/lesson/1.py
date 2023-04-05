tv=["GOT","Narcos","Vice"]

i=0
for show in tv:
    new=tv[i]
    new=new.upper()
    tv[i]=new
    i+=1
print(tv)

tv=["GOT","Narcos","Vice"]
coms=["Arrested Development","friends","Always Sunny"]
all_shows=[]

for show in tv:
    show=show.upper()
    all_shows.append(show)

for show in coms:
    show=show.upper()
    all_shows.append(show)

print(all_shows)
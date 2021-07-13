#удаление строчных комментариев C like
d=[]
with open("test.txt","r") as f:
    m=f.readlines()
    for i in m:
        d.append(i[:i.find("//")]+"\n")

with open("test.txt","w") as f:
    f.writelines(d)

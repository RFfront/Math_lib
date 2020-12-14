class mathObj():
    def __init__(self,stroka):
        #status 2- init eror
        #status 1- sucsess init
        #status "at string: " error at
        self.stroka=stroka

        status =1
    def __str__(self):
        return self.stroka
#class oper()
a=str("2f+12+1g+r3+#[t2]")
af=a.find("#[")
if af!=int(-1):
    a[af:].find("]")=
else:
    ae


lastPlus=[]
for i in range(len(a)):

    if a[i] =='+':
        lastPlus.append(i)


slice=[]
lastPlus.insert(0,0)
lastPlus.append(len(a))
print(lastPlus)

for i in range(len(lastPlus)-1):
    slice.append(a[lastPlus[i]:lastPlus[i+1]])

print(slice)

#a=str(input())

#[2^2]
#   2f+12

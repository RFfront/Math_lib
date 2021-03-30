class MathWrongStr(Exception):
    print("!!!!!!!!!!!!!!!!!!!!!!!\n\nstring not correct\n\n!!!!!!!!!!!!!!!!!!!!!!!")

class mathObj:
    num=0
    stephen=1
    #child=mathObj()
    def __init__(self,stroka,mathchild=[]):
        self.stroka=stroka
        self.mathchild=mathchild
    def __str__(self):
        return self.stroka
    """
    def toAnthStr(self):
        return "mathObj"+
    """

#class oper()
a=str("(2x+34)-(11x+20x")
a="("+a+")"

def findParenthesisPrimitives(stroka):
    #stroka
    MOL=[]
    opened=0
    #mathObj
    a=0
    while a!=-1:
        for i in range(len(stroka)):
            if stroka[i]=="(":
                opened=i
        if opened!=0:

            Tlast=stroka[opened:].find(")")
            if Tlast!=-1:
                primitive=stroka[opened:opened+Tlast+1]
                stroka=stroka[:opened]+"#mathObj"+str(a)+"#"+stroka[opened+Tlast+1:]
                MOL.append(mathObj(primitive))
                #print(primitive)
                a+=1
                #print(stroka)
            else:
                raise MathWrongStr()
        else:
            a=-1
    return [MOL,stroka]

print(findParenthesisPrimitives(a))
#print(a)

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

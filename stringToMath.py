class MathWrongStr(Exception):
    def __init__(self):
        print("!!!!!!!!!!!!!!!!!!!!!!!\n\nstring not correct\n\n!!!!!!!!!!!!!!!!!!!!!!!")
        super().__init__()

class RootMath():
    __num = 0
    def __init__(self,stringPart,multiplyer=1,poow=1):
        self.multiplyer=multiplyer
        self.actNu=self.__num
        self.num+=1
        self.poow=poow
        self.stringPart=''


class mathObj:
    __num = 0
    def __init__(self,strokaGe):
        self.type=""
        self.thisNum=self.__num
        self.stroka=strokaGe
        self.__num+=1
        self.mathObjList=list()

    def optimize(self):
        self.findBracketPrimitives()
        self.findRootMath()


    def findRootMath(self):
        n=set("^+-*/=")

        for i in self.mathObjList:
            print(str(i))

    def __str__(self):
        return self.stroka

    def __repr__(self):
        return f"mathObj{self.thisNum}{{{self.stroka}}}"

    def findBracketPrimitives(self):
        self.mathObjList=[]
        a=0
        while a!=-1:
            opened=self.stroka.rfind("(")
            if opened!=-1:

                Tlast=self.stroka[opened:].find(")")
                if Tlast!=-1:
                    primitive=self.stroka[opened+1:opened+Tlast]
                    tmp=mathObj(primitive)
                    self.mathObjList.append(tmp)
                    self.stroka=f"{self.stroka[:opened]}#mathObj{tmp.thisNum}#{self.stroka[opened+Tlast+1:]}"
                    a+=1
                else:
                    raise MathWrongStr()
            else:
                a=-1
        return [self.mathObjList,self.stroka]

    def findAnotPrimitives(self):
        return

a=mathObj("(2x^2+34)^2-(11x+20x+(2x-11x))")
a.optimize()
print(a)

"expression"
'''lastPlus=[]
for i in range(len(a)):

    if a[i] =='+':
        lastPlus.append(i)


slice=[]
lastPlus.insert(0,0)
lastPlus.append(len(a))
print(lastPlus)

for i in range(len(lastPlus)-1):
    slice.append(a[lastPlus[i]:lastPlus[i+1]])

print(slice)'''

#a=str(input())

#[2^2]
#   2f+12

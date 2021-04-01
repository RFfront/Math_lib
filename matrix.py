class Matrix:
    def __init__(self,listA):
        self.__listAr=listA
        n=len(listA[0])
        for i in listA:
            if n <len(i):
                n=len(i)
        self.__n=n#colls столбцы

        self.__m=len(listA)#rows строки
    @property
    def n(self):
        return self.__n
    @property
    def m(self):
        return self.__m


    def __str__(self): #"Matrix obj {}x{}".format(self.__m,self.__n)
        sgr=''
        for i in self.__listAr:
            h=list(map(lambda x:str(x),i))
            sgr+=" ".join(h)
            sgr+="\n"
        return sgr
    def __add__(self, other):
        if not isinstance(other,Matrix):
            raise ValueError("you try add not Matrix")
        else:
            if self.__n == other.__n and self.__m == other.__m:
                for i in range(len(self.__listAr)):
                    for g in range(len(self.__listAr[i])):
                        self.__listAr[i][g]+=other.__listAr[i][g]
            else:
                raise ValueError("you try add Matrix different sizes")
        return self
    def __mul__(self, other):
        if not isinstance(other,Matrix):
            for i in range(len(self.__listAr)):
                for g in range(len(self.__listAr[i])):
                    self.__listAr[i][g]*=other
        else:
            if self.__n == other.__m:
                s=0
                t=[]
                m3=[]
                for z in range(0,self.__m):
                    for j in range(0,other.__n):
                        for i in range(0,self.__n):
                           s+=self.__listAr[z][i]*other.__listAr[i][j]
                        t.append(s)
                        s=0
                    m3.append(t)
                    t=[]
                self.__listAr=m3
        return self

    def __pow__(self,exp):
        if abs(exp) >50:
            print("too big exp, be careful!")
        if exp==0:
            raise Exception("oops, here must be a E matrix")
        else:
            for i in range(exp):
                self.__mul__(self)
        return self
    def __neg__(self):
        return self.__mul__(-1)
a=[
[1,2,3],
[1,3,5],
[6,6,6]
]
b=[
[-9,1,3],
[12,7,1],
[0,10,-5]
]
a=[
[5,0,2,3],
[4,1,5,3],
[3,1,-1,2]
]
b=[
[6],
[-2],
[7],
[4]
]
mat=Matrix(a)
mat2=Matrix(b)
print(mat)
print(mat2)

print(mat*mat2)

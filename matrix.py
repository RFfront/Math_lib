from vector import Vect
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

    def copy(self):
        return Matrix(self.__listAr)

    def __str__(self): #"Matrix obj {}x{}".format(self.__m,self.__n)
        sgr=''
        for i in self.__listAr:
            h=list(map(lambda x:str(x),i))
            sgr+=" ".join(h)
            sgr+="\n"
        return sgr

    def __add__(self, other):
        newMat=self.copy()
        if not isinstance(other,Matrix):
            raise ValueError("you try add not Matrix")
        else:
            if newMat.__n == other.__n and newMat.__m == other.__m:
                for i in range(len(newMat.__listAr)):
                    for g in range(len(newMat.__listAr[i])):
                        newMat.__listAr[i][g]+=other.__listAr[i][g]
            else:
                raise ValueError("you try add Matrix different sizes")
        return newMat

    def __mul__(self, other):
        newMat=self.copy()
        if not isinstance(other,Matrix):
            for i in range(len(newMat.__listAr)):
                for g in range(len(newMat.__listAr[i])):
                    newMat.__listAr[i][g]*=other
        else:
            if newMat.__n == other.__m:
                s=0
                t=[]
                m3=[]
                for z in range(0,newMat.__m):
                    for j in range(0,other.__n):
                        for i in range(0,newMat.__n):
                           s+=newMat.__listAr[z][i]*other.__listAr[i][j]
                        t.append(s)
                        s=0
                    m3.append(t)
                    t=[]
                newMat.__listAr=m3
        return newMat

    def genEMat(self,n=0):
        emat=[]

        def genEma(size):
            tmp=[]
            for i in range(size):
                for g in range(size):
                    if i==g:
                        tmp.append(1)
                    else:
                        tmp.append(0)
                emat.append(tmp.copy())
                tmp.clear()
        if n==0:
            genEma(self.__n)
        else:
            genEma(n)
        return Matrix(emat)

    def __pow__(self,exp):
        if abs(exp) >50:
            print("too big exp, be careful!")
        if exp==0:
            self=self.genEMat()
        else:
            for i in range(exp):
                self.__mul__(self)
        return self

    def __neg__(self):
        return self.__mul__(-1)

    def det(self):
        if self.__n==self.__m:

            def mi2(ar):
                return ar[0][0] * ar[1][1] - ar[1][0] * ar[0][1]
            def mi3(ar):
                return \
                (ar[0][0] * ar[1][1] * ar[2][2]) \
                + (ar[0][1] * ar[1][2] * ar[2][0])\
                + (ar[0][2]*ar[1][0]* ar[2][1])\
                -(ar[0][2]*ar[1][1]*ar[2][0])\
                -(ar[0][0]*ar[1][2]*ar[2][1])\
                -(ar[0][1]*ar[1][0]*ar[2][2])

            def detFind(array):
                if len(array[0])==1:
                    return array[0][0]
                if len(array[0]) == 2:
                    return mi2(array)
                if len(array[0]) > 3:
                    result = 0

                    for i in range(len(array[0])):
                        new_arr = []
                        for j in range(len(array[0])):
                            if j != i:
                                new_arr.append([array[j][k] for k in range(1, len(array[0]))])
                        result += detFind(new_arr) * array[i][0] * (-1 + 2 * ((i + 1) % 2))
                    return result
                else:
                    return mi3(array)
            return detFind(self.__listAr)
        else:
            raise ValueError("Matrix must be square")

    def lux(self):
        newMat=self.copy()
        for i in range(len(newMat.__listAr)):
            for m in range(len(newMat.__listAr)):
                if m>i:
                    vec1=Vect(newMat.__listAr[i])
                    vec2=Vect(newMat.__listAr[m])
                    vec1mul=newMat.__listAr[m][i]
                    vec2mul=newMat.__listAr[i][i]
                    vec3=vec2*vec2mul-vec1*vec1mul
                    newMat.__listAr[m]=vec3.arg
                    print(vec2mul,vec2,'-',vec1mul,vec1,"=",vec3)
                    #print(newMat.__listAr)
        #newMat.__listAr[2]=[0,0,1]

        return newMat



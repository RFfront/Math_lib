import math
class Point:
    def __init__(self,*args):
        self.arg=list(args)
        self.len=len(args)

class Vect:
    def jaje(li):
        new=[]
        for k in range(len(li)):
            if type(li[k])==list:
                new.extend(Vect.jaje(li[k]))
            else:
                new.append(li[k])

        return new

    def __init__(self,*args):
        self.arg=list(args)
        self.arg=Vect.jaje(self.arg)
        self.len=len(args)

    def __add__(self,second):
        if self.len==second.len:
            for i in range(len(second.arg)):
                self.arg[i]+=second.arg[i]
        return self

    def __sub__(self,second):
        new=Vect()
        if self.len==second.len:
            for i in range(len(second.arg)):
                new.arg.append(self.arg[i]-second.arg[i])
        return new

    def __str__(self):
        return str(tuple(self.arg))

    def __mul__(self,second):
        if isinstance(second,Vect):
            if self.len==second.len:
                tmp=[]
                for i in range(len(second.arg)):
                    tmp.append(self.arg[i]*second.arg[i])
                return sum(tmp)
        elif type(second)==int:
            new=Vect()
            for i in range(len(self.arg)):
                new.arg.append(self.arg[i]*second)
            return new

    def llen(self):
        tmp=[]
        for i in range(len(self.arg)):
            tmp.append(self.arg[i]**2)
        from math import sqrt
        return sqrt(sum(tmp))

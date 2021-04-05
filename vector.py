import math
class Point:
    def __init__(self,*args):
        self.arg=list(args)
        self.len=len(args)

class Vect(object):
    def __init__(self,*args):
        self.arg=list(args)
        self.len=len(args)

    def __add__(self,second):
        if self.len==second.len:
            for i in range(len(second.arg)):
                self.arg[i]+=second.arg[i]
        return self

    def __sub__(self,second):
        if self.len==second.len:
            for i in range(len(second.arg)):
                self.arg[i]-=second.arg[i]
        return self

    def __str__(self):
        return str(tuple(self.arg))

    def __mul__(self,second):
        if self.len==second.len:
            tmp=[]
            for i in range(len(second.arg)):
                tmp.append(self.arg[i]*second.arg[i])

        return sum(tmp)
    def llen(self):
        tmp=[]
        for i in range(len(self.arg)):
            tmp.append(self.arg[i]**2)
        from math import sqrt
        return sqrt(sum(tmp))

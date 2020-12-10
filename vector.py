import math
class DV(object):
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k

    def __add__(self,second):
        return DV(self.i+second.i,self.j+second.j,self.k+second.k)
    def __radd__(self,second):
        return DV(self.i+second.i,self.j+second.j,self.k+second.k)

    def __sub__(self,second):
        return DV(self.i-second.i,self.j-second.j,self.k-second.k)

    def __str__(self):
        return "("+str(self.i)+','+str(self.j)+','+str(self.k)+")"
    def sclD(self,second):
        return (self.i*second.i)+(self.j*second.j)+(self.k*second.k)
    def M0d(self):
        return "sqrt("+str((self.i**2)+(self.j**2)+(self.k**2))+")"

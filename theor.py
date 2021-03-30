import decimal      #  импортируем модуль
from decimal import Decimal
from fractions import Fraction
def mult(to,frome=0):
    t=1
    frome+=1
    for i in range(frome,to+1):
        t*=i
    return t

def c(m,n):
    return mult(n,n-m)/mult(m)

def bern(n,p,k):

    decimal.getcontext().prec = 5    #  устанавливаем точность
    re=  Decimal(c(k,n))*   (Decimal(p)**k) *    ((1-Decimal(p))**(n-k) )
    return re

#print(bern(8012322,0.3333333,1233313).quantize(Decimal('1.0000')))
def laplFunc(x):
    import math
    from math import e,pi
    #print(math.exp(0.1))
    #decimal.getcontext().prec = 10
    x=Decimal(x)
    print((Decimal(pi*2).sqrt()))
    ret=(1/(2*Decimal(pi)).sqrt()) * Decimal(e)**((x**2)/2)

    return ret
print(laplFunc(0.09))

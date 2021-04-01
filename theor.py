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
def gaussFoLaplas(x):
    import math
    from math import e,pi
    #print(math.exp(0.1))
    #decimal.getcontext().prec = 10
    x=Decimal(x)

    t=(1/(2*Decimal(pi)).sqrt())
    figulina=((x**2)/2)
    ee=Decimal(e)**figulina
    print(ee)
    ret=t * ee

    return ret

print(gaussFoLaplas(3.99))
def cdf(x):
    """
    Расчет функции Лапласа.
    """
    import numpy as np
    x = x / 1.414213562
    a1 = 0.254829592
    a2 = -0.284496736
    a3 = 1.421413741
    a4 = -1.453152027
    a5 = 1.061405429
    p = 0.3275911

    t = 1 / (1 + p * x)
    b = np.exp(-x * x)
    y = (((((a5 * t + a4) * t) + a3) * t + a2) * t + a1) * t * b
    return (1 - y / 2)-0.5
#print(cdf(2.5))

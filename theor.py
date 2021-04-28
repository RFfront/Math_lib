import decimal      #  импортируем модуль
from decimal import Decimal
from fractions import Fraction
from math import e,pi,exp


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


def gaussFoLaplas(x):

    x=Decimal(x)

    t=(1/(2*Decimal(pi)).sqrt())
    figulina=-((x**2)/2)
    ee=Decimal(e)**figulina
    ret=t * ee
    return ret

def cdf(x):
    x=Decimal(x)
    f=1
    if x<0:
        f*=-1
        x*=-1
    """
    Расчет функции Лапласа.
    """

    x = x / Decimal(1.414213562)
    a1 = Decimal(0.254829592)
    a2 = Decimal(-0.284496736)
    a3 = Decimal(1.421413741)
    a4 = Decimal(-1.453152027)
    a5 = Decimal(1.061405429)
    p = Decimal(0.3275911)

    t = Decimal(1 / (1 + p * x))
    b = Decimal(exp(-x * x))
    y = (((((a5 * t + a4) * t) + a3) * t + a2) * t + a1) * t * b
    return ((1 - y / 2)-Decimal(0.5))*f

def xFoLap(n,p,k):
    q=1-p
    return (k-n*p)/((n*p*q).sqrt())

def laplas(n,p,k,k2=False):
    q=1-p
    decimal.getcontext().prec = 6
    if not k2:
        return (1/((n*p*q).sqrt())*gaussFoLaplas(xFoLap(n,p,k)))

print(laplas(400,Decimal(0.5),225))
print(bern(400,Decimal(0.5),225))

print(cdf(2.5))

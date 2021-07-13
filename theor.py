import decimal      #  импортируем модуль
from decimal import Decimal
from fractions import Fraction
from math import e,pi,exp,sqrt


def mult(to,frome=0):
    t=1
    frome+=1
    for i in range(frome,to+1):
        t*=i
    return t

def c(m,n):
    return mult(n,n-m)/mult(m)

def a(m,n,p):
    if p:return n**m
    else:return mult(5,3)

def bern(n,p,k):
    decimal.getcontext().prec = 5    #  устанавливаем точность
    re=  Decimal(c(k,n))*   (Decimal(p)**k) *    ((1-Decimal(p))**(n-k) )
    return re


def gaussFoLaplas(x):
    x=Decimal(x)

    t=(1/sqrt(2*Decimal(pi)) )
    t=Decimal(t)
    figulina=-((x**2)/2)
    ee=Decimal(e)**figulina
    ee=Decimal(ee)
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
    decimal.getcontext().prec = 9    #  устанавливаем точность

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
    return (k-n*p)/(sqrt(n*p*q))

def laplas(n,p,k,k2=False):
    q=1-p
    decimal.getcontext().prec = 6
    if not k2:
        ga=Decimal(1/(sqrt(n*p*q)))
        return ga*gaussFoLaplas(xFoLap(n,p,k))
    else:
        a=cdf(xFoLap(n,p,k2))
        b=cdf(xFoLap(n,p,k))
        print(a,b)
        return a-b
def puason(n,p,k):
    h=n*p
    #print(h)
    return (h**k)*(e**(-h))/mult(k)

def mF(table):
    sum=0
    for k in table.items():
        sum+=k[0]*k[1]
    return sum

def d(table,m=None):
    if not m:
        m=mF(table)
    sum=0
    for k in table.items():
        sum+=(k[0]**2)*k[1]
    return sum-(m**2)

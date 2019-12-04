from math import *
def lagrange_term(x0,x1,x2,x3,y):
    div = (x0-x1)*(x0-x2)*(x0-x3)
    a = 1/div*y
    b = -(x1+x2+x3)/div*y
    c = (x1*x2+x2*x3+x1*x3)/div*y
    d = -x1*x2*x3/div*y
    
    return a,b,c,d

def lagrange(x0,y0,x1,y1,x2,y2,x3,y3):
    t0x3,t0x2,t0x1,t0x0 = lagrange_term(x0,x1,x2,x3,y0)
    t1x3,t1x2,t1x1,t1x0 = lagrange_term(x1,x0,x2,x3,y1)
    t2x3,t2x2,t2x1,t2x0 = lagrange_term(x2,x0,x1,x3,y2)
    t3x3,t3x2,t3x1,t3x0 = lagrange_term(x3,x0,x1,x2,y3)

    tx3 = t0x3+t1x3+t2x3+t3x3
    tx2 = t0x2+t1x2+t2x2+t3x2
    tx1 = t0x1+t1x1+t2x1+t3x1
    tx0 = t0x0+t1x0+t2x0+t3x0

    return tx3,tx2,tx1,tx0

def findMaxMin(a,b,c):
    if(  b*b-4*a*c < 0):
        return "0","0"
    x1 = (-b+sqrt(b*b-4*a*c))/(2*a)
    x2 = (-b-sqrt(b*b-4*a*c))/(2*a)
    return x1, x2
def findPossibleMaxMin(a,b,c):
    return 3*a, 2*b, c

def isMaximum(a,b,x):
    return 2*a*x+b > 0

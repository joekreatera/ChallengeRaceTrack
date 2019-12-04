import turtle
from lagrangianpolynomial import *
from math import *
"""

x3:5.031886629081145e-05
x2:-0.39943973919899856
x1:1054.8572808054996
x0:-923592.5837511527


"""
def cubic(x,p1,p2,p3,p4):
    return x*x*x*p1+x*x*p2+x*p3+p4



def drawTrack(startX,startY,graphingFunction, p1,p2,p3,p4,startViewX,startViewY,z):
    for i in range(startX, startY):
            x = i
            y = graphingFunction(x,p1,p2,p3,p4)
            painter.pendown()
            painter.goto((i-startViewX)/z,(y-startViewY)/z)
    

def squareDerivativeOnPoint(x,a,b,c):
    return a*x*x + b*x + c

def vecMagnitude(x,y):
    return sqrt(x*x + y*y)

def simulate(x0,y0,x1,y1,x2,y2,x3,y3, startX, startY, graphingFunction,startViewX, startViewY, gDelay,z):

    turtle.Screen().delay(100)
        
    p1,p2,p3,p4 = lagrange(x0,y0,x1,y1,x2,y2,x3,y3)
    ma,mb,mc = findPossibleMaxMin(p1,p2,p3)
    print(p1 , "," , p2, ",",p3 , " " , p4)
    minMax1, minMax2 = findMaxMin(ma,mb,mc)

    if( minMax1 == minMax2 == "0" ):
        print("cannot be done")
    elif( isMaximum(ma,mb,x1) ):
        print("max 1" , minMax1)
        minMaxY1 = cubic(minMax1, p1,p2,p3,p4)-100.0*2
        
    else:
        print("min 1" , minMax1)
        minMaxY1 = cubic(minMax1, p1,p2,p3,p4)
    print("y) 1" , minMaxY1)
        
        
    if( minMax1 == minMax2 == "0" ):
        print("cannot be done")
    elif( isMaximum(ma,mb,x2) ):
        print("max 2" , minMax2)
        minMaxY2 = cubic(minMax2, p1,p2,p3,p4)- 100.0*2
    else:
        print("min 2" , minMax2)
        minMaxY2 = cubic(minMax2, p1,p2,p3,p4)
    print("y) 2" , minMaxY2)

    curveOut = False
    speed = 0.0
    actualX = startX
    actualY = startY
    turtle.tracer(0)
    #for j in range(startX, startY):
    doCrash = False
    while(not curveOut and not doCrash):
        painter.penup()
        #turtle.Screen().delay(0)
        painter.clear()
        drawTrack(startX,startY, graphingFunction, p1,p2,p3,p4,startViewX,startViewY,z)      
        painter.penup()
        actualY = graphingFunction(actualX,p1,p2,p3,p4)
        prevY = graphingFunction(actualX-speed,p1,p2,p3,p4)
        painter.goto((actualX-startViewX)/z,(actualY-startViewY)/z)
        print( ((actualX-startViewX)/z),((actualY-startViewY)/z) )
        painter.dot(14)
        turtle.Screen().update()

        # check if speed can go up
        if( speed  == 0):
            speed = 2
        else:
            # x is the time/speed
            prevX = actualX - speed # one is a very small value for the total scale
            prevSpeedY = squareDerivativeOnPoint(prevX, ma,mb,mc)
            actualSpeedY = squareDerivativeOnPoint(actualX, ma,mb,mc)
            magA = vecMagnitude(1,prevSpeedY) # if f(s) = x then f'(s) = 1
            magB = vecMagnitude(1,actualSpeedY) # also if derivative is slope, then y/1 = y/x then x=1
            axbxayby = (1 + prevSpeedY*actualSpeedY)

            ang = 0
            if abs( axbxayby - magA*magB )< 0.00001:
                ang = 0
            else:
                ang = acos(axbxayby/(magA*magB))

            vx = actualX-prevX
            vy = actualY-prevY
            velocityVector = sqrt(vx*vx + vy*vy )
            kmPerHour = "Speed:" + str((velocityVector/1000)*60*60)
            painter.goto(0,0)
            
            painter.write(kmPerHour)
            #print("Speed calculated as vector (" , kmPerHour ,")" , speed  )
            #print(pi)
            ang = ang*180/pi
            print(ang)
            if( abs(ang) < 5):
                speed = speed*1.2 # speed capability
            elif( abs(ang) > 45):
                speed = speed*0.5 # brake capability
            elif( abs(ang) > 5):
                speed = speed*0.9 # speed capability

            #speed = min(84,speed)
        if( speed > 10 and ang > 10):
            curveOut = True
            doCrash = True
            painter.goto((actualX-startViewX)/z,(actualY-startViewY)/z)
            turtle.Screen().update()
        else:
            actualX = actualX + speed
        if( actualX > x3 ):
            curveOut = True

    painter.pendown()
    if( doCrash ):
        turtle.tracer(0)
        # get y=m(x-x1)+y1
        lastPointX = actualX
        lastPointY = actualY
        m = squareDerivativeOnPoint(lastPointX, ma,mb,mc)
            
        #print("LPX 0 00 0 0 11111 !!!! " , (lastPointX) , " : " , lastPointY)
        #print("LPX FIRST!!!! " , ((lastPointX-startViewX)/z) , " : " , ((lastPointY-startViewY)/z))

        for i in range(0,200):
            lastPointX = lastPointX+5
            lastPointY = lastPointY+5*m
            #print("LPX!!!! " , ((lastPointX-startViewX)/z) , " : " , ((lastPointY-startViewY)/z))

            painter.goto((lastPointX-startViewX)/z,(lastPointY-startViewY)/z)
            painter.color('red')
            painter.dot(5)
            turtle.Screen().update()
            
    print("drawing curves")
    turtle.tracer(0)
    painter.goto((minMax1-startViewX)/z,(minMaxY1-startViewY)/z)
    painter.pendown()
    painter.circle(100/z)
    painter.penup()
    painter.goto((minMax2-startViewX)/z,(minMaxY2-startViewY)/z)
    painter.pendown()
    painter.circle(100/z)
    turtle.Screen().update()
    
offsetX = 1000
offsetY = 1000
x0 = 300; y0 = 500
x3 = 2800; y3 = 2900
x1 = x0+(x3-x0)*.33; y1 = y0+(y3-y0)*.5 +250
x2 = x0+(x3-x0)*.66; y2 = y0+(y3-y0)*.5-200

print(x0,",",y0)
print(x1,",",y1)
print(x2,",",y2)
print(x3,",",y3)


painter = turtle.Turtle()
turtle.Screen().setup(1800,900)
turtle.tracer(0)
painter.pendown()
simulate(x0,y0,x1,y1,x2,y2,x3,y3,300,2800, cubic,x0+offsetX,y0+offsetY,1000, 3 )

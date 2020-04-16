from graphics import *
import operator
import math

win=GraphWin("tap",800,800)
win.setCoords(-400,-400,400,400)
p=Line(Point(0,400),Point(0,-400))
q=Line(Point(400,0),Point(-400,0))
p.setFill('blue')
q.setFill('red')
p.draw(win)
q.draw(win)
win.setBackground("White")

def Scanline(d):
    y=min(d.keys())
    st=[]
    while len(d)!=0 or len(st)!=0:
        if y in d:
            l=d[y]
            for i in l:
                st.append(i)
            del d[y]
        i=0
        for i in range(0,len(st)-1,2):
            x1,x2=st[i][0],st[i+1][0]
            for x in range(math.ceil(x1),int(x2)+1):
                win.plot(math.ceil(x),y,'orange')
        while i<len(st):
            if st[i][1]==y:
                del st[i]
                i-=1
            else:
                st[i][0]=(st[i][0]+st[i][2])
            i+=1
        st.sort()
        y+=1
        

def plotLineLow(x0,y0, x1,y1):
    dx = x1 - x0
    dy = y1 - y0
    yi = 1
    if dy < 0:
        yi = -1
        dy = -dy
    D = 2*dy - dx
    y = y0

    for x in range(x0,x1+1):
        win.plot(x,y,'black')
        if D > 0:
               y = y + yi
               D = D - 2*dx
        D = D + 2*dy

def plotLineHigh(x0,y0,x1,y1):
    dx = x1 - x0
    dy = y1 - y0
    xi = 1
    if dx < 0:
        xi = -1
        dx = -dx
    D = 2*dx - dy
    x = x0

    for y in range(y0,y1+1):
        win.plot(x,y,'black')
        if D > 0:
               x = x + xi
               D = D - 2*dy
        D = D + 2*dx

def plotLine(x0,y0,x1,y1):
    if abs(y1 - y0) < abs(x1 - x0):
        if x0 > x1:
            plotLineLow(x1, y1, x0, y0)
        else:
            plotLineLow(x0, y0, x1, y1)
    else:
        if y0 > y1:
            plotLineHigh(x1, y1, x0, y0)
        else:
            plotLineHigh(x0, y0, x1, y1)

def DrawPolygon(points):
    for i in range(len(points)-1):
	    x0,y0=points[i]
	    x1,y1=points[i+1]
	    plotLine(x0,y0,x1,y1)
    x0,y0=points[-1]
    x1,y1=points[0]
    plotLine(x0,y0,x1,y1)

points=[]
n=int(input("Enter number of points for Polygon: "))
for i in range(n):
    x,y=map(int,input('Enter point: ').split())
    points.append((x,y))
print(points)
DrawPolygon(points)

d={}
for i in range(len(points)):
    x0,y0=points[i]
    x1,y1=points[(i+1)%len(points)]
    if y0!=y1:
        y=min(y1,y0)
        dm=(x1-x0)/(y1-y0)
        if y==y0:
            d[y]=d.get(y,[])+[[x0,y1,dm]]
        else:
            d[y]=d.get(y,[])+[[x1,y0,dm]]
        d[y].sort()
d=dict(sorted(d.items(), key=operator.itemgetter(0)))
for i in d.keys():
    print(i)
print(d)
Scanline(d)

win.getMouse()
win.close()        

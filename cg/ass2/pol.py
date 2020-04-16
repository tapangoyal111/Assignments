from graphics import *
import sys 
  
# the setrecursionlimit function is 
# used to modify the default recursion 
# limit set by python. Using this,  
# we can increase the recursion limit 
# to satisfy our needs 
  
sys.setrecursionlimit(10**6) 

def drawline(x1,y1,x2,y2,win):
    l=Line(Point(x1,y1),Point(x2,y2))
    l.setFill("red")
    l.setWidth(5)
    l.draw(win)
    
winx,winy=0,0    
    
alreadyFilled={}    
    
def drawline(x0,y0,x1,y1,win):
    if(x1-x0 == 0):
        slope = None
        (x0,y0) = (y0,x0)
        (x1,y1) = (y1,x1)
    else:
        slope = (y1-y0)/(x1-x0)
        if(slope >= 0) and (abs(slope) > 1):
            (x0,y0),(x1,y1) = (y0,x0),(y1,x1)
        elif(slope < 0) and (abs(slope) <= 1):
            (x0,y0),(x1,y1) = (-x0,y0),(-x1,y1)
        elif(slope < 0) and (abs(slope) > 1):
            (x0,y0),(x1,y1) = (y0,-x0),(y1,-x1)
    if(x0 > x1):
        (x0,y0),(x1,y1) = (x1,y1),(x0,y0)
        
    dy = y1 - y0 ; dx = x1 - x0
    a = dy ; b = -dx
    del_E = a ; del_NE = a + b
    d = a + (b/2)
    x = x0 ; y = y0
    while(x <= x1):
        if(slope is None):
            (xp,yp) = (y,x)
        elif(slope >= 0) and (abs(slope) > 1):
            (xp,yp) = (y,x)
        elif(slope < 0) and (abs(slope) <= 1):
            (xp,yp) = (-x,y)
        elif(slope < 0) and (abs(slope) > 1):
            (xp,yp) = (-y,x)
        else:
            (xp,yp) = (x,y)
        win.plotPixel(xp ,yp,"red")
        alreadyFilled[(xp,yp)]=1
        
        if(d<0):	#East
            d = d + del_E
            
        else:		#North -East
            d = d + del_NE
            y = y + 1
        x = x + 1
    
def polygon_draw():
    global winx,winy
    n=int(input("Enter No. Of Side : "))
    a=[]
    print("Enter length,width Of Window ")
    winx,winy=map(int,input().split())
    win=GraphWin("tap",winx,winy)
    win.setBackground("orange")
        
    for i in range(n):
        print("Enter Point ",i+1)
        a.append(list(map(int,input().split())))
    
    for i in range(n):
        drawline(a[i][0],a[i][1],a[(i+1)%n][0],a[(i+1)%n][1],win)
    
    print("Enter Any Strictly Interior Point : ")
    x,y=map(int,input().split())
    st=[(x,y)]
    
    while st:
        print(st)
        x,y=st.pop(0)
        win.plotPixel(x,y,"red")
        alreadyFilled[(x,y)]=1
        if (x+1,y) not in alreadyFilled:
            alreadyFilled[(x+1,y)]=1
            st.append((x+1,y))
        if (x-1,y) not in alreadyFilled:
            st.append((x-1,y))
            alreadyFilled[(x-1,y)]=1
        if (x,y+1) not in alreadyFilled:
            st.append((x,y+1))
            alreadyFilled[(x,y+1)]=1
        if (x,y-1) not in alreadyFilled:
            st.append((x,y-1))
            alreadyFilled[(x,y-1)]=1
    
    win.getMouse()
    win.close()  
        
    
polygon_draw()


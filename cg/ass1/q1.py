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
    d={}    
    ymin=10**12
    ymax=-10**12
    
    for i in range(n):
        print("Enter Point ",i+1)
        a.append(list(map(int,input().split())))
        ymin=min(ymin,a[-1][1])
        ymax=max(ymax,a[-1][1])
    for i in range(n):
        drawline(a[i][0],a[i][1],a[(i+1)%n][0],a[(i+1)%n][1],win)
        x1,y1,x2,y2=a[i][0],a[i][1],a[(i+1)%n][0],a[(i+1)%n][1]
        islope=0
        if (y1!=y2):
            islope=(x2-x1)/(-y2+y1)
            m=min(y1,y2)
            if m==y1:
                d[m]=d.get(m,[]) + [[x1,y2,-islope]]
            else:
                d[m]=d.get(m,[]) + [[x2,y1,-islope]]

    
    print((d))
    b=list(d.keys())
    b.sort()
    st=[]
    
    for i in range(ymin,ymax+ 1):
        st1=[]
        for j in d.get(i,[]):
            st1.append(j)
        for j in st:
            if j[1]!=i:
                st1.append([j[0]+j[2],j[1],j[2]])
        st=st1[:]
        st.sort()
        par=True
        for j in range(len(st)-1):
            if par:
                drawline(st[j][0],i,st[j+1][0],i,win)
            par=not par
                
        print(i,st)
                 
        
    win.getMouse()
    win.close()
polygon_draw()


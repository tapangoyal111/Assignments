from graphics import *
window = (0,0,0,0)
viewport = (0,0,0,0)

def winToViewPort(xw,yw,win):
    (xw_min,yw_min,xw_max,yw_max) = window
    (xv_min,yv_min,xv_max,yv_max) = viewport
    xv = (xw - xw_min)/(xw_max - xw_min)*(xv_max - xv_min) + xv_min
    xv = round(xv)
    
    yv = (yw - yw_min)/(yw_max - yw_min)*(yv_max - yv_min) + yv_min
    yv = yv_max - yv
    yv = round(yv)
    win.plotPixel(xv,yv,"black")

def drawLine(x0,y0,x1,y1,win):
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
        winToViewPort(xp,yp,win)
        
        if(d<0):	#East
            d = d + del_E
            
        else:		#North -East
            d = d + del_NE
            y = y + 1
        x = x + 1

def main():
    global viewport,window
    print("Enter length of viewport : ")
    x = int(input())
    print("Enter width of viewport : ")
    y = int(input())
    viewport = (0,0,x,y)
    win = GraphWin("Bresenham Line Generation",x,y)
    win.setBackground("orange")
    print("Enter xw_min,yw_min,xw_max,yw_max : ")
    xw_min,yw_min,xw_max,yw_max = map(int,input().split())
    if(xw_min>xw_max):
        (xw_max,yw_max),(xw_min,yw_min)=(xw_min,yw_min),(xw_max,yw_max)
    if(yw_min>yw_max):
        (yw_min,yw_max) = (yw_max,yw_min)
    
    win.setCoords(xw_min,yw_min,xw_max,yw_max)
    window = (xw_min,yw_min,xw_max,yw_max)
        
    print("Enter Point 1 for line : ")
    (x0,y0) = (map(int,input().split()))
    print("Enter Point 2 for line : ")
    
    (x1,y1) = (map(int,input().split()))
    drawLine(x0,y0,x1,y1,win)
    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()

'''Ellipse'''
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

def plotpts(x,y,a,b,color,win):
    winToViewPort(x+a,y+b,win)
    winToViewPort(-x+a,y+b,win)
    winToViewPort(x+a,-y+b,win)
    winToViewPort(-x+a,-y+b,win)
    
def plotEllipse(a,b,x0,y0,win):
    x = 0 ; y = b;
    d1 = (b**2) - ((a**2)*b) + (0.25*(a**2))
    dx = 2*(b**2)*x
    dy = 2*(a**2)*y
    # For Area 1
    while (dx < dy):
        plotpts(x,y,x0,y0,"black",win)
        if (d1 < 0):
            dx = dx + (2 * b * b)
            d1 = d1 + dx + (b * b)
        else:
            y=y-1;
            dx = dx + (2 * b * b)
            dy = dy - (2 * a * a)
            d1 = d1 + dx - dy + (b * b)
        x=x+1

    d2 = ((b**2) * ((x + 0.5) * (x + 0.5))) + \
    ((a**2) * ((y - 1) * (y - 1))) - \
    ((a**2) * (b**2))
    # For Area 2
    while (y >= 0):
        plotpts(x,y,x0,y0,"black",win)
        if (d2 > 0):
            dy = dy - (2 * (a**2))
            d2 = d2 + (a**2) - dy
        else:
            x=x+1
            dx = dx + (2 * (b**2))
            dy = dy - (2 * (a**2))
            d2 = d2 + dx - dy + (a**2)
        y=y-1

def main():
    print("Enter length of viewport : ",end="") ; x = int(input())
    print("Enter width of viewport : ",end="") ; y = int(input())
    viewport = (0,0,x,y)
    win = GraphWin("Scan Conversion of Ellipse",x,y)
    win.setBackground(color_rgb(195, 141, 158))
    
    print("Enter xw_min,yw_min,xw_max,yw_max : ")
    xw_min,yw_min,xw_max,yw_max = map(int,input().split())
    
    if(xw_min>xw_max):
        (xw_max,yw_max),(xw_min,yw_min)=(xw_min,yw_min),(xw_max,yw_max)
    if(yw_min>yw_max):
        (yw_min,yw_max) = (yw_max,yw_min)
    win.setCoords(xw_min,yw_min,xw_max,yw_max)
    window = (xw_min,yw_min,xw_max,yw_max)
    print("Enter mid-Point of ellipse(x space y) : ",end="")
    (x0,y0) = (map(int,input().split()))
    print("Enter semi-major axis of ellipse : ",end="")
    a = int(input())
    print("Enter semi-minor axis of ellipse : ",end="")
    b = int(input())
    plotEllipse(a,b,x0,y0,win)
    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()


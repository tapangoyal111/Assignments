from graphics import *
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

xmin,xmax,ymin,ymax=map(int,input('Enter co-ordinates of rectangle(xmin,xmax,ymin,ymax): ').split())
rectangle=Rectangle(Point(xmin,ymin),Point(xmax,ymax))
rectangle.draw(win)

x0,y0,x1,y1=map(int,input('Enter co-ordinates of line(x0,y1,x1,y1): ').split())
line=Line(Point(x0,y0),Point(x1,y1))
line.draw(win)

line.setOutline('red')
if(x0==x1 and y0==y1):
        print("line is degenerate so clip as a point")
        
else:
        te=0.0
        tl=1.0
        
        #left
        if(x1-x0 !=0):
                t=(x0-xmin)/(x0-x1)
                print("left")
                
                if(-(x1-x0)<0):
                        te=max(te,t)
                        
                else:
                        tl=min(tl,t)
                
        
                
        #bottom
        if(y1-y0 !=0):
                t=(y0-ymin)/(y0-y1)
                print("bottom")
                
                if(-(y1-y0)<0):
                        te=max(te,t)
                        
                else:
                        tl=min(tl,t)
                
        #top
        if(y1-y0 !=0):
                t=(y0-ymax)/(y0-y1)
                print("top")
                
                if((y1-y0)<0):
                        te=max(te,t)
                        
                else:
                        tl=min(tl,t)
                
        #right
        if(x1-x0 !=0):
                t=(x0-xmax)/(x0-x1)
                print("right")
                
                if((x1-x0)<0):
                        te=max(te,t)
                        
                else:
                        tl=min(tl,t)
                        
                
if(te>tl):
        print("no clipping")
        
else:
        x0=x0+(x1-x0)*te
        y0=y0+(y1-y0)*te
        x1=x0+(x1-x0)*tl
        y1=y0+(y1-y0)*tl
        
        print(x0)  
        print(y0) 
        print(x1) 
        print(y1) 
        
        line=Line(Point(x0,y0),Point(x1,y1))
        line.draw(win)
        line.setOutline('green')

                
win.getMouse()
win.close()
                
                
                
                
                
                
                
                

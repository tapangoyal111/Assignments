from graphics import *
def drawpt(x,y,win):
    l=Point(x,y)
    l.setFill("red")
    l.draw(win)
    

    
def main_cir():
    print("Enter Length,Width Of Window")
    winx,winy=map(int,input().split())
    win=GraphWin("tap",winx,winy)
    win.setBackground("orange")
    print("Enter Co-ordinate Of Center Of Circle ")
    x1,y1=map(int,input().split())
    print("Enter Radius Of Circle ")
    R=int(input())
    d=5/4 -R
    x=0

    y=R
    
    while x<y:
        if d<0:
            x+=1
            d+= 2*x + 3
        else:
            x+=1
            y-=1
            d+= (2*x -2*y  + 5)
        drawpt(x+x1,-y+y1,win)                 
        drawpt(-x + x1,(-y) + y1,win)
        drawpt(x+x1,+y+y1,win)                 
        drawpt(-x + x1,(+y) + y1,win)
        drawpt(-y+y1,x+x1,win)                 
        drawpt((-y) + y1,-x + x1,win)
        drawpt(+y+y1,x+x1,win)                 
        drawpt((+y) + y1,-x + x1,win)
    win.getMouse()
    win.close()  

if __name__ == '__main__':
    main_cir()
    

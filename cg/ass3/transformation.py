
from graphics import *
import sys 
from math import cos as cos
from math import sin as sin

pi=3.141592654
    
def matmul(a,b):
	p,q,r=len(a),len(b[0]),len(b)
	c=[[0 for i in range(r)] for j in range(p)]
	for i in range(p):
		for j in range(r):
			s=0
			for k in range(q):
				s+=a[i][k]*b[k][j]
			c[i][j]=s
	return c

	
def drawline(x0,y0,x1,y1,win,col):
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
        p=Point(xp ,yp)    
        p.setFill(col)
        p.draw(win)
        
        if(d<0):	#East
            d = d + del_E
            
        else:		#North -East
            d = d + del_NE
            y = y + 1
        x = x + 1


def main():
	win=GraphWin("Xformation",800,800)
	win.setCoords(-400,-400,400,400)
	drawline(-400,0,400,00,win,'black')			#X-Axis
	drawline(0,-400,000,400,win,"black")		#Y-Axis
	
	print("This Window Has Co-ordinate -400 to 400 In Both X and Y")
	print("Enter The Number of vertices")
	numberOfVertices=int(input())
	pts=[]
	for i in range(numberOfVertices):
		print("Enter Coordinate for vertex",i+1)
		x,y=map(int,input().split())
		pts.append([x,y])
		
	for i in range(numberOfVertices):
		drawline(pts[i][0],pts[i][1],pts[(i+1)%numberOfVertices][0],pts[(i+1)%numberOfVertices][1],win,"red")
	
	print("Press 1 for Translation")
	print("Press 2 for Rotation About Origin")
	print("Press 3 for Scaling")
	
	task=int(input())
	if (task==1):
		trans(pts,win)
	elif (task==2):
		rotation(pts,win)
	elif (task==3):
		scaling(pts,win)
	
	win.getMouse()
	win.close()
        
def trans(pts,win):
	print("Enter translatinf factor in Both X and Y")
	tx,ty=map(int,input().split())
	ptnew=[]
	mat=[[1,0,1],[0,1,1],[tx,ty,1]]
	for i in pts:
		ptnew.append(matmul([[i[0],i[1],1]],mat))
	numberOfVertices=len(pts)
	print(ptnew)	
	for i in range(len(pts)):
		drawline(ptnew[i][0][0],ptnew[i][0][1],ptnew[(i+1)%numberOfVertices][0][0],ptnew[(i+1)%numberOfVertices][0][1],win,"blue")
	        
def rotation(pts,win):
	print("Enter Rotating angle(In degree) and Direction (-1 for ClockWise and 1 for AnticlockWise)")
	theeta,di=map(int,input().split())
	ptnew=[]
	theeta*=(pi/180)
	mat=[[cos(theeta),sin(theeta*di),0],[-sin(theeta*di),cos(theeta*di),0],[0,0,1]]
	for i in pts:
		ptnew.append(matmul([[i[0],i[1],1]],mat))
	numberOfVertices=len(pts)
	print(ptnew)	
	for i in range(len(pts)):
		drawline(ptnew[i][0][0],ptnew[i][0][1],ptnew[(i+1)%numberOfVertices][0][0],ptnew[(i+1)%numberOfVertices][0][1],win,"blue")
	        
        
def scaling(pts,win):
	print("Enter Scaling factor in Both X and Y")
	sx,sy=map(int,input().split())
	ptnew=[]
	mat=[[sx,0,0],[0,sy,0],[0,0,1]]
	for i in pts:
		ptnew.append(matmul([[i[0],i[1],1]],mat))
	numberOfVertices=len(pts)
	print(ptnew)	
	for i in range(len(pts)):
		drawline(ptnew[i][0][0],ptnew[i][0][1],ptnew[(i+1)%numberOfVertices][0][0],ptnew[(i+1)%numberOfVertices][0][1],win,"blue")
		
	
main()


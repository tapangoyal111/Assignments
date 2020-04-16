from graphics import *
import sys 
from math import cos as cos
from math import sin as sin
pi=3.141592654

# pts=[]
    
def drawaxis(win):
	drawline(-400,0,400,00,win,'black')			#X-Axis
	drawline(0,-400,000,400,win,"black")		#Y-Axis
	
	    
    
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
	# global pts
	win=GraphWin("Xformation",800,800)
	win.setCoords(-400,-400,400,400)
	drawaxis(win)
	win.setBackground("white")
	# drawline(-400,0,400,00,win,'black')			#X-Axis
	# drawline(0,-400,000,400,win,"black")		#Y-Axis
	pts=[]
	print("This Window Has Co-ordinate -400 to 400 In Both X and Y")
	print("Enter The Number of vertices")
	numberOfVertices=int(input())
	
	for i in range(numberOfVertices):
		print("Enter Coordinate for vertex",i+1)
		x,y=map(int,input().split())
		pts.append([x,y])
		
	for i in range(numberOfVertices):
		drawline(pts[i][0],pts[i][1],pts[(i+1)%numberOfVertices][0],pts[(i+1)%numberOfVertices][1],win,"red")
	
	while (True):
		print("Press X for Reflection About X axis")
		print("Press Y for Reflection About Y axis")
		print("Press S for Scaling")
		print("Press -> or <- or up or Down key for Translation")
		print("Press R for Rotation")
		print("Press Q for Exit")
		
		k=win.getKey()
		if k in 'XY':
			pts=ref(win,pts,k)
		elif k=="R":
			pts=rotation(win,pts,k)
		elif k=="S":
			pts=scaling(win,pts,k)
		elif k in ["Up","Right","Left","Down"]:
			pts=trans(win,pts,k)
		elif k=='Q':
			win.close()
			break
		else:	
			print("Press Valid Key")
		
	
def trans(win,pts,k):
	fx=0;fy=0
	if k=="Up":
		fy=1
	elif k=="Down":
		fy=-1
	elif k=="Left":
		fx=-1
	elif k=="Right":
		fx=1
	
	x,y=50*fx,50*fy
	ptnew=[]
	mat=[[1,0,0],[0,1,0],[x,y,1]]
	numberOfVertices=len(pts)
	for i in range(numberOfVertices):
		drawline(pts[i][0],pts[i][1],pts[(i+1)%numberOfVertices][0],pts[(i+1)%numberOfVertices][1],win,"white")
	drawaxis(win)
	for i in pts:
		ptnew.append(matmul([[i[0],i[1],1]],mat))
	pt1=[]	
	# print(ptnew)	
	
	for i in range(len(pts)):
		drawline(ptnew[i][0][0],ptnew[i][0][1],ptnew[(i+1)%numberOfVertices][0][0],ptnew[(i+1)%numberOfVertices][0][1],win,"red")
		pt1.append([ptnew[i][0][0],ptnew[i][0][1]])
		
	return pt1
	        
def ref(win,pts,k):
	# global pts
	if k=="X":
		x,y,theeta=0,0,0
	else:
		x,y,theeta=0,0,90
			
	ptnew=[]
	theeta*=(pi/180)
	mat1=[[1,0,0],[0,1,0],[-x,-y,1]]
	mat2=[[cos(theeta),-sin(theeta),0],[sin(theeta),cos(theeta),0],[0,0,1]]
	mat3=[[1,0,0],[0,-1,0],[0,0,1]]
	mat4=[[cos(theeta),sin(theeta),0],[-sin(theeta),cos(theeta),0],[0,0,1]]
	mat5=[[1,0,0],[0,1,0],[x,y,1]]
	mat=matmul(matmul(matmul(matmul(mat1,mat2),mat3),mat4),mat5)
	numberOfVertices=len(pts)
	
	for i in range(numberOfVertices):
		drawline(pts[i][0],pts[i][1],pts[(i+1)%numberOfVertices][0],pts[(i+1)%numberOfVertices][1],win,"white")
	drawaxis(win)
	for i in pts:
		ptnew.append(matmul([[i[0],i[1],1]],mat))
	pt1=[]	
	# print(ptnew)	
	
	for i in range(len(pts)):
		drawline(ptnew[i][0][0],ptnew[i][0][1],ptnew[(i+1)%numberOfVertices][0][0],ptnew[(i+1)%numberOfVertices][0][1],win,"red")
		pt1.append([ptnew[i][0][0],ptnew[i][0][1]])
		
	return pt1
	        
def rotation(win,pts,k):
	# global pts
	x,y,theeta=0,0,45
	ptnew=[]
	theeta*=(pi/180)
	
	mat1=[[1,0,0],[0,1,0],[-x,-y,1]]
	mat2=[[cos(theeta),sin(theeta),0],[-sin(theeta),cos(theeta),0],[0,0,1]]
	mat3=[[1,0,0],[0,1,0],[x,y,1]]
	mat=matmul(matmul(mat1,mat2),mat3)
	
	for i in pts:
		ptnew.append(matmul([[i[0],i[1],1]],mat))
	numberOfVertices=len(pts)
	for i in range(numberOfVertices):
		drawline(pts[i][0],pts[i][1],pts[(i+1)%numberOfVertices][0],pts[(i+1)%numberOfVertices][1],win,"white")
	drawaxis(win)
	pt1=[]
	print(ptnew)	
	for i in range(len(pts)):
		drawline(ptnew[i][0][0],ptnew[i][0][1],ptnew[(i+1)%numberOfVertices][0][0],ptnew[(i+1)%numberOfVertices][0][1],win,"RED")
		pt1.append([ptnew[i][0][0],ptnew[i][0][1]])
	return pt1        
        
def scaling(win,pts,k):
	# global pts
	print("Enter Scaling factor in Both X and Y")
	
	sx,sy=2,2
	ptnew=[]
	mat=[[sx,0,0],[0,sy,0],[0,0,1]]
	for i in pts:
		ptnew.append(matmul([[i[0],i[1],1]],mat))
	numberOfVertices=len(pts)
	for i in range(numberOfVertices):
		drawline(pts[i][0],pts[i][1],pts[(i+1)%numberOfVertices][0],pts[(i+1)%numberOfVertices][1],win,"white")
	drawaxis(win)
	pt1=[]
	
	print(ptnew)	
	for i in range(len(pts)):
		drawline(ptnew[i][0][0],ptnew[i][0][1],ptnew[(i+1)%numberOfVertices][0][0],ptnew[(i+1)%numberOfVertices][0][1],win,"RED")
		pt1.append([ptnew[i][0][0],ptnew[i][0][1]])
	return pt1
main()


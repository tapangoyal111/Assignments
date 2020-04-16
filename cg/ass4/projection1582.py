import numpy as np
from graphics import *
import math

def clear(self):
        for item in self.items[:]:
            item.undraw()
            #item.draw(self)
        self.update()

mat2=np.array([[1,0,0,0],[0,1,0,0],[0,0,0,0],[0,0,0,1]])

def iso_projection(win, coordinates):
    return np.dot(np.dot(coordinates,np.array([[2/3,-1/3,1/3,0],[-1/3,2/3,-1/3,0],[-1/3,-1/3,2/3,0],[0,0,0,1]])),mat2)

def di_projection(win,coordinates):
    return np.dot(np.dot(coordinates,np.array([[5/6,-1/6,-1/3,0],[-1/6,5/6,-1/3,0],[-1/3,-1/3,1/3,0],[0,0,0,1]])),mat2)

def tri_projection(win,coordinates):
    return np.dot(np.dot(coordinates,np.array([[13/14,-1/14,-1/14,0],[-1/7,6/7,-1/7,0],[-3/14,-3/14,11/14,0],[0,0,0,1]])),mat2)

def gen_projection(win,coordinates,f):
    matrix2=np.array([[1,0,0,0],[0,1,0,0],[math.cos(math.pi/4)*f,math.sin(math.pi/4)*f,0,0],[0,0,0,1]])
    return np.dot(coordinates,matrix2)

def oPP(win,coordinates):
    return np.dot(coordinates,np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1/100],[0,0,0,1]]))

def tPP(win,coordinates):
    return np.dot(coordinates,np.array([[1,0,0,0],[0,1,0,0],[-1,0,0,1/100],[0,0,0,1]]))

def thPP(win,coordinates):
    return np.dot(coordinates,np.array([[1,0,0,0],[0,1,0,0],[-1,-1,0,1/100],[0,0,0,1]]))

def orth_projection(win,coordinates):
    return np.dot(coordinates,np.array([[1,0,0,0],[0,1,0,0],[0,0,0,0],[0,0,0,1]]) )

def plotCube(win,res):
    for i in range(0,4):
        P11=Point(res[i][0]/res[i][3],res[i][1]/res[i][3])
        P22=Point(res[(i+1)%4][0]/res[(i+1)%4][3],res[(i+1)%4][1]/res[(i+1)%4][3])
        L=Line(P11,P22)
        L.draw(win)
        P33=Point(res[i + 4][0]/res[i+4][3],res[i + 4][1]/res[i+4][3])
        P44=Point(res[((i+1)%4)+4][0]/res[((i+1)%4)+4][3],res[((i+1)%4)+4][1]/res[((i+1)%4)+4][3])
        L = Line(P33,P44)
        L.draw(win)
        L = Line(P11,P33)
        L.draw(win)
        L = Line(P22,P44)

def drawAxis(win,X1,X2,Y1,Y2):
    L = Line(Point(X1,0),Point(X2,0))
    L.draw(win)
    L.setOutline('black')
    L = Line(Point(0,Y1),Point(0,Y2))
    L.draw(win)
    L.setOutline('green')

def main():
    WIN_X,WIN_Y = 1000,1000
    X1,X2,Y1,Y2 = -WIN_X//2,WIN_X//2,-WIN_Y//2,WIN_Y//2
    win=GraphWin("drawLine",WIN_X,WIN_Y )
    win.setCoords(X1,Y1,X2,Y2)
    drawAxis(win,X1,X2,Y1,Y2)
    coordinates = np.array([[0,0,0,1],[100,0,0,1],[100,100,0,1],[0,100,0,1],[0,0,100,1],[100,0,100,1],[100,100,100,1],[0,100,100,1]])
    print("Press these keys for projections: ")
    print("Press 'i' for isometric")
    print("Press 'd' for dimetric")
    print("Press 't' for trimetric")
    print("Press 'o' for orthographic")
    print("Press 'shift_L' for cavalier")
    print("Press 'shift_R' for cabinet")
    print("Press 'g' for general")
    print("Press 'Control_L' for onePointPerspective")
    print("Press 'space' for twoPointPerspective")
    print("Press 'Control_R for threePointPerspective'")
    print("Click anywhere on windows for exit")
    while(True):
        key = win.getKey()
        if(key == 'i'):
            clear(win)
            drawAxis(win,X1,X2,Y1,Y2)
            res = iso_projection(win, coordinates)
            plotCube(win,res)
        elif(key == 'd'):
            clear(win)
            drawAxis(win,X1,X2,Y1,Y2)
            res = di_projection(win,coordinates)
            plotCube(win,res)
        elif(key == 't'):
            clear(win)
            drawAxis(win,X1,X2,Y1,Y2)
            res = tri_projection(win,coordinates)
            plotCube(win,res)
        elif(key == 'Shift_L'):
            clear(win)
            drawAxis(win,X1,X2,Y1,Y2)
            res = gen_projection(win,coordinates,1)
            plotCube(win,res)
        elif(key == 'Shift_R'):
            clear(win)
            drawAxis(win,X1,X2,Y1,Y2)
            res = gen_projection(win,coordinates,1/2)
            plotCube(win,res)
        elif(key == 'g'):
            clear(win)
            drawAxis(win,X1,X2,Y1,Y2)
            res = gen_projection(win,coordinates,1/math.tan(math.pi/3))
            plotCube(win,res)
        elif(key == 'Control_L'):
            clear(win)
            drawAxis(win,X1,X2,Y1,Y2)
            res = oPP(win,coordinates)
            plotCube(win,res)
        elif(key == 'space'):
            clear(win)
            drawAxis(win,X1,X2,Y1,Y2)
            res = tPP(win,coordinates)
            plotCube(win,res)
        elif(key == 'Control_R'):
            clear(win)
            drawAxis(win,X1,X2,Y1,Y2)
            res = thPP(win,coordinates)
            plotCube(win,res)
        elif(key == 'o'):
            clear(win)
            drawAxis(win,X1,X2,Y1,Y2)
            res = orth_projection(win,coordinates)
            plotCube(win,res)
        else:
            print(key)
            break
    win.getMouse()
    win.close()
main()

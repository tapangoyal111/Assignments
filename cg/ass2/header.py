from graphics import *

def plotPoints(win, l, color = "black", screen=None, c=0):
	
	for i in l:
		win.plot(i[0], i[1], color)
		if screen:
			screen[i[0]][i[1]] = c

def drawline(win, x1, y1, x2, y2, color = "black", screen=None, c = 0):
	
	l = []
	
	if x1 == x2:
		for i in range(min(y1,y2), max(y1, y2)+1):
			l.append((x1, i))
		plotPoints(win, l, color,screen,c)
		return
	
	cond = float(y2-y1)/(x2-x1)
	
	if cond > 1.0:
		x1,y1 = y1,x1
		x2,y2 = y2,x2
	elif cond <= -1.0:
		x1,y1,x2,y2 = -x1,y1,-x2,y2
		x1,y1 = y1,x1
		x2,y2 = y2,x2
	elif cond < 0 and cond > -1.0:
		x1,y1,x2,y2 = -x1,y1,-x2,y2
	if x1 > x2:
		x1,x2,y1,y2 = x2,x1,y2,y1
	dy = (y2-y1)
	dx = (x2-x1)
	m = dy/float(dx)
	a = dy
	b = -dx
	d = 2*a + b
	dne = 2*(a+b)
	de = 2*a
	x0,y0 = x1,y1
	
	while x0<=x2:
		l.append((x0,y0))
		if d>=0:
			d += dne
			y0 += 1
		else :
			d += de
		x0 += 1
	

	if cond > 1.0:
		l = [(i[1],i[0]) for i in l]     # (x = y)

	elif cond <= -1.0:
		l = [(i[1], i[0]) for i in l]    # first swap  (x=y)
		l = [(-i[0],i[1]) for i in l]    # than negate (y-axis)
	elif cond < 0 and cond > -1.0:
		l = [(-i[0], i[1]) for i in l]   # y-axis

	plotPoints(win, l, color, screen, c)


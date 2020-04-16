from graphics import *
import operator
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

inside=0 #0000 
left=1 #0001 
right=2 #0010 
bottom=4 #0100 
top=8	 #1000 

x_min,x_max,y_min,y_max=map(int,input('Enter co-ordinates of rectangle(x_min,x_max,y_min,y_max): ').split())
rectangle=Rectangle(Point(x_min,y_min),Point(x_max,y_max))
rectangle.draw(win)

def computeCode(x, y): 
	code = inside
	if x < x_min: 
		code |= left 
	elif x > x_max: 
		code |= right 
	if y < y_min: 
		code |= bottom 
	elif y > y_max: 
		code |= top 

	return code 
 
def cohenSutherlandClip(x1, y1, x2, y2): 
 
	code1 = computeCode(x1, y1) 
	code2 = computeCode(x2, y2) 
	accept = False

	while True: 

		# If both endpoints lie within rectangle 
		if code1 == 0 and code2 == 0: 
			accept = True
			break

		# If both endpoints are outside rectangle 
		elif (code1 & code2) != 0: 
			break

		# Some segment lies within the rectangle 
		else:  
			x = 1.0
			y = 1.0
			if code1 != 0: 
				code_out = code1 
			else: 
				code_out = code2 

			# Find intersection point 
			# using formulas y = y1 + slope * (x - x1), 
			# x = x1 + (1 / slope) * (y - y1) 
			if code_out & top: 
				x = x1 + ((x2 - x1) / (y2 - y1)) * (y_max - y1) 
				y = y_max 

			elif code_out & bottom: 
				x = x1 + ((x2 - x1) / (y2 - y1)) * (y_min - y1) 
				y = y_min 

			elif code_out & right:  
				y = y1 + ((y2 - y1) / (x2 - x1)) * (x_max - x1) 
				x = x_max 

			elif code_out & left:  
				y = y1 + ((y2 - y1) / (x2 - x1)) * (x_min - x1) 
				x = x_min 
 
			if code_out == code1: 
				x1 = x 
				y1 = y 
				code1 = computeCode(x1,y1) 

			else: 
				x2 = x 
				y2 = y 
				code2 = computeCode(x2, y2) 

	if accept: 
		print ("Line accepted from %.2f,%.2f to %.2f,%.2f" % (x1,y1,x2,y2)) 
		line=Line(Point(x1,y1),Point(x2,y2))
		line.draw(win)
		line.setOutline('black')
	else: 
		print("Line rejected") 

x1,y1,x2,y2=map(int,input('Enter co-ordinates of line(x1,y1,x2,y2): ').split())
line=Line(Point(x1,y1),Point(x2,y2))
line.draw(win)
line.setOutline('red')

cohenSutherlandClip(x1,y1,x2,y2) 

win.getMouse()
win.close()

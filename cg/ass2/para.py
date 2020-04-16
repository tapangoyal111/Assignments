from header import *

directions = ['left', 'bottom', 'right', 'top']
normals = {'left': [-1, 0], 'bottom': [0, -1], 'right': [1, 0], 'top':[0, 1]}

def dot(a, b):
	n = len(a)
	if n == len(b):
		temp = 0
		for i in range(n):
			temp += a[i]*b[i]
		return temp
def pClip(lines, clip_rec):
	wxmin, wymin, wxmax, wymax = clip_rec[0], clip_rec[1], clip_rec[2], clip_rec[3]
	pe = {'left': [wxmin, wymin], 'bottom': [wxmin, wymin], 'right': [wxmax, wymax], 'top': [wxmax, wymax]}
	finalLines = []
	for line in lines:
		p1x,p1y,p2x,p2y = line[0], line[1], line[2], line[3]

		if p1x == p2x and p1y == p2y:    # Single point
			continue

		te = 0    # t: entry
		tl = 1	  # t: leave
		d = [p2x-p1x, p2y-p1y]
		for i in directions:
			if dot(normals[i], d) != 0:
				p0MinusPe = [p1x-pe[i][0], p1y - pe[i][1]]
				p1MinusP0 = d

				num = dot(normals[i], p0MinusPe)
				den = dot(normals[i], p1MinusP0)
	#			print(num, den)
				t = num/-den
	#			print(t)
				if den>0:
					tl = min(tl, abs(t))
				else:
					te = max(te, abs(t))
	#			print(tl, te)
	#	tempLine = None
	#	print(te, tl)
		if abs(te)<abs(tl):
			tempLine = [p1x + (p2x-p1x)*(te), p1y + (p2y-p1y)*(te), p1x + (p2x-p1x)*tl, p1y + (p2y-p1y)*tl]
	#		print(tempLine)
			finalLines.append(tempLine)
	return finalLines

if __name__ == '__main__':
	lines = [[-100, 100, 100, 50], [0,0, 200, 50]]
	clip_rec = [0, 0, 100, 100]

	win = GraphWin("window", 400, 400)
	win.setCoords(-200, -200, 200, 200)
	drawline(win, -200, 0, 200, 0, "blue")
	drawline(win, 0, -200, 0, 200, "blue")

	drawline(win, clip_rec[0], clip_rec[1], clip_rec[2], clip_rec[1], "black")
	drawline(win, clip_rec[0], clip_rec[1], clip_rec[0], clip_rec[2], "black")
	drawline(win, clip_rec[2], clip_rec[1], clip_rec[2], clip_rec[3], "black")
	drawline(win, clip_rec[0], clip_rec[3], clip_rec[2], clip_rec[3], "black")

#	for i in range(n):
#		drawline(win, points[i][0], points[i][1], points[(i+1)%n][0], points[(i+1)%n][1], "black")
#		lines.append([points[i][0], points[i][1], points[(i+1)%n][0], points[(i+1)%n][1]])

	finalLines = pClip(lines, clip_rec)
	for line in lines:
		drawline(win, int(line[0]), int(line[1]), int(line[2]), int(line[3]), "green")
	for line in finalLines:
		drawline(win, int(line[0]), int(line[1]), int(line[2]), int(line[3]), "red")
	win.getKey()
	win.close()
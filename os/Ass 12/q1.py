import sys 
sys.stdin = open('alloc.dat', 'r')  
inf=10**12
def first_fit(size,arr1):
	print("First Fit Technique")
	mem=[[0,0,inf],[size,size,inf]]
	ent=0
	arr=arr1[:]
	free=size
	used=0
	time=0
	serve=0
	miss=0
	while arr or len(mem)>2:
		if arr and arr[0][0]==time:
			ent+=1
			p=arr.pop(0)
			x,si,ti=p[0],p[1],p[2]
			mem1=[]
			ind=-1
			for i in range(len(mem)-1):
				a,b,c=mem[i][0],mem[i][1],mem[i][2]
				d,e,f=mem[i+1][0],mem[i+1][1],mem[i+1][2]
				if d-b>=si:
					ind=i+1
					x,y,z=b,b+si,ti
					break
			if ind==-1:
				miss+=1
			else:
				serve+=1
				free-=si
				used+=si
				mem.insert(ind,[x,y,z])
			if ent%25==0:
				print("After",ent,"entries",ent)
				print("Total serves are ",serve)
				print("Total Misses are ",miss)
				print("% of memory free ",(free/size)*100)
				print(arr)
				print(mem)
				print()	
			continue	
		time+=1
		n=len(mem)
		for i in range(n):
			p=mem.pop(0)
			p[2]-=1
			if p[2]:
				mem.append(p)
			else:
				free+=(p[1]-p[0])
				used-=(p[1]-p[0])	
	if ent%25==0:
		print("After",ent,"entries",ent)
		print("Total serves are ",serve)
		print("Total Misses are ",miss)
		print("% of memory free ",(free/size)*100)
		print(arr)
		print(mem)
		print()
	print()		
				
def next_fit(size,arr1):
	prev=0
	arr=arr1[:]
	print("Next Fit Technique")
	print(arr)
	mem=[[0,0,inf],[size,size,inf]]
	ent=0
	free=size
	used=0
	time=0
	serve=0
	miss=0
	while arr or len(mem)>2:
		if arr and arr[0][0]==time:
			ent+=1
			p=arr.pop(0)
			x,si,ti=p
			mem1=[]
			ind=-1
			n=len(mem)
			for i in range(prev,prev + len(mem)):
				a,b,c=mem[i%n][0],mem[i%n][1],mem[i%n][2]
				d,e,f=mem[(i+1)%n][0],mem[(i+1)%n][1],mem[(i+1)%n][2]
				print(a,b,c,d,e,f)
				if d-b>=si:
					ind=(i+1)%n
					prev=(i+1)%n
					x,y,z=b,b+si,ti
					break
			if ind==-1:
				miss+=1
			else:
				serve+=1
				free-=si
				used+=si
				mem.insert(ind,[x,y,z])
			if ent%1==0:
				print("After",ent,"entries",ent)
				print("Total serves are ",serve)
				print("Total Misses are ",miss)
				print("% of memory free ",(free/size)*100)
				print(arr)
				print(mem)
				print()	
				
			continue	
		time+=1
		n=len(mem)
		for i in range(n):
			p=mem.pop(0)
			p[2]-=1
			if p[2]:
				mem.append(p)
			else:
				free+=(p[1]-p[0])
				used-=(p[1]-p[0])	
	if ent%1==0:
		print("After",ent,"entries",ent)
		print("Total serves are ",serve)
		print("Total Misses are ",miss)
		print("% of memory free ",(free/size)*100)
		print(arr)
		print(mem)
		print()
	print()		


def best_fit(size,arr1):
	print("Best Fit Technique")
	mem=[[0,0,inf],[size,size,inf]]
	ent=0
	arr=arr1[:]
	free=size
	used=0
	time=0
	serve=0
	miss=0
	while arr or len(mem)>2:
		if arr and arr[0][0]==time:
			ent+=1
			p=arr.pop(0)
			x,si,ti=p[0],p[1],p[2]
			mem1=[]
			ind=-1
			mi=10**12
			for i in range(len(mem)-1):
				a,b,c=mem[i][0],mem[i][1],mem[i][2]
				d,e,f=mem[i+1][0],mem[i+1][1],mem[i+1][2]
				if d-b>=si and d-b<mi:
					mi=d-b
					ind=i+1
					x,y,z=b,b+si,ti
			if ind==-1:
				miss+=1
			else:
				serve+=1
				free-=si
				used+=si
				mem.insert(ind,[x,y,z])
			if ent%1==0:
				print("After",ent,"entries",ent)
				print("Total serves are ",serve)
				print("Total Misses are ",miss)
				print("% of memory free ",(free/size)*100)
				print(arr)
				print(mem)
				print()	
			continue	
		time+=1
		n=len(mem)
		for i in range(n):
			p=mem.pop(0)
			p[2]-=1
			if p[2]:
				mem.append(p)
			else:
				free+=(p[1]-p[0])
				used-=(p[1]-p[0])	
				
	if 1:
		print("After",ent,"entries",ent)
		print("Total serves are ",serve)
		print("Total Misses are ",miss)
		print("% of memory free ",(free/size)*100)
		print(arr)
		print(mem)
		print()		
	
	print()		


def worst_fit(size,arr1):
	print("Worst Fit Technique")
	mem=[[0,0,inf],[size,size,inf]]
	ent=0
	arr=arr1[:]
	free=size
	used=0
	time=0
	serve=0
	miss=0
	while arr or len(mem)>2:
		if arr and arr[0][0]==time:
			ent+=1
			p=arr.pop(0)
			x,si,ti=p[0],p[1],p[2]
			mem1=[]
			ind=-1
			mi=-10**12
			for i in range(len(mem)-1):
				a,b,c=mem[i][0],mem[i][1],mem[i][2]
				d,e,f=mem[i+1][0],mem[i+1][1],mem[i+1][2]
				if d-b>=si and d-b>mi:
					mi=d-b
					ind=i+1
					x,y,z=b,b+si,ti
			if ind==-1:
				miss+=1
			else:
				serve+=1
				free-=si
				used+=si
				mem.insert(ind,[x,y,z])
			if ent%1==0:
				print("After",ent,"entries",ent)
				print("Total serves are ",serve)
				print("Total Misses are ",miss)
				print("% of memory free ",(free/size)*100)
				print(arr)
				print(mem)
				print()	
			continue	
		time+=1
		n=len(mem)
		for i in range(n):
			p=mem.pop(0)
			p[2]-=1
			if p[2]:
				mem.append(p)
			else:
				free+=(p[1]-p[0])
				used-=(p[1]-p[0])	
				
	if 1:
		print("After",ent,"entries",ent)
		print("Total serves are ",serve)
		print("Total Misses are ",miss)
		print("% of memory free ",(free/size)*100)
		print(arr)
		print(mem)
		print()		
	
	print()		



if __name__ == '__main__':
	size=int(input())
	req=[]
	while 1:
		req.append(list(map(int,input().split())))
		if req[-1]==[-1,-1,-1]:
			req.pop()
			break
	first_fit(size,req)
	best_fit(size,req)
	worst_fit(size,req)
	next_fit(size,req)
	
	
	
	
						
				
	


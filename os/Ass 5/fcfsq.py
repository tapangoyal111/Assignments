#sample Input
# Pid , Priority ,Arr_time , P, cpu burst, I ,Input burst ,  P, cpu burst, O ,Output burst , P, cpu burst, -1
import heapq as hp
from collections import deque
    
inf=10**12           
with open("input.dat","r") as inp:
	f=list(inp.readlines())
	for i in range(len(f)):
		f[i]=f[i].split('\n')[0]
	n=int(f[0])
	q=int(f[1])
	f.pop(0)
	f.pop(0)
	ready1=[]
	time=[[] for i in range(n)]
	burst=[0]*(n)
	cpu=[inf]*(n)
	status=[[] for i in range(n)]
	#Arrival Time,PID,Index
	
	
	for i in range(n):
		f[i]=list(f[i].split())
		f[i][0],f[i][1],f[i][2]=int(f[i][0]),int(f[i][1]),int(f[i][2])
		ready1.append([f[i][2],f[i][1],f[i][0],i])	
		# print(f[i])
		for j in range(4,len(f[i]),2):
			burst[i]+=int(f[i][j])
		for j in range(4,len(f[i]),2):
			if f[i][j-1]=="P":
				status[i].append(str(int(f[i][j])))
			elif f[i][j-1]=="I":
				status[i].append(-int(f[i][j]))
			else:
				status[i].append(int(f[i][j]))
		status[i].append(0)
		status[i].append(len(status[i])  - 1)
					
		
		time[i]+=[f[i][2],0]
	ready1.sort()
	ready1=deque(ready1)	
	
	ready=deque([])	
	inp=deque([])
	out=deque([])
	
	print("FIRST COME FIRST SERVE Algorithm")
	i=0
	# print(ready)
	while ready1 or inp or out or ready:
		while ready1 and ready1[0][0]<=i:
			ready.append(ready1.popleft())
			
		if ready and ready[0][0]<=i:	
			rp=ready.popleft()
			j=0
			ind=rp[3]
			# print(ind,status)
			
			while j<int(status[ind][status[ind][-2]]):
				while ready1 and ready1[0][0]<=i:
					ready.append(ready1.popleft())
		
				if inp and inp[0][0]==0:
					p=inp.popleft()
					p[0]=i
					status[p[3]][-2]+=1
					if status[p[3]][-2]<status[p[3]][-1]:
						ready.append(p)
				elif inp:
					inp[0][0]-=1
							
				if out and out[0][0]==0:
					p=out.popleft()
					p[0]=i
					status[p[3]][-2]+=1
					if status[p[3]][-2]<status[p[3]][-1]:
						ready.append(p)
				elif out:
					out[0][0]-=1
				# print(i,rp[3])	
				cpu[rp[3]]=min(cpu[rp[3]],i)
			
				j+=1
				i+=1
			status[rp[3]][-2]+=1
			time[ind][1]=i 
			if status[rp[3]][-2]<status[rp[3]][-1]:
				rp[0]= abs(status[ind][status[ind][-2]]) - 1
				
				if status[ind][status[ind][-2]]<0:
					inp.append(rp)
				else:
					out.append(rp)	
		else:
			while ready1 and ready1[0][0]<=i:
				ready.append(ready1.popleft())
			if inp and inp[0][0]==0:
				p=inp.popleft()
				p[0]=i
				status[p[3]][-2]+=1
				if status[p[3]][-2]<status[p[3]][-1]:
					ready.append(p)
			elif inp:
				inp[0][0]-=1
						
			if out and out[0][0]==0:
				p=out.popleft()
				p[0]=i
				status[p[3]][-2]+=1
				if status[p[3]][-2]<status[p[3]][-1]:
					ready.append(p)
			elif out:
				out[0][0]-=1
			
			i+=1
# print(time)				
def printALL(time):
	avg=0
	for i in range(n):
		print("Process With PID",f[i][0],"Has Turn Around Time : ",time[i][1]-time[i][0] )			
		avg+=	time[i][1]-time[i][0]
	print("Average Turn Around Time is ",avg/len(time))
	print()			
	avg=0
	for i in range(n):
		print("Process With PID",f[i][0],"Has Response Time : ",cpu[i]-time[i][0])			
		avg+=	cpu[i]-time[	i][0] 
	print("Average Response  Time is ",avg/len(time))
	print()			
	avg=0
	for i in range(n):
		print("Process With PID",f[i][0],"Has Waiting Time : ",time[i][1]-time[i][0] - burst[i])			
		avg+=	time[i][1]-time[i][0] - burst[i] 
	print("Average Waiting  Time is ",avg/len(time))
	
		
	
printALL(time)
# print(time,cpu)
	
		
		
		


	
	



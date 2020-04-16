
#sample Input
# Pid , Priority ,Arr_time , P, cpu burst, I ,Input burst ,  P, cpu burst, O ,Output burst , P, cpu burst, -1
import heapq as hp
from collections import deque
import random as r    
inf=10**12
niceToWeight={}
c=0

d=[88761, 71755, 56483, 46273, 36291,29154, 23254, 18705, 14949, 11916,9548, 7620, 6100, 4904, 3906,3121, 2501, 1991, 1586, 1277,1024, 820, 655, 526, 423,335, 272, 215, 172, 137,110, 87, 70, 56, 45,36, 29, 23, 18, 15]
for i in range(-20,20):
	niceToWeight[i]=d[c]           
	c+=1
with open("cfs.dat","r") as inp:
	f=list(inp.readlines())
	for i in range(len(f)):
		f[i]=f[i].split('\n')[0]
	schLate=int(f[0])
	minGran=int(f[1])
	f.pop(0)
	f.pop(0)
	numOfProc=len(f) - 1
	print(numOfProc)
	nice=[0]*(numOfProc+1)
	cpu=[inf]*(numOfProc + 1)
	burst=[0]*(numOfProc + 1)
	time=[[0,0] for  i in range(numOfProc + 1)]
	
	status=[[] for i in range(numOfProc +1)]
	#Arrival Time,PID,Index
	totalWeight=0
	for i in range(numOfProc):
		f[i]=list(f[i].split())
		f[i][0],f[i][1]=int(f[i][0]),int(f[i][1])
		pid=f[i][0]
		# print(pid)
		nice[pid]=f[i][1]
		totalWeight+=niceToWeight[nice[pid]]
		for j in range(3,len(f[i]),2):
			if f[i][j-1]=="P":
				status[pid].append(int(f[i][j]))
			elif f[i][j-1]=="I":
				status[pid].append(-int(f[i][j]))
			else:
				status[pid].append(int(f[i][j]))
			burst[pid]+=int(f[i][j])
				
	inp=deque([])
	out=deque([])
	ready=[]
	vrun=0
	for pid in range(1,numOfProc + 1):
		ready.append([vrun,pid])
		
		
	print("CFS Algorithm")
	i=0
	curTime=0
	hp.heapify(ready)
	
	while ready or inp or out:
		
		if inp:
			pid=inp[0][1]
			if status[pid][0]==0:
				status[pid].pop(0)
				totalWeight+=niceToWeight[nice[pid]]
				hp.heappush(ready,inp.popleft())
				
		if out:
			pid=out[0][1]
			if status[pid][0]==0:
				status[pid].pop(0)
				totalWeight+=niceToWeight[nice[pid]]
				hp.heappush(ready,out.popleft())
				
		if inp:
			pid=inp[0][1]
			status[pid][0]+=1
		if out:
			pid=out[0][1]
			status[pid][0]-=1
		
		if ready:
			proc=hp.heappop(ready)
			pid=proc[1]
			
			timeSlice=(niceToWeight[nice[pid]]/totalWeight)*schLate
			# print(niceToWeight[nice[pid]],totalWeight)
			timeToRun=max(minGran,min(timeSlice,status[pid][0]))
			vrun=(niceToWeight[nice[pid]]/totalWeight)*min(timeSlice,status[pid][0])
			# print(min(timeSlice,status[pid][0]))
			while timeToRun!=0:
				if inp:
					pid=inp[0][1]
					status[pid][0]+=1
					if status[pid][0]==0:
						status[pid].pop(0)
						totalWeight+=niceToWeight[nice[pid]]
						hp.heappush(ready,inp.popleft())
						
				if out:
					pid=out[0][1]
					status[pid][0]+=1
					if status[pid][0]==0:
						status[pid].pop(0)
						totalWeight+=niceToWeight[nice[pid]]
						hp.heappush(ready,out.popleft())
				
				pid=proc[1]
				status[pid][0]-=1
				# print(curTime,pid,inp,out,ready)
				cpu[pid]=min(cpu[pid],curTime)
				time[pid][1]=max(curTime + 1,time[pid][1])
				curTime+=1
				timeToRun-=1
		
			proc[0]+=vrun
			if status[pid][0]<=0:
				totalWeight-=niceToWeight[nice[pid]]
				status[pid].pop(0)
				if status[pid] and status[pid][0]<0:
					inp.append(proc)
				elif status[pid] and status[pid][0]>0:
					out.append(proc)
			else:
				hp.heappush(ready,proc)
						
		else:					
			curTime+=1
		
def printALL():
	avg=0
	for pid in range(1,numOfProc + 1):
		print("Process With PID",pid,"Has Turn Around Time : ",time[pid][1])			
		avg+=	time[pid][1]
	print("Average Turn Around Time is ",avg/numOfProc)
	print()			
	avg=0
	for pid in range(1,numOfProc + 1):
		print("Process With PID",pid,"Has Response Time : ",cpu[pid])			
		avg+=	cpu[pid]
		 
	print("Average Response  Time is ",avg/numOfProc)
	print()			
	avg=0
	for pid in range(1,numOfProc + 1):
		print("Process With PID",pid,"Has Waiting Time : ",time[pid][1]- burst[pid])			
		avg+=	time[pid][1]- burst[pid]
	print("Average Waiting  Time is ",avg/numOfProc)
		
printALL()					
				
		
					
			
					
		
	
	



#sample Input
# Pid , Priority ,Arr_time , P, cpu burst, I ,Input burst ,  P, cpu burst, O ,Output burst , P, cpu burst, -1
import heapq as hp
from collections import deque
import random as r    
inf=10**12           
with open("lottery.dat","r") as inp:
	f=list(inp.readlines())
	for i in range(len(f)):
		f[i]=f[i].split('\n')[0]
	numOfTick=int(f[0])
	numOfProc=int(f[1])
	largeNum=int(f[2])
	f.pop(0)
	f.pop(0)
	f.pop(0)
	cpuShare=[0]*(numOfProc+1)
	totalCPUShare=0
	cpu=[inf]*(numOfProc + 1)
	burst=[0]*(numOfProc + 1)
	time=[[0,0] for  i in range(numOfProc + 1)]
	
	status=[[] for i in range(numOfProc +1)]
	#Arrival Time,PID,Index
	
	for i in range(numOfProc):
		f[i]=list(f[i].split())
		f[i][0],f[i][1]=int(f[i][0]),int(f[i][1])
		pid=f[i][0]
		print(pid)
		cpuShare[pid]=f[i][1]
		totalCPUShare+=f[i][1]
		for j in range(3,len(f[i]),2):
			if f[i][j-1]=="P":
				status[pid].append(int(f[i][j]))
			elif f[i][j-1]=="I":
				status[pid].append(-int(f[i][j]))
			else:
				status[pid].append(int(f[i][j]))
			burst[pid]+=int(f[i][j])
				
	# print(status)	
	inp=deque([])
	out=deque([])
	ready=[]
	tic=1
	for pid in range(1,numOfProc + 1):
		ready.append([pid,tic,tic + (numOfTick * cpuShare[pid])//totalCPUShare - 1])
		tic+= (numOfTick * cpuShare[pid])//totalCPUShare
		
	print("Lottery Scheduling Algorithm")
	i=0
	curTime=0
	while ready or inp or out:
		anyChange=False
		toBeAdded=[]
		if inp:
			pid=inp[0][0]
			if status[pid][0]==0:
				status[pid].pop(0)
				toBeAdded.append(pid)
				inp.popleft()
				totalCPUShare+=cpuShare[pid]
				anyChange=True
		if out:
			pid=out[0][0]
			if status[pid][0]==0:
				status[pid].pop(0)
				toBeAdded.append(pid)
				out.popleft()
				totalCPUShare+=cpuShare[pid]
				anyChange=True
		if inp:
			pid=inp[0][0]
			status[pid][0]+=1
		if out:
			pid=out[0][0]
			status[pid][0]-=1
			
					
		if anyChange:
			ready1=[]
			tic=1
			for i in ready:
				pid=i[0]
				ready1.append([pid,tic,tic + (numOfTick * cpuShare[pid])//totalCPUShare - 1])
				tic+= (numOfTick * cpuShare[pid])//totalCPUShare
			
			for i in toBeAdded:
				pid=i
				ready1.append([pid,tic,tic + (numOfTick * cpuShare[pid])//totalCPUShare - 1])
				tic+= (numOfTick * cpuShare[pid])//totalCPUShare
			ready=ready1[:]
		
		ticGen=r.randint(1,numOfTick)
		# print(ticGen)
		for i in range(len(ready)):
			proc=ready[i]
			pid=proc[0]
			if proc[1]<=ticGen and proc[2]>=ticGen:
				# print(pid,status)
				cpu[pid]=min(cpu[pid],curTime)
				time[pid][1]=max(curTime + 1,time[pid][1])
				status[pid][0]-=1
				if status[pid][0]==0:
					totalCPUShare-=cpuShare[pid]
					anyChange=True
					ready=ready[:i] + ready[i+1:]
					status[pid].pop(0)
					if status[pid] and status[pid][0]<0:
						inp.append(proc)
					elif status[pid] and status[pid][0]>0:
						out.append(proc)
				break
		# print(curTime,ready,inp,out)		
							
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
				
		
					
			
					
		
	
	



#sample Input
# Pid , Priority ,Arr_time , P, cpu burst, I ,Input burst ,  P, cpu burst, O ,Output burst , P, cpu burst, -1
import heapq as hp
from collections import deque
def calc(s):
    tot=0
    for i in s[3:]:
        try:
            if int(i)>0:
                tot+=int(i)
        except:
            pass
    return tot            
    
inf=10**12           
with open("input.dat","r") as inp:
	f=list(inp.readlines())
	for i in range(len(f)):
		f[i]=f[i].split('\n')[0]
	n=int(f[0])
	q=int(f[1])
	f.pop(0)
	f.pop(0)
	ready=[]
	time=[[] for i in range(n)]
	burst=[0]*(n)
	cpu=[inf]*(n)
	status=[[] for i in range(n)]
	#Arrival Time,Priority,PID,Index
	for i in range(n):
		f[i]=list(f[i].split())
		f[i][0],f[i][1],f[i][2]=int(f[i][0]),int(f[i][1]),int(f[i][2])
		ready.append([f[i][2],f[i][1],f[i][0],i])	
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
		
		
	hp.heapify(ready)
	inp=deque([])
	out=deque([])
	print("SHOTEST JOB FIRST Algorithm")
	i=0
	ready1=[]
	hp.heapify(ready1)
	while ready or inp or out or ready1:
		# print(i,ready1,inp,out)
		while ready and ready[0][0]<=i:	
			rp=hp.heappop(ready)
			j=0
			ind=rp[3]
			rp1=[int(status[ind][status[ind][-2]])] + rp
			# print(ind,status)
			hp.heappush(ready1,rp1)
		while inp and inp[0][0]==0:
			p=inp.popleft()
			p[0]=i
			ind=p[4]
			status[ind][-2]+=1
			if status[ind][-2]<status[ind][-1]:
				p[0]=int(status[ind][status[ind][-2]])
				hp.heappush(ready1,p)
					
		while out and out[0][0]==0:
			p=out.popleft()
			p[0]=i
			ind=p[4]
			status[ind][-2]+=1
			if status[ind][-2]<status[ind][-1]:
				p[0]=int(status[ind][status[ind][-2]])
				hp.heappush(ready1,p)
		if ready1:
			# print(i,ready1,status[4])
			# print(i,inp,out)
		
			rp=hp.heappop(ready1)
			ind=rp[4]
			j=0
			cpu[ind]=min(cpu[ind],i)
			
			while j<int(status[rp[4]][status[rp[4]][-2]]):
				# print(i,rp[4])
				if inp and inp[0][0]==0:
					p=inp.popleft()
					p[0]=i
					ind=p[4]
					status[p[4]][-2]+=1
					if status[ind][-2]<status[ind][-1]:
						p[0]=int(status[ind][status[ind][-2]])
						hp.heappush(ready1,p)
				elif inp:
					inp[0][0]-=1
							
				if out and out[0][0]==0:
					p=out.popleft()
					p[0]=i
					ind=p[4]
					status[ind][-2]+=1
					if status[ind][-2]<status[ind][-1]:
						p[0]=int(status[ind][status[ind][-2]])
						hp.heappush(ready1,p)
				elif out:
					out[0][0]-=1
				
				j+=1
				i+=1
				
			status[rp[4]][-2]+=1
			time[rp[4]][1]=i
			if status[rp[4]][-2]<status[rp[4]][-1]:
				# print(rp,status[rp[4]])
				rp[0]= abs(status[rp[4]][status[rp[4]][-2]]) 
				if status[rp[4]][status[rp[4]][-2]]<0:
					inp.append(rp)
				else:
					out.append(rp)	
		else:
			# print(i,inp,out)
			if inp:
				inp[0][0]-=1
						
			if out:
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
	
		
		
		


	
	



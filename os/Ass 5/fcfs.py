#sample Input
#Arr_time , Priority , Pid , P, cpu burst, I ,Input burst ,  P, cpu burst, O ,Output burst , P, cpu burst, -1
import heapq as hp
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
	status=[[] for i in range(n)]
	burst=[0]*(n)
	cpu=[inf]*(n)
	#Arrival Time,Priority,PID,Index
	for i in range(n):
		f[i]=list(f[i].split())
		f[i][2],f[i][0]=f[i][0],f[i][2]
		f[i][0],f[i][1],f[i][2]=int(f[i][0]),int(f[i][1]),int(f[i][2])
		ready.append([f[i][0],f[i][1],f[i][2],i])	
		# print(f[i])
		for j in range(4,len(f[i]),2):
			if f[i][j-1]=="P":
				status[i].append(int(f[i][j]))
			else:
				status[i].append(-int(f[i][j]))
			burst[i]+=int(f[i][j])
			
		status[i].append(0)
		status[i].append(len(status[i])  - 1)
					
		time[i]+=[f[i][0],0]
		
		
	hp.heapify(ready)
	block=[]
	hp.heapify(block)
	print("FCFS Algorithm")
	t=0
	avgta=0
	avgrs=0
	avgwt=0
	i=0
	# print(ready)
	while ready or block:
		# print(ready)
		while block and block[0][0]==i:
			p=[i,block[0][1],block[0][2],block[0][3]]
			status[block[0][3]][-2]+=1
			if status[block[0][3]][-2]<status[block[0][3]][-1]:
				hp.heappush(ready,p)
			hp.heappop(block)
			
		if ready and ready[0][0]<=i:	
			rp=hp.heappop(ready)
			
			j=0
			ind=rp[3]
			cpu[ind]=min(cpu[ind],i)
			
			while j<status[ind][status[ind][-2]]:
				while block and block[0][0]==i:
					p=[i,block[0][1],block[0][2],block[0][3]]
					status[block[0][3]][-2]+=1
					if status[block[0][3]][-2]<status[block[0][3]][-1]:
						hp.heappush(ready,p)
					hp.heappop(block)
				print(i,ind)		
				# print(i,rp[2],ready,block)
				j+=1
				i+=1
			status[rp[3]][-2]+=1
			time[ind][1]=i 
			if status[rp[3]][-2]<status[rp[3]][-1]:
				rp[0]=i + abs(status[ind][status[ind][-2]])
				hp.heappush(block,rp)
		else:
			i+=1
				
def printALL(time):
	avg=0
	for i in range(n):
		print("Process With PID",f[i][2],"Has Turn Around Time : ",time[i][1]-time[i][0] )			
		avg+=	time[i][1]-time[i][0]
	print("Average Turn Around Time is ",avg/len(time))
	print()			
	avg=0
	for i in range(n):
		print("Process With PID",f[i][2],"Has Response Time : ",cpu[i]-time[i][0])			
		avg+=	cpu[i]-time[	i][0] 
	print("Average Response  Time is ",avg/len(time))
	print()			
	avg=0
	for i in range(n):
		print("Process With PID",f[i][2],"Has Waiting Time : ",time[i][1]-time[i][0] - burst[i])			
		avg+=	time[i][1]-time[i][0] - burst[i] 
	print("Average Waiting  Time is ",avg/len(time))
	
		
	
printALL(time)
# print(time,cpu)
	
		
		
		


	
	



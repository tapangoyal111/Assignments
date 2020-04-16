import sys 
sys.stdin = open('reference.dat', 'r')  

def fifo(n,page):
	ind=0
	pagetable=[-1]*n
	d={}
	miss=0
	hit=0
	print("FIFO Algorithm")
	ent=0
	for i in page:
		if i==-1:
			break
		if d.get(i,0)==0:
			d[i]=1
			miss+=1
			if pagetable[ind%n]!=-1:
				d[pagetable[ind%n]]-=1
			pagetable[ind%n]=i
			ind+=1
		else:
			hit+=1
		ent+=1
		# print(ent)
		if ent%5==0:
			print("After",ent,"entries",ent)
			print("Total Hits are ",hit)
			print("Total Misses are ",miss)
			print("Hit Ratio is",hit/(miss+hit))
			print()
	print()
	
def lru(n,page):
	pagetable={}
	time=1
	length=0
	hit=0
	miss=0
	ent=0
	print("LRU Algorithm")
	for i in page:
		if pagetable.get(i,0)!=0:
			pagetable[i]=time
			hit+=1
			# print(i,"hit",pagetable)
		elif pagetable.get(i,0)==0 and length<n:
			pagetable[i]=time
			miss+=1
			length+=1
			# print(i,"miss",pagetable)
		elif pagetable.get(i,0)==0 and length==n:
			miss+=1
			mi=10**12
			for t in pagetable:
				if  pagetable[t]<mi and pagetable[t]>0:
					mi=pagetable[t]
					ind=t
			pagetable[t]=0
			pagetable[i]=time
			# print(i,"miss",pagetable)
			
		time+=1
		ent+=1
		if ent%5==0:
			print("After",ent,"entries",ent)
			print("Total Hits are ",hit)
			print("Total Misses are ",miss)
			print("Hit Ratio is",hit/(miss+hit))
			print()
	
	print()				

def optimal(n,page):
	pagetable={}
	length=0
	hit=0
	miss=0
	ent=0
	print("Optimal Algorithm")
	for i in page:
		if pagetable.get(i,0)!=0:
			pagetable[i]=1
			hit+=1
			print(i,"hit",pagetable)
		elif pagetable.get(i,0)==0 and length<n:
			pagetable[i]=1
			miss+=1
			length+=1
			print(i,"miss",pagetable)
		elif pagetable.get(i,0)==0 and length==n:
			miss+=1
			d={}
			ma=0
			ind=0
			for k in pagetable:
				if pagetable[k]>0:
					d[k]=10**12
			for t in range(ent + 1,len(page)):
				if pagetable.get(page[t],0)>0:
					d[page[t]]=min(t,d[page[t]])
			for t in d:
				if d[t]>ma:
					ma=d[t]
					ind=t			
			pagetable[ind]=0
			pagetable[i]=1
			print(i,"miss",pagetable)
			
		ent+=1
		if ent%5==0:
			print("After",ent,"entries",ent)
			print("Total Hits are ",hit)
			print("Total Misses are ",miss)
			print("Hit Ratio is",hit/(miss+hit))
			print()
	
	print()				


	
def lfu(n,page):
	pagetable={}
	length=0
	hit=0
	miss=0
	ent=0
	print("LFU Algorithm")
	for i in page:
		if pagetable.get(i,0)!=0:
			pagetable[i]+=1
			hit+=1
			# print(i,"hit",pagetable)
		elif pagetable.get(i,0)==0 and length<n:
			pagetable[i]=1
			miss+=1
			length+=1
			# print(i,"miss",pagetable)
		elif pagetable.get(i,0)==0 and length==n:
			miss+=1
			mi=10**12
			for t in pagetable:
				if  pagetable[t]<mi and pagetable[t]>0:
					mi=pagetable[t]
					ind=t
			pagetable[t]=0
			pagetable[i]=1
			# print(i,"miss",pagetable)
			
		ent+=1
		if ent%5==0:
			print("After",ent,"entries",ent)
			print("Total Hits are ",hit)
			print("Total Misses are ",miss)
			print("Hit Ratio is",hit/(miss+hit))
			print()
	
	print()				
				

def mfu(n,page):
	pagetable={}
	length=0
	hit=0
	miss=0
	ent=0
	print("MFU Algorithm")
	for i in page:
		if pagetable.get(i,0)!=0:
			pagetable[i]+=1
			hit+=1
			# print(i,"hit",pagetable)
		elif pagetable.get(i,0)==0 and length<n:
			pagetable[i]=1
			miss+=1
			length+=1
			# print(i,"miss",pagetable)
		elif pagetable.get(i,0)==0 and length==n:
			miss+=1
			mi=-10**12
			for t in pagetable:
				if  pagetable[t]>mi and pagetable[t]>0:
					mi=pagetable[t]
					ind=t
			pagetable[t]=0
			pagetable[i]=1
			# print(i,"miss",pagetable)
			
		ent+=1
		if ent%5==0:
			print("After",ent,"entries",ent)
			print("Total Hits are ",hit)
			print("Total Misses are ",miss)
			print("Hit Ratio is",hit/(miss+hit))
			print()
	
	print()				
								
if __name__ == '__main__':
	n=int(input())
	print(n)
	page=list(map(int,input().split()))
	print(n)
	fifo(n,page)
	lru(n,page)
	lfu(n,page)
	mfu(n,page)
	optimal(n,page)
	
	
	
	
						
				
	

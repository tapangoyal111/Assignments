#include <stdio.h> 
#include <stdlib.h> 
#include <unistd.h> 
#include <pthread.h> 

int z = 0,n;
int choosing[12];
int ticket[12];

int maxValue(){
	int max=0;
	for(int i=0;i<n;i++)
		if(ticket[i]>max)
			max=ticket[i];
	return max;
}
void *func1(void *s) { 
	int i,k,j;
	int x=(int)s;
    for(i=0;i<5;i++)  {

		choosing[x] =1;
		ticket[x]=maxValue()+1;
		choosing[x]=0;
		for(j=0;j<n;j++){
			if(j == x)
				continue;
			while(choosing[j] != 0);
			while(ticket[j] != 0 && ticket[j] < ticket[x]);
		 
			if(ticket[i] == ticket[x] && i < x) {
				while(ticket[i] != 0);
			}
		}
		z = z+1;
		printf("%2d :  Thread %d in Critical Section (%d).\n", i+1,x,z);
		ticket[x]=0;
		k = (int) ((5.0*rand())/RAND_MAX);
		sleep(k);
	}
}
int main(){
	printf("Enetr the no. of process ro be created :");
	scanf("%d",&n);
	pthread_t Thread[n];
	for(int i=0;i<n;i++){
		pthread_create(&Thread[i], NULL, func1, (void *) i); 
	}
	for(int i=0;i<n;i++){
		pthread_join(Thread[i], NULL); 
	}
	return 0;
} 

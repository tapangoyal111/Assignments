#include <stdio.h> 
#include <stdlib.h> 
#include <unistd.h> 
#include <pthread.h> 

int	x = 0;		// Shared variable


#define	THREAD1	0
#define	THREAD2	1

#define	TRUE 1
#define FALSE 0
  
int favoredProcess;
int P1_WantsToEnter; 
int P2_WantsToEnter;
void Initialization(void) { 
	favoredProcess=1;
        P1_WantsToEnter = FALSE;P2_WantsToEnter = FALSE;
	srand(time(NULL));
} 

void *func1(void *s) { 
	int	i, k;
    	for (i=0; i < 5; i++)  {
                P1_WantsToEnter = TRUE;
		while(P2_WantsToEnter) {
			
			if(favoredProcess == 2) {
				P1_WantsToEnter = FALSE;
				while(favoredProcess == 2); // busy wait             
				P1_WantsToEnter = TRUE;
			}          
			
		}
		x = x+1;
		printf("[%2d] :  Thread 1 in Critical Section (%d).\n", i+1,x);
		favoredProcess = 2;
		P1_WantsToEnter=FALSE;
        k = (int) ((3.0*rand())/RAND_MAX);
		sleep(k);
		
		
	}
} 
  
  
void *func2(void *s) { 
	int	i, k;
    	for (i=0; i < 5; i++)  {
                P2_WantsToEnter = TRUE;
		while(P1_WantsToEnter) {
			if(favoredProcess == 1) {
				P2_WantsToEnter = FALSE;
				while(favoredProcess == 1); // busy wait                       
				P2_WantsToEnter = TRUE;
			}
		}
                
                
		x = x+1;
		printf("[%2d] :  Thread 2 in Critical Section (%d).\n", i+1,x);
		favoredProcess = 1;
		P1_WantsToEnter=FALSE;
		k = (int) ((5.0*rand())/RAND_MAX);
		sleep(k); 
		
	}
} 
  

int main() { 
    	pthread_t Thread1, Thread2; 
    	// Initialized the lock then fork 2 threads 
		Initialization();
  
    	// Create two threads (both run func)  
    	pthread_create(&Thread1, NULL, func1, (void *) THREAD1); 
    	pthread_create(&Thread2, NULL, func2, (void *) THREAD2); 
  
	// Wait for the threads to end. 
    	pthread_join(Thread1, NULL); 
    	pthread_join(Thread2, NULL); 
  
    	return 0; 
}

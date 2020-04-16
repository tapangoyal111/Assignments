#include <unistd.h> 
#include <sys/types.h> 
#include <errno.h> 
#include <stdio.h> 
#include <sys/wait.h> 
#include <stdlib.h> 
#include <sys/ipc.h> 
#include <sys/shm.h> 

int main(){
	int buffSize=10;
	key_t key = ftok("shmfile",65); 
	int shmid = shmget(key,1024,0666|IPC_CREAT); 
	int *arr = (int*) shmat(shmid,(void*)0,0); 
	
	//key_t keyptr = ftok("shmptr",70); 
	// shmget returns an identifier in shmid 
	//int shmidptr = shmget(keyptr,1024,0666|IPC_CREAT); 
  
	// shmat to attach to shared memory 
	//int *arrptr = (int*) shmat(shmidptr,(void*)0,0); 
	 //shmat to attach to shared memory 
	 
	 
	 
	for(int i=0;i<1000;i++){
		arr[i]=-1;
	}
	arr[0]=2;
	arr[1]=2;
	
	int t=1;
	if(1){
		int pid=fork();
		if (pid>0){
			while(1){
					int num;
					arr[0]++;
					sleep(2);
					printf("%d %d\n",arr[0],arr[1]);	
					arr[arr[0]]=rand()%1000;
					printf("Number that Producer Wants to Write at %d is %d\n",arr[0],arr[arr[0]]);
					sleep(1);
				}
			}
			
		else{
			//printf("%d %d",)
			while(1){
				if ( arr[1]<arr[0]){
					//printf("Entering Child\n");
					arr[1]=arr[1] + 1;
					sleep(1);
					printf("Number that Consumer Reads From %d is %d\n",arr[1],arr[arr[1]]);
					
				}
			}
		}
	}
}


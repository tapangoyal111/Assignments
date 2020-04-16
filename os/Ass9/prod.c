#include <sys/ipc.h> 
#include <sys/shm.h> 
#include <stdio.h> 
  
int main() 
{ 
    // ftok to generate unique key 
    key_t key = ftok("shmfile",65); 
  
    // shmget returns an identifier in shmid 
    int shmid = shmget(key,1024,0666|IPC_CREAT); 
  
    // shmat to attach to shared memory 
    int *arr = (int*) shmat(shmid,(void*)0,0);
    int t=5;
    while (t-->0){
    scanf("%d",&arr[4-t]);
    printf("Data written in memory: %d\n",arr[4-t]); 
	} 
    //detach from shared memory  
    shmdt(arr); 
  
    return 0; 
} 


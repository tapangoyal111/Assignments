
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
  
    printf("Data read from memory: %d %d %d %d %d\n",arr[0],arr[1],arr[2],arr[3],arr[4]); 
      
    //detach from shared memory  
    shmdt(arr); 
    // destroy the shared memory 
    shmctl(shmid,IPC_RMID,NULL); 
    
    
    
    return 0; 
    
}

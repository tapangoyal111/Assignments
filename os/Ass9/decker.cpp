#include <iostream> 
#include <sys/ipc.h> 
#include <sys/shm.h> 
#include <stdio.h> 
#include <fcntl.h>
#include <assert.h>
#include <sys/wait.h>
#include "err.h"
#include <sys/types.h>
#include <unistd.h>
using namespace std; 
#define value 100000

int main()
{
    key_t key = 5678;
    int shm_id;
    shm_id = shmget(key, 10*sizeof(int), 0666 | IPC_CREAT);
    
    int* array = (int*)shmat(shm_id, NULL, 0);
    int size = 9;
    array[0] = 0;

    array[1] = 0; //1 wants to enter
    array[2] = 0; //2 wants to enter
    array[3] = 1; // favoured process 

    int pid = fork();
    if(pid > 0)
    {   
        for(int i=0; i<value; i++){
        	array[1] = 1;
        	while (array[2] == 1){
        		if(array[3] == 2){
        			array[1] = 0;
        			while(array[3] == 2)
        				;
        			array[1] = 1;
        		}
        	}

        	array[0]++;  //Critical secion of program.

        	array[3] = 2;
        	array[1] = 0;
        }
        wait(&pid);
        cout << "Value of Counter is " << array[0] << ". Expected value " << 2*value << endl;

    }
    else
    {

    	for (int j = 0; j < value; j++){
    		array[2] = 1;
    		while(array[1] == 1){
    			if(array[3] == 1){
    				array[2] = 0;
    				while(array[3] == 1)
    					;
    				array[2] = 1;
    			}
    		}

    		array[0]++; //Crtical section.

    		array[3] = 1;
    		array[2] = 0;
    	}
    }
}

#include <iostream> 
#include <algorithm>
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
#define COUNTER 100000

int main()
{
    key_t key = 5678;
    key_t key2 = 5689;
    key_t key3 = 5690;

    int shm_id, shm_id2, sid;

    shm_id = shmget(key, 2*sizeof(int), 0666 | IPC_CREAT);
    shm_id2 = shmget(key2, 2*sizeof(bool), 0666 | IPC_CREAT);
    sid = shmget(key3, sizeof(int), 0666 | IPC_CREAT);

    int* count = (int*)shmat(sid, NULL, 0);
    int* tic = (int*)shmat(shm_id, NULL, 0);
    bool* select = (bool*)shmat(shm_id2, NULL, 0);

    *count = 0;
    int size = 2;
    for(int i=0; i<size; i++){
        tic[i] = 0;
        select[i] = false;
    }

 
    int pid = fork();
    if(pid > 0)
    {   
        int x = 0;
        for(int i=0; i<COUNTER; i++){
            select[x] = true;
            tic[x] = *max_element(tic, tic+size)+1;
            select[x] = false;

            for(int j=0; j<size; j++){
                if(j == x)
                    continue;
                while(select[j])
                    ;
                while(tic[j] != 0 && tic[j] < tic[x])
                    ;
                while(tic[j] == tic[x] && j<x)
                    ;
            }

            (*count)++;  //critical section

            tic[x] = 0;

        }
        wait(&pid);
        cout << "Value of counter is " << *count << ". Expected value " << 2*COUNTER << endl;

    }
    else
    {
        int x = 1;
        for(int i=0; i<COUNTER; i++){
            select[x] = true;
            tic[x] = *max_element(tic, tic+size)+1;
            select[x] = false;

            for(int j=0; j<size; j++){
                if(j == x)
                    continue;
                while(select[j])
                    ;
                while(tic[j] != 0 && tic[j] < tic[x])
                    ;
                while(tic[j] == tic[x] && j<x)
                    ;
            }


            (*count)++;  //critical section

            tic[x] = 0;

        }
    }
}

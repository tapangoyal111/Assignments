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
#include <pthread.h>
using namespace std; 
#define SIZE 2
#define counter 100000

int *tick;
bool *choose;
int c = 0;

void *thread_fun(void *args){
        int x = 1;
        for(int i=0; i<counter; i++){
            choose[x] = true;
            tick[x] = *max_element(tick, tick+SIZE)+1;
            choose[x] = false;

            for(int j=0; j<SIZE; j++){
                if(j == x)
                    continue;
                while(choose[j])
                    ;
                while(tick[j] != 0 && tick[j] < tick[x])
                    ;
                while(tick[j] == tick[x] && j<x)
                    ;
            }


            c++;  //critical section

            tick[x] = 0;

        }
    }   



int main()
{
    tick = (int *)malloc(sizeof(int)*SIZE);
    choose = (bool *)malloc(sizeof(bool)*SIZE);

    for(int i=0; i<SIZE; i++){
        tick[i] = 0;
        choose[i] = false;
    }

    pthread_t ptid;

    pthread_create(&ptid, NULL, thread_fun, NULL);

    int x = 0;
    for(int i=0; i<counter; i++){
        choose[x] = true;
        tick[x] = *max_element(tick, tick+SIZE)+1;
        choose[x] = false;

        for(int j=0; j<SIZE; j++){
            if(j == x)
                continue;
            while(choose[j])
                ;
            while(tick[j] != 0 && tick[j] < tick[x])
                ;
            while(tick[j] == tick[x] && j<x)
                ;
        }

        c++;  //critical section

        tick[x] = 0;

    }
    pthread_join(ptid, NULL);
    cout << "Value of counter is " << c << ". Expected value " << 2*counter << endl;

}

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

bool process1 = false;
bool process2 = false;
int favoured = 1;
int c = 0;

void *thread_fun(void *args){

        for(int i=0; i<counter; i++){
            
            process1 = true;
            while(process2){
                if(favoured == 2){
                    process1 = false;
                    while(favoured == 2)
                        ;
                    process1 = true;
                }
            }

            c++;  //critical section

            favoured = 2;
            process1 = false;
        }
    }   



int main()
{
    pthread_t ptid;

    pthread_create(&ptid, NULL, thread_fun, NULL);

    for(int i=0; i<counter; i++){
        
        process2 = true;
        while(process1){
            if(favoured == 1){
                process2 = false;  
                while(favoured == 1)
                    ;
                process2 = true;
            }
        }
        c++;  //critical section

        favoured = 1;
        process2 = false;
    }
    pthread_join(ptid, NULL);
    cout << "Value of counter is " << c << ". Expected value " << 2*counter << endl;

}

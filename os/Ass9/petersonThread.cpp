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
#define cERCOUNTER 100000

bool process1 = false;
bool process2 = false;
int favoured = 1;
int c = 0;

void *thread_fun(void *args){
        int x = 1;
        for(int i=0; i<cERCOUNTER; i++){
            
            process1 = true;
            favoured = 2;
            while(process2 && favoured == 2)
                ;
            c++;  //critical section

            process1 = false;
        }
    }   



int main()
{
    pthread_t ptid;

    pthread_create(&ptid, NULL, thread_fun, NULL);

    int x = 0;
    for(int i=0; i<cERCOUNTER; i++){
        
        process2 = true;
        favoured = 1;
        while(process1 && favoured == 1)
            ;

        c++;  //critical section

        process2 = false;
    }
    pthread_join(ptid, NULL);
    cout << "Value of counter is " << c << ". Expected value " << 2*cERCOUNTER << endl;

}

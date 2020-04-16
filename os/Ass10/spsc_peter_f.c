#include <stdio.h> 
#include <stdlib.h> 
#include <unistd.h> 
#include <pthread.h>
#include <stdbool.h>
#include <sys/mman.h>
static int *balance;//=0;  
static int *favProcess;//=1;
static bool* p1_wants_to_enter;//=false;
static bool* p2_wants_to_enter;//=false;
 



int main(){

       balance = mmap(NULL, sizeof *balance, PROT_READ | PROT_WRITE, 
                    MAP_SHARED | MAP_ANONYMOUS, -1, 0);
        *balance=0;
        
        favProcess = mmap(NULL, sizeof *favProcess, PROT_READ | PROT_WRITE, 
                    MAP_SHARED | MAP_ANONYMOUS, -1, 0);
        *favProcess=1;
        
         p2_wants_to_enter= mmap(NULL, sizeof *p2_wants_to_enter, PROT_READ | PROT_WRITE, 
                    MAP_SHARED | MAP_ANONYMOUS, -1, 0);
        *p2_wants_to_enter=false;
        
        
        p1_wants_to_enter= mmap(NULL, sizeof *p1_wants_to_enter, PROT_READ | PROT_WRITE, 
                    MAP_SHARED | MAP_ANONYMOUS, -1, 0);
        *p1_wants_to_enter=false;
        
        
        
        if(fork()==0){
                *p1_wants_to_enter=true;
                *favProcess=2;
                while(*p2_wants_to_enter && *favProcess==2)
                        ;
                *balance=*balance+500;
                printf("balance from producer = %d\n",*balance);
                *p1_wants_to_enter=false;
                
                
        }
        else{
                *p2_wants_to_enter=true;
                *favProcess=1;
                while(*p1_wants_to_enter && *favProcess==1)
                        ;
                *balance=*balance-500;
                printf("balance from consumer = %d\n",*balance);
                *p2_wants_to_enter=false;
        
        }
        
        
	//printf("the final balance is %d\n",balance);
	return(0);   
        
        
        
}

#include <stdio.h>
#include <sys/mman.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include<stdbool.h>
#include<time.h>
#include<stdlib.h>
#include<stdbool.h>
#define N 30    // buffer size
int main(){
    int *pindex,*cindex,*favoured_process;
    int *buffer;
    bool *p1_wants,*p2_wants;
    
   
    
    p1_wants = mmap(NULL, sizeof *p1_wants, PROT_READ | PROT_WRITE, MAP_SHARED | MAP_ANONYMOUS,-1,0);
   	*p1_wants = false;
    
    p2_wants = mmap(NULL, sizeof *p2_wants, PROT_READ | PROT_WRITE, MAP_SHARED | MAP_ANONYMOUS,-1,0);
   	*p2_wants = false;      



     pindex = mmap(NULL, sizeof *pindex, PROT_READ | PROT_WRITE, MAP_SHARED | MAP_ANONYMOUS,-1,0);
    *pindex = 0;

    cindex = mmap(NULL, sizeof *cindex, PROT_READ | PROT_WRITE, MAP_SHARED | MAP_ANONYMOUS,-1,0); 
    *cindex=0; 
    
    buffer = mmap(NULL, sizeof (*buffer)*N, PROT_READ | PROT_WRITE, MAP_SHARED | MAP_ANONYMOUS, -1, 0);
    
    favoured_process = mmap(NULL, sizeof *favoured_process, PROT_READ | PROT_WRITE, MAP_SHARED | MAP_ANONYMOUS,-1,0);
    *favoured_process = 1;
    
    srand(time(0));
    

        if(fork()>0){

            int cnt = 0;

            while(cnt<18){

                *p1_wants=true;

                *favoured_process=2;

                while(*p2_wants && *favoured_process==2){
                                      
                }

                int c=0;
                while((*pindex==N-1 && *cindex==0) || *pindex==*cindex-1){
                }  



                buffer[*pindex]=rand()%99;
                printf("producer is producing %d \n",buffer[*pindex]);


                *pindex=(*pindex+1)%N;                
                cnt++;
                *p1_wants=false; 
                sleep(rand()%3);
            }

        }
        else{
            int cnt = 0;
            while(cnt<18){
                *p2_wants=true;
                *favoured_process=1;
                while(*p1_wants && *favoured_process==1){
                                     
                }
                
                while(*pindex==*cindex){
                   
                    *favoured_process=*favoured_process+1;
                } 
                printf("consumer is reading %d\n",buffer[*cindex]);
                buffer[*cindex]=0;
                *cindex=(*cindex+1)%N;                
                cnt++;
                sleep(rand()%4);
                *p2_wants=false;
                sleep(rand()%2);
            }
        }                  
    return 0;
}

#include<stdio.h>
#include<unistd.h>
#include<sys/stat.h>
#include <fcntl.h> 
#include <sys/mman.h>
#include <sys/wait.h>
#include <stdbool.h> 
#include<stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include<sys/shm.h>


int main(){
    
    const char* name = "buffer";
    const char* cin = "cind";
    const char* cnitems = "nitems";
    const char* cfavoured = "favoured";
    const char* cp1wants = "p1wants";
    const char* cp2wants = "p2wants";

    int shm_fd = shm_open(name, O_CREAT | O_RDWR, 0666); 
    ftruncate(shm_fd, sizeof(int)*BUFF_SIZE); 
    int *buf = (int*)mmap(0, sizeof(int)*10 , PROT_READ, MAP_SHARED, shm_fd, 0); 

    int shmc = shm_open(cin, O_CREAT | O_RDWR, 0666); 
    ftruncate(shmc, sizeof(int)); 
    int *cind = (int*)mmap(0, sizeof(int) , PROT_READ | PROT_WRITE, MAP_SHARED, shmc, 0);
    
    int sh_p1wants = shm_open(cp1wants, O_CREAT | O_RDWR, 0666);
    ftruncate(sh_p1wants, sizeof(int));
    int* p1wants = (int*) mmap(0, sizeof(int), PROT_READ | PROT_WRITE, MAP_SHARED, sh_p1wants, 0);

    int sh_nitems = shm_open(cnitems, O_CREAT | O_RDWR, 0666);
    ftruncate(sh_nitems, sizeof(int));
    int* nitems = (int*) mmap(0, sizeof(int), PROT_READ | PROT_WRITE, MAP_SHARED, sh_nitems, 0);

    
    int sh_favoured = shm_open(cfavoured, O_CREAT | O_RDWR, 0666);
    ftruncate(sh_favoured, sizeof(int));
    int* favoured = (int*) mmap(0, sizeof(int), PROT_READ | PROT_WRITE, MAP_SHARED, sh_favoured, 0);    
    int sh_p2wants = shm_open(cp2wants, O_CREAT | O_RDWR, 0666);
    ftruncate(sh_p2wants, sizeof(int));
    int* p2wants = (int*) mmap(0, sizeof(int), PROT_READ | PROT_WRITE, MAP_SHARED, sh_p2wants, 0);
    int flag = 0;
    while(1){
            (*p2wants) = 1;
            (*favoured) = 1;
 //           while((*p1wants) && (*favoured)==1);
            while((*nitems) == 0);
            int c = buf[*cind];
            if((c != 0) || (flag == 0))
            printf("Consumer id: %d value: %d\n",getpid(),c), flag = 1;
            *cind = (*cind + 1)%(BUFF_SIZE);
            (*nitems)--;
            (*p2wants) = 0;
            sleep(rand()%3);
    }
    

}

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
    
    

    const char* cfavoured = "favoured";
    int sh_favoured = shm_open(cfavoured, O_CREAT | O_RDWR, 0666);
    ftruncate(sh_favoured, sizeof(int));
    int* favoured = (int*) mmap(0, sizeof(int), PROT_READ | PROT_WRITE, MAP_SHARED, sh_favoured, 0);

    const char* cp1wants = "p1wants";
    int sh_p1wants = shm_open(cp1wants, O_CREAT | O_RDWR, 0666);
    ftruncate(sh_p1wants, sizeof(int));
    int* p1wants = (int*) mmap(0, sizeof(int), PROT_READ | PROT_WRITE, MAP_SHARED, sh_p1wants, 0);

    const char* cp2wants = "p2wants";
    int sh_p2wants = shm_open(cp2wants, O_CREAT | O_RDWR, 0666);
    ftruncate(sh_p2wants, sizeof(int));
    int* p2wants = (int*) mmap(0, sizeof(int), PROT_READ | PROT_WRITE, MAP_SHARED, sh_p2wants, 0);



    const char* name = "buffer";
    int shm_fd = shm_open(name, O_CREAT | O_RDWR, 0666); 
    ftruncate(shm_fd, sizeof(int)*BUFF_SIZE); 
    int *buf = (int*)mmap(0, sizeof(int)*10 , PROT_WRITE, MAP_SHARED, shm_fd, 0); 
    
    const char* nval = "val";

    int shm = shm_open(nval, O_CREAT | O_RDWR, 0666); 
    ftruncate(shm, sizeof(int)); 
    int *val = (int*)mmap(0, sizeof(int) , PROT_READ | PROT_WRITE, MAP_SHARED, shm, 0);

    const char* pin = "pind";

    int shmp = shm_open(pin, O_CREAT | O_RDWR, 0666); 
    ftruncate(shmp, sizeof(int)); 
    int *pind = (int*)mmap(0, sizeof(int) , PROT_READ | PROT_WRITE, MAP_SHARED, shmp, 0);

    const char* cnitems = "nitems";
    int sh_nitems = shm_open(cnitems, O_CREAT | O_RDWR, 0666);
    ftruncate(sh_nitems, sizeof(int));
    int* nitems = (int*) mmap(0, sizeof(int), PROT_READ | PROT_WRITE, MAP_SHARED, sh_nitems, 0);

    
    while(1){
        (*p1wants) = 1;
        (*favoured) = 2;

        while((*nitems) == BUFF_SIZE);
        buf[*pind] = *val;
        printf("Producer [%d] producing [%d]\n", getpid(),*val);
      
        (*val)++;
      
        *pind = (*pind+1)%(BUFF_SIZE); 
        (*nitems)++;
        (*p1wants) = 0;
        sleep(rand()%2);
    }

}

#include<stdio.h>
#include<sys/types.h>
#include<stdlib.h>
#include<time.h>
#include<unistd.h>
#include<sys/mman.h>

static int *x;
static int *flag0;
static int *flag1;
static int *turn;

int main(int argc, char const *argv[]){
	srand(time(NULL));
	x = mmap(NULL, sizeof *x, PROT_READ | PROT_WRITE, 
                    MAP_SHARED | MAP_ANONYMOUS, -1, 0);
	flag0 = mmap(NULL, sizeof *flag0, PROT_READ | PROT_WRITE, 
                    MAP_SHARED | MAP_ANONYMOUS, -1, 0);

    flag1 = mmap(NULL, sizeof *flag1, PROT_READ | PROT_WRITE, 
                    MAP_SHARED | MAP_ANONYMOUS, -1, 0);

    turn = mmap(NULL, sizeof *turn, PROT_READ | PROT_WRITE, 
                    MAP_SHARED | MAP_ANONYMOUS, -1, 0);
	*flag0=0;
	*flag1=0;
	*turn;
	*x=0;
	int pid,i,k;
	pid=fork();
	if(pid==0){
		for(i=0;i<5;i++){
			*flag0=1;
			while(*flag1){
				if(*turn==0){
					*flag0=0;
					while(*turn==0);
					*flag0=1;
				}
			}
			*x=*x+1;
			printf("Process 1 is in Critical Section (%d)\n",*x);
			*turn=0;
			*flag0=0;
			k = (int) ((3.0*rand())/RAND_MAX);
			sleep(k);
		}
	}
	else{
		for(i=0;i<5;i++){
			*flag1=1;
			while(*flag0){
				if(*turn==1){
					*flag1=0;
					while(*turn==1);
					*flag1=1;
				}
			}
			*x=*x+1;
			printf("Process 2 is in Critical Section (%d)\n",*x);
			*turn=1;
			*flag1=0;
			k = (int) ((3.0*rand())/RAND_MAX);
			sleep(k);
		}
	}

	return 0;
}
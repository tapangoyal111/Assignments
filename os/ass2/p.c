#include<unistd.h>
#include<stdio.h>
#include<stdlib.h>
int main(){
	int a=5;
	int arr[5]={10,20,30,40,50};
	//printf("parent pid %d and ppid %d\n",(int)(getpid()),(int)(getppid()));
	int x=fork();
	int pid1,pid2;
	//int arr[5]={10,20,30,40,50};
	if(x<0){
		
		printf("frk failed");
		
	}
	else if(x==0){
		//sleep(2);
		a=10;
		//int *p=&a;
		printf("in child %d\n",a);
		//printf("child process %d value of a is %d ppid is %d\n",(int)(getpid()),a,(int)(getppid()));
	}
	else{
		/*int ab[100000],i;
		for(i=0;i<100000;i++){
			a=a+ab[i];
		}*/
		//int *
		sleep(20);
		arr[3]=320;
		printf("in parnet %d\n",a);
		//printf("parent pid %d value of a is %d ppid is %d\n",(int)(getpid()),a,(int)(getppid()));
	}
	return 0;
}

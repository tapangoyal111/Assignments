#include <stdio.h> 
#include <stdlib.h> 
#include <unistd.h> 
#include <pthread.h>
#include <stdbool.h>  
int favProcess=1;
bool p1_wants_to_enter=false;
bool p2_wants_to_enter=false;
int item=0;
void* producer(){
        p1_wants_to_enter=true;
        favProcess=2;
        while(p2_wants_to_enter && favProcess==2)
                ;
        item=item+500;
        printf("item from producer= %d\n",item);
        p1_wants_to_enter=false;
        
}

void* consumer(){
        p2_wants_to_enter=true;
        favProcess=1;
        while(p1_wants_to_enter && favProcess==1)
                ;
        item=item-500;
        printf("item from consumer = %d\n",item);
        p2_wants_to_enter=false;
        
}

int main(){
        pthread_t tid1;
        pthread_t tid2;
        
        for(int i=0;i<3;i++){
                pthread_create(&tid1, NULL, producer, (void *)&tid1); 
		pthread_create(&tid2,NULL,consumer,(void *)&tid2);
        }
        
        for (int i = 0; i < 3; i++){
		pthread_join(tid1,NULL);
		pthread_join(tid2,NULL);
	}
	printf("the final no of item is %d\n",item);
	return(0);   
        
        
        
}

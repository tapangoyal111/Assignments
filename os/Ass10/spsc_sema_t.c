#include <pthread.h>
#include <stdio.h>
#include <semaphore.h>
#include<stdlib.h>

#define BUFF_SIZE 4
#define FULL 0
#define EMPTY 0
char buffer[BUFF_SIZE];
int nextIn = 0;
int nextOut = 0;

sem_t empty; //producer semaphore
sem_t full; //consumer semaphore

void put(char item){
        
        sem_wait(&empty);
        buffer[nextIn]=item;
        nextIn=(nextIn+1)%BUFF_SIZE;
        printf("Producing %c ...nextIn %d\n",item,nextIn);
        sem_post(&full);
        

}
void get(){
        sem_wait(&full);
        char item=buffer[nextOut];
        nextOut=(nextOut+1)%BUFF_SIZE;
        printf("consuming %c ...nextOut %d\n",item,nextOut);
        sem_post(&empty);
        

}

void*consumer(){
        for(int i=0;i<3;i++){
                get();
        }

}

void * producer(){
        for(int i=0;i<3;i++){
                put((char)('A'+i));
        }

        
        
        

}



int main()
{
  pthread_t ptid,ctid;
  //initialize the semaphores

  sem_init(&empty,0,BUFF_SIZE);
  sem_init(&full,0,0);
  for(int i=0;i<2;i++)
        pthread_create(&ptid, NULL,producer, NULL);
  for(int i=0;i<2;i++)
        pthread_create(&ctid, NULL,consumer, NULL);
  pthread_join(ptid, NULL);
  pthread_join(ctid, NULL);
  sem_destroy(&empty);
  sem_destroy(&full);
  return(0);
  
  
}

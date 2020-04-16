#include <pthread.h>
#include <stdio.h>
#include <semaphore.h>
#include<stdlib.h>

#define BUFF_SIZE 4
#define N 3

char buffer[BUFF_SIZE];
int pindex = 0;
int cindex = 0;

sem_t empty; //producer semaphore
sem_t full; //consumer semaphore
sem_t mutex;

void put(char item){
        
        sem_wait(&empty);
        //sem_wait(&mutex);
        buffer[pindex]=item;
        pindex=(pindex+1)%BUFF_SIZE;
        printf("Producing %c ...pindex %d\n",item,pindex);
        //sem_post(&mutex);
        sem_post(&full);
        

}
void get(){
        sem_wait(&full);
        sem_wait(&mutex);
        char item=buffer[cindex];
        cindex=(cindex+1)%BUFF_SIZE;
        printf("consuming %c ...cindex %d\n",item,cindex);
        sem_post(&mutex);
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
  pthread_t ptid,ctid[N];
  //initialize the semaphores

  sem_init(&empty,0,BUFF_SIZE);
  sem_init(&full,0,0);
  sem_init(&mutex,0,1);
  //for(int i=0;i<N;i++)
        pthread_create(&ptid, NULL,producer, NULL);
        
  for(int i=0;i<N;i++)
        pthread_create(&ctid[i], NULL,consumer, NULL);
        
  //for(int i=0;i<N;i++)
        pthread_join(ptid, NULL);
        
  for(int i=0;i<N;i++)
        pthread_join(ctid[i], NULL);
        
  sem_destroy(&empty);
  sem_destroy(&full);
  return(0);
  
  
}





#include <pthread.h>
#include <stdio.h>
#include <semaphore.h>
#include <stdlib.h>

int Max=10;
int searchers=0;
int deleters=0;
//int searchers=0;

struct node {
	int val;
	struct node* next;
};

struct node* head;

struct node* createnode(int value){
	struct node* temp=(struct node*)malloc(sizeof(struct node));
	temp->val=value;
	temp->next=NULL;
	return temp;
}


void addnode(struct node* temp){
	struct node* temp1=head;
	while (temp1->next!=NULL){
		temp1=temp1->next;
	}
	temp1->next=temp;
	printf("Element %d Added Successfully\n",temp->val);
	
}
int length(){
	struct node *temp1;
	
	int len=0;
	temp1=head;
	while (temp1) {
		temp1=temp1->next;
		len++;
	}
	return len;
}



void print(){
	printf("List is Here ...\n");
	struct node* temp1=head;
	while (temp1!=NULL){
		printf("%d ",temp1->val);
		temp1=temp1->next;
	}
	printf("\n");
}


void insert(){
	int val=rand()%Max;
	printf("Inserted element is %d\n",val);
	addnode(createnode(val));
}

void delete(){
	struct node *temp1,*temp2;
	if (head==NULL) return ;
	
	int len=length() - 2;
	temp1=head;
	temp2=head->next;
	while (len){
		temp2=temp2->next;
		temp1=temp1->next;
		len--;
	}
	
	temp1->next=temp2->next;
	printf("Element %d Removed Successfully\n",temp2->val);
	free(temp2);
	
}


void search(int value){
	struct node* temp=head;
	printf("Searching for Element... %d\n",value);
	while(temp){
		if (temp->val==value) { printf("Element %d Found in Linked List\n",value); return;}
		temp=temp->next;
	}
	printf("Element %d Not Found in Linked List\n",value);
	
	
}

sem_t semdel;
sem_t semins;
sem_t semsea;
sem_t semall;


void *del(){
	int c=5;
	while(c){
		
		while(length()<10)
		sleep(1);
		
		sem_wait(&semall);
		sem_wait(&semdel);
		sem_wait(&semins);
		sem_wait(&semsea);
		
		delete();
		sleep(1);
		
		sem_post(&semsea);
		sem_post(&semins);
		sem_post(&semdel);
		sem_post(&semall);
		//sleep(1);
		printf("all ends\n");
		
	}
}


void *ins(){
	int c=5;
	while(c){
		//printf("ins\n");
		
		while(length()>20)
		sleep(1);
		sem_wait(&semall);
		sem_wait(&semins);
		sem_wait(&semdel);
		sem_wait(&semsea);
		
		insert();
		printf("ins wait start\n");
		
		sleep(1);
		printf("ins wait ends\n");
		
		sem_post(&semsea);
		sem_post(&semdel);
		sem_post(&semins);
		sem_post(&semall);
		printf("all ends\n");
		//sleep(1);
	}
}

void *sea(){
	int c=5;
	while(c){
		//pid_t id=gettid();
		//printf("sea \n");
		sem_wait(&semall);
		if (searchers==0){
			sem_wait(&semsea);
			sem_wait(&semins);
			sem_wait(&semdel);
		}
		sem_post(&semall);
		
		searchers++;	
		search(rand()%Max);
		printf("Searcher is %d\n",searchers);
		sleep(1);
		
		
		searchers--;
		if (searchers==0){
			sem_post(&semsea);
			sem_post(&semdel);
			sem_post(&semins);
		}
		printf("all ends\n");
			
	}
}

int main(){
	srand(time(0));
	head=createnode(rand()%Max);
	insert();
	insert();
	insert();
	print();
	delete(); 	
	
	pthread_t psea[10],pdel[10],pins[10];
	
	sem_init(&semdel,0,1);
	sem_init(&semins,0,1);
	sem_init(&semsea,0,1);
	sem_init(&semall,0,1);
	
	
    for(int i=0;i<10;i++)
		pthread_create(&pins[i], NULL,ins, NULL);
    for(int i=0;i<10;i++)
        pthread_create(&psea[i], NULL,sea, NULL);
    for(int i=0;i<10;i++)
		pthread_create(&pdel[i], NULL,del, NULL); 
    
	
    
    for(int i=0;i<10;i++)
        pthread_join(psea[i], NULL);
    for(int i=0;i<10;i++)
        pthread_join(pdel[i], NULL);
    for(int i=0;i<10;i++)
        pthread_join(pins[i], NULL);
    
    printf("Here we go...\n");
        
    sem_destroy(&semins);sem_destroy(&semsea);sem_destroy(&semdel);
    sem_destroy(&semall);    
    
}


#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>

int main(int argc,char * argv[]){

	
	char str[10000] = "";	
	strcpy(str,"cat /proc/");
	strcat(str,argv[1]);
	strcat(str,"/cmdline | awk '{printf(\" \\n \")}'");
	system(str);
	printf("\n");
	
	strcpy(str,"cat /proc/");
	strcat(str,argv[1]);
	strcat(str,"/schedstat | awk '{printf(\"Running time %d , waiting time %d\\n\",int($1),int($2))}'");
	system(str);
	printf("\n");
	
	strcpy(str,"cat /proc/");
	strcat(str,argv[1]);
	strcat(str,"/stat | awk '{printf(\"Cpu Time in user mode %d ,Cpu Time in kernel mode %d\\n\",int($14),int($15))}'");
	system(str);
	printf("\n");
	
	strcpy(str,"cat /proc/");
	strcat(str,argv[1]);
	strcat(str,"/environ | awk '{printf(\"\\n\")}'");
	system(str);
	printf("\n");
	
	strcpy(str,"cat /proc/");
	strcat(str,argv[1]);
	strcat(str,"/maps | awk '{print $1 $2}'");
	system(str);
	printf("\n");		
	return 0;
}

#include <stdio.h>
#include <string.h>

void get_boot ()
{
 FILE* fp;
 char buffer[10000];
 char *match;
 char *str1,*str2,*str3;

 size_t bytes_read;
 int ti;
 
 fp = fopen ("/proc/uptime", "r");
 bytes_read = fread (buffer, 1, sizeof (buffer), fp);
 fclose (fp);
 
 buffer[bytes_read] = '\0';
 sscanf(buffer,"%d",&ti);
 int day=ti/(3600*24);
 ti%=(3600*24);
 int hr=ti/3600;
 ti%=3600;
 int min=ti/60;
 ti%=60;
 
 	
 printf("Total Time is %d:%d:%d:%d\n",day,hr,min,ti);

}


void get_mem ()
{
 FILE* fp;
 char buffer[10000];
 char *match;
 char *str1,*str2,*str3;

 size_t bytes_read;
 int mem;
 
 fp = fopen ("/proc/meminfo", "r");
 bytes_read = fread (buffer, 1, sizeof (buffer), fp);
 fclose (fp);

 buffer[bytes_read] = '\0';
 match = strstr (buffer, "MemTotal:");
 sscanf(match,"MemTotal: %d",&mem);
 printf("MemTotal is %d KB\n",mem);

}


void get_version ()
{
 FILE* fp;
 char buffer[10000];
 char *match;
 char *str1,*str2,*str3;

 size_t bytes_read;
 int clock_speed;
 
 fp = fopen ("/proc/version", "r");
 bytes_read = fread (buffer, 1, sizeof (buffer), fp);
 fclose (fp);

 
 buffer[bytes_read] = '\0';
 match = strstr (buffer, "Linux version");
 
 printf("%s\n",match);

}


void get_cpu_info ()
{
 FILE* fp;
 char buffer[10024];
 size_t bytes_read;
 char* match;
 int clock_speed;
 
 fp = fopen ("/proc/cpuinfo", "r");
 bytes_read = fread (buffer, 1, sizeof (buffer), fp);
 fclose (fp);

 
buffer[bytes_read] = '\0';
 
match = strstr (buffer, "processor");
 
while(match!=NULL){
 match = strstr (match, "processor");
 sscanf (match, "processor : %d", &clock_speed);
 printf("Processor %d\n",clock_speed);
 match = strstr (match, "cpu MHz");
 sscanf (match, "cpu MHz : %d", &clock_speed);
 printf("cpu MHz of This Processor %d\n",clock_speed);
 match = strstr (match, "cpu cores");
 sscanf (match, "cpu cores : %d", &clock_speed);
 printf("cpu cores of This Processor %d\n",clock_speed);
 match=strstr (match, "processor");
}
 printf("\n");
}




int main ()
{
get_cpu_info();
get_version();
get_mem();
get_boot();

 return 0;
}

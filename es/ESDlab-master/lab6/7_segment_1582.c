/***************Seven Segments***************/
/***************Connections******************/
/**********		SS data --- PORT 0	    ******/
/**********		SS control --- PORT 2	******/
#include<reg51.h>
// _gfedcba

char arr[10]={0xbf,0x86,0xdb,0xcf,0xe6,0xed,0xfd,0x87,0xff,0xef}; // an array that defines the value that should be loaded into port 0
void delay(void);  //function that used to create delay

void main(void)
{
	int a;
	while(1)  // an infinite loop
	{	
 		for(a=0;a<10;a++)
 		{
 			P2=0x02;
		  	P0=arr[a];
			delay(); //creates delay
	  		delay();
		    delay();
		}
	}
}
void delay(void)
{	// delay function that creates delay of 30000 instructions
 	int f;
 	for(f=0;f<30000;f++);
}


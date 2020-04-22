/***************Seven Segments***************/
/***************Connections******************/
/**********		SS data --- PORT 0	    ******/
/**********		SS control --- PORT 1/2	******/
#include<reg51.h>
char arr[10]={0xbf,0x86,0xdb,0xcf,0xe6,0xed,0xfd,0x87,0xff,0xef};
// char arr[] stores the hex values of element [0.,1.,....,9.]
void delay(void);
void main(void)
{
	int i,j,k,l,m;	
	for(l=0;l<10;l++)
	{
		for(k=0;k<10;k++)
		{
			for(j=0;j<10;j++)
			{
				for(i=0;i<10;i++)
				{
					for(m=0;m<50;m++)
					{
						// total loop count = 10**4 * 50=500000 times
					P2=0x01;
					P0=arr[i];
					//first led changes after 50 units of times
					delay();
					P2=0x02;
					P0=arr[j]; //second led will change after 500 units of time 
					delay();
					P2=0x04;
					P0=arr[k];// third led will change after 5000 unit of time 
					
					delay();
					P2=0x08;
					P0=arr[l]; // fourth led will change after 50000 unit of time 
					delay();		   
					}
				}
			

			}
		
		}
	}
}

/*
patterns 
* 	0000 -50 times
	1000-50	times
	2000-50 times
	.
	.
	.
	.
	.
	9000 - 50 times
	
	0100 - 50 times
	1100 - 50 times
	2100 - 50 times
	.
	.
	.
	.
	.
	9100 - 50 times
	.
	.
	.
	.
	.
	.
	.
	.
	.
	.
	9900 - 50 times
	
	0010 - 50 times
	1010 - 50times
	.
	.
	.
	.
	.
	.
	.
	.
	.
	.
	9910 - 50 times
	0020 - 50 times
	.
	.
	.
	.
	.
	.
	.
	.
	.
	.
	9990 - 50 times
	0001- 50 times
	1001 - 50 times
	.
	.
	.
	.
	.
	.
	.
	.
	.
	9999 - 50 times
	
	then it stops
	*/
	
	
void delay(void)
{	//used to create the delay
	int f;
	for(f=0;f<50;f++);
}

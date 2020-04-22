#include<reg51.h>
//////////// PIN DEFINED ///////////////
#define KEYPAD_PORT  P1
#define CONTROL  P2
#define DATA P3
//control port2
sbit RS=P2^0;
sbit E=P2^1;
#include"delay.h"
#include"lcd.h"
#include"keypad.h"
#include"reg51.h"

int get_num(char ch)         //convert char into int
/*
 * this function used to convert the string character to interger.
 */
  
{
	switch(ch)
	{
		case '0': return 0; break;
		case '1': return 1; break;
		case '2': return 2; break;
		case '3': return 3; break;
		case '4': return 4; break;
		case '5': return 5; break;
		case '6': return 6; break;
		case '7': return 7; break;
		case '8': return 8; break;
		case '9': return 9; break;
		
	}
}

void delay1()
{
	// used to create delay
int i;
for(i=0;i<=30000;i++);
}
void print(int temp)
{
	/*
	 * this function used to print/display the value(integer) to lcd in terms of string 
	 * */
	 
 	 char arr[10];
	 int i=0;
	 int j=0;
	 if(temp==0)
	 {		//if temp is simply 0 then directly print 0
	 	  data_lcd(48);
		  return;
	 }
	 // otherwise store the rightmost digit to array print then later print their corresponding ascii value 
	 while(temp!=0)
	 {
	 	int w;
		w=temp%10;
		arr[i]=w+48;
		i++;
		temp=temp/10;
	 }
	 
	 j=i-1;
	 while(j>=0)
	 {
	 		 data_lcd(arr[j]);
				j--;
	 }
}
void main(void)
{
  unsigned char key1,key2,key3;
  init_lcd();                           //lcd init.
  cmd_lcd(0x80);                        //Set curser position
  string_lcd("Calculator:");        //Display string
  P0=0X00;  //0 means no light  8 bit zero so no i/p goes to led
  while(1)
  {
  	int n1=0;
	int n2=0;
	key1 = keyscan();		//	input maybe number
	
	key2 = keyscan();		// input a character 
	key3 = keyscan();		//input a number

        n1 = get_num(key1); 
		n2 = get_num(key3);   
		cmd_lcd(0xc0);
        
		switch(key2)
        {
        	case 'A':
				// A is used for addition
				
				data_lcd(key1);
				string_lcd("+"); 
				data_lcd(key3);
				string_lcd("=");
				print(n1+n2);	//print the addition of two number
        		P0=0X01;
				delay1();
				break;
			case 'B':
				//data_lcd(n1-n2+48);
				data_lcd(key1);
				string_lcd("-"); 
				data_lcd(key3);
				string_lcd("=");
				if(n1<n2)
				{
					string_lcd("-"); 
					  print(n2-n1);		//print the subtraction of two number
				}
				else
				{
					print(n1-n2);		//print the subtraction of two number
				}
        		P0=0X02;
				delay1();
				break;
        	case 'C':
				//data_lcd(n1*n2+48);
				data_lcd(key1);
				string_lcd("*"); 
				data_lcd(key3);
				string_lcd("=");
				print(n1*n2);	//print the multiplication of two number
        		P0=0X04;
				delay1();
				break;
        	case 'D':
				//data_lcd(n1/n2+48);
				data_lcd(key1);
				string_lcd("/"); 
				data_lcd(key3);
				string_lcd("=");
				if(n2!=0)
				print(n1/n2);	//divide the no.
				else
				string_lcd("div by 0"); 
        		P0=0X08;
				delay1();
				break;     	
        		
        	default:
        		break;
		}
        //data_lcd(key);                                //Display pressed key on lcd
  }
}

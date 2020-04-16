#include<reg51.h>
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

void delay1()
{
int i;
for(i=0;i<=30000;i++);
}

void main(void)
{
  unsigned char key;
  init_lcd();                           //lcd init.
  cmd_lcd(0x80);                        //Set curser position
  string_lcd("Key : ");                 //Display string
  P0=0X00;                              //0 means no light  8 bit zero so no i/p goes to led
  while(1)
  {
    key = keyscan();  
    cmd_lcd(0xc0);
    switch(key){
      case '0':
                data_lcd(key);
        	P0=0X01;
		delay1();
		break;
      case '1':
				        
      case '2':
				        
      case '3':
				      
      case '4':
				       
      case '5':                         //COMPLETE REST OF THE CASES
      
      case '6':
				        
      case '7':
				        
      default:
        	break;
  }
  data_lcd(key);                                //Display pressed key on lcd
  }
}

/*
#include<reg51.h>
//////////// PIN DEFINED ///////////////
#define KEYPAD_PORT  P1
#define DATA P1
//control port2
sbit RS=P2^0;
sbit E=P2^1;

#include"delay.h"
#include"lcd.h"
#include"keypad.h"

void main(void)
{
  unsigned char key;
  init_lcd();                           //lcd init.
  cmd_lcd(0x80);                        //Set curser position
  string_lcd("Press key : ");        //Display string
  while(1)
  {
        cmd_lcd(0xc0);
        key = keyscan();                        //Scan keypad
        data_lcd(key);                                //Display pressed key on lcd
  }
}
*/
#include<reg51.h>
#define KEYPAD_PORT  P1
#define CONTROL  P2
#define DATA P3

//control port2
sbit RS=P2^0;
sbit E=P2^1;
#include<string.h>
#include "delay.h"
#include "lcd.h"
#include "keypad.h"
#include "reg51.h"

//////////// PIN DEFINED ///////////////



void delay1()
{
	int i;
	for(i=0;i<=30000;i++); // delay function that creates delay of 30000 instructions
}

void main(void)
{
  unsigned char key;

  char st[]="                Listen student of mnit !! HI From Us.                ";
  int len = strlen(st);
  int i;
  len-=32;
  i=0x0;
  init_lcd();                           //lcd init.
  P0=0X00;  //0 means no light  8 bit zero so no i/p goes to led
  while(1)
  {
    cmd_lcd(0x80);
  if(i>=16 && i<=32+len)
      string_lcd(st+(i-16));
  else
    string_lcd("                ");
  cmd_lcd(0xc0);
  if(i>=0 && i<=16+len)
    string_lcd(st+i);
  else
    string_lcd("                ");

  delay1();
  
  i++;
  i=i%(len+32);
  }
}

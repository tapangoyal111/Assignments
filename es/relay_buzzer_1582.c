//Keil C Program
/*
When we need more than one relays, using transistors and diodes become bulky. In these cases we can use ULN drivers. These are monolithic IC s consists of High Voltage High Current Darlington transistor arrays. When using these driver ICs we don’t need to connect freewheeling diode as they have built in clamp diodes. Here we are using ULN2003 for demostration.
*/

#include<reg52.h>

#define relayport P2

void Delay_ms(int);

void main()
{
  do
  {
    relayport = 0xFF; //All relays On
    Delay_ms(1000);
    relayport = 0x00; //All relays Off
    Delay_ms(1000);
  }while(1);
}

void Delay_ms(int k)
{
  int j;
  int i;
  for(i=0;i<k;i++)
  {
    for(j=0;j<100;j++)
    {
    }
  }
}

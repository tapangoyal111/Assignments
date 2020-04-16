/*******************RTC************************/
/****************connections ******************/
/*********	LCD control --- PORT 0	**********/
/*********	LCD DATA ----- PORT 2   **********/
/*********	RTC SEC ---- PORT 1	    **********/
#include<reg51.h>
#include<intrins.h>
typedef unsigned char uchar;
typedef unsigned long ulong;
typedef unsigned int  uint;
#define		TIMER_RELOAD (-921)
#define		port_delay()	 _nop_(), _nop_(), _nop_(), _nop_()
#define		AVG	10
sbit  LRS		=   P0 ^ 0;
sbit  LEN		=   P0 ^ 1;
sbit ICLK		=	P1 ^ 0;
sbit IDAT		=	P1 ^ 1;

uint count;
uchar rdata,edata;
uint time;
uchar second,minute,hour,day,date,month,year;

void timer0(void)
interrupt 1 using 1
{
	count++;
	TH0 = (uchar)(TIMER_RELOAD>>8);
	TL0 = (uchar)TIMER_RELOAD;
}

void delay(uint n)
{
	n = count + n;
   while (n != count);
}

void dispstr(uchar *str, uchar stcol, uchar encol) 
{
   uint q;
	if(stcol <= 15)
		P2 = 0x80 + stcol;
	else
		P2 = 0xB0 + stcol;
	LRS = 0;
	LEN = 1;
    LEN = 0;
    delay(1);
	LRS = 1;
	q=0;
	for(; stcol <= encol; stcol++)
	{
		if(stcol == 16)
		{
			P2 = 0xB0 + stcol;
			LRS = 0;
			LEN = 1;
		   LEN = 0;
			delay(1);
			LRS = 1;
		}
		P2 = str[q];
		q++;
		LEN = 1;
	   LEN = 0;
		delay(1);
	}
}
 
void dispnum(uint no, uchar stcol, uchar encol) 
{
	uchar temp[5];
	uchar i;
	for (i = 0; i < 2; i++)
	{
		temp[i] = no % 10;
		no /= 10;
	}
	if(stcol <= 15)
		P2 = 0x80 + stcol;
	else
		P2 = 0xB0 + stcol;
	LRS = 0;
	LEN = 1;
    LEN = 0;
    delay(1);
	LRS = 1;
	i = 1;
	for(; stcol <= encol; stcol++)
	{
		P2 = temp[i] + 0x30;
		i--;
		LEN = 1;
	    LEN = 0;
		delay(1);
	}
}

void clrlcd()
{
	LRS = 0;
	P2 = 0x01;
	LEN = 1;
	LEN = 0;
	delay(6);
}

void str1307(void)
{
   IDAT = 1 ;
   _nop_() , _nop_() , _nop_() ;
   ICLK = 1 ;
   _nop_() , _nop_() , _nop_() ;
   IDAT = 0 ;
   _nop_() , _nop_() , _nop_() ;
   ICLK = 0 ;
   _nop_() , _nop_() , _nop_() ;
}

void stp1307(void)
{
   IDAT = 0 ;
   _nop_() , _nop_() , _nop_() ;
   ICLK = 1 ;
   _nop_() , _nop_() , _nop_() ;
   IDAT = 1 ;
   _nop_() , _nop_() , _nop_() ;
   ICLK = 0 ;
   _nop_() , _nop_() , _nop_() ;
}

void clock(void)
{
   _nop_() ; _nop_() ; _nop_() ;
   ICLK = 1 ;
   _nop_() ; _nop_() ; _nop_() ;
   ICLK = 0 ;
   _nop_() ; _nop_() ; _nop_() ;
}

void ack1307(void)
{
    IDAT = 0 ;
    clock() ;
}

void nack1307(void)
{
    IDAT = 1 ;
    clock() ;
}

void opdat(char rtcdata)
{
   char i ;
   for ( i = 0 ; i < 8 ; i++ )
   {
      if ( ( rtcdata >> ( 7 - i ) ) & 0x01 )  IDAT = 1 ; 
      else	 											 IDAT = 0 ;
         clock() ;
   }
}

void waitack(void)
{
//   watch() ;
   IDAT = 1 ;
   _nop_() , _nop_() , _nop_() ;
   while ( IDAT ) ;
   ICLK = 1 ;
   _nop_() , _nop_() , _nop_() ;
   ICLK = 0 ;
}

char getdat(void)
{
   char i , dat ;
//   watch() ;
   IDAT = 1 ;
   _nop_() , _nop_() , _nop_() ;
   for ( i = 0 ; i < 8 ; i++ ) 
   {
      ICLK = 1 ;
      dat = ( ( ( dat << 1 ) & 0xfe ) | IDAT ) ;
	   _nop_() , _nop_() , _nop_() ;
      ICLK = 0 ;
 	   _nop_() , _nop_() , _nop_() ;
   }
   return dat ;
}


void getrtc(void)
{
   char rdata ;
//   watch() ;
   str1307() ;
   opdat(0xd0) ;
   waitack() ;
   opdat(0x00) ;
   waitack() ;
   stp1307() ;
   _nop_() , _nop_() , _nop_() ;
   str1307() ;
   opdat(0xd1) ;
   waitack() ;
   rdata = getdat() ;
   ack1307() ;
	second = ( rdata & 0x7f) ;
   rdata = getdat() ;
   ack1307() ;
	minute = ( rdata & 0x7f) ;
   rdata = getdat() ;
   ack1307() ;
	hour = ( rdata & 0x3f) ;
   rdata = getdat() ;
   ack1307() ;
//   watch() ;
	day = ( rdata & 0x07) ;
   rdata = getdat() ;
   ack1307() ;
	date = ( rdata & 0x3f) ;
   rdata = getdat() ;
   ack1307() ;
	month = ( rdata & 0x1f) ;
   rdata = getdat() ;
   nack1307() ;
	year = rdata ;
   stp1307() ;
}

void setrtc(void)
{
   char rdata ;
//   watch() ;
   str1307() ;
   opdat(0xd0) ;
   waitack() ;
   opdat(0x00) ;
   waitack() ;
   rdata = ( second & 0x7f) ;
   opdat(rdata) ;
   waitack() ;
   rdata = ( minute & 0x7f) ;
   opdat(rdata) ;
   waitack() ;
   rdata = ( hour & 0x3f) ;
   opdat(rdata) ;
   waitack() ;
   rdata = ( day & 0x07) ;
   opdat(rdata);
   waitack();
   rdata = ( date & 0x3f);
   opdat(rdata) ;
   waitack() ;
   rdata = ( month & 0x1f);
   opdat(rdata);
   waitack() ;
   rdata = year ;
   opdat(rdata) ;
   waitack() ;
   stp1307() ;
}

unsigned char bcdtime(unsigned char x)
{
    return ( ( ( x / 10 ) << 4 ) + ( x % 10 ) ) ;
}

unsigned char binarytime(unsigned char x)
{
    return ( ( ( x >> 4 ) * 10 ) + ( x & 0xf ) ) ;
}

void getrtc1(void)
{
    getrtc() ;
//    watch() ;
    year = binarytime( year );
    month = binarytime( month );
    date  = binarytime( date );
    hour = binarytime( hour );
    minute = binarytime( minute );
    second = binarytime( second );
}

void setrtc1(void)
{
 //   watch() ;
    year   = bcdtime( year ) ;
    month  = bcdtime( month ) ;
    date   = bcdtime( date ) ;
    hour   = bcdtime( hour ) ;
    minute = bcdtime( minute ) ;
    second = bcdtime( second ) ;
    setrtc() ;
}



void io_open(void)
{
	LEN = 0;
	TMOD = 0x21;
	IE = 0x92; //1001 0010
	SCON = 0x50; //0101 0000
	REN = 1;
	TL0 = (uchar)TIMER_RELOAD;
	TH0 = (uchar)TIMER_RELOAD >> 8;
	TH1 = TL1 = 0xFA;
	TR0 = 1;
	TR1 = 1;
}

void initlcd(void)
{
	LEN = 0;
	LRS = 0;
	delay(20);

    P2 = 0x30;
    LEN = 1;
    delay(1);
    LEN = 0;
    delay(6);
  
    P2 = 0x30;
    LEN = 1;
    delay(1);
    LEN = 0;
    delay(6);

    P2 = 0x30; 
    LEN = 1;
    delay(1);
    LEN = 0;
    delay(6);

    P2 = 0x38;  //funtion set	
    LEN = 1;
    delay(1);
    LEN = 0;
    delay(6);
 
    P2 = 0x0c8;    //display off
    LEN = 1;
    delay(1);
    LEN = 0;
    delay(6);

    P2 = 0x01;  //clear display;
    LEN = 1;
    delay(1);
    LEN = 0;
    delay(6);

   P2 = 0x06; //entry mode set
   LEN = 1;
   delay(1);
   LEN = 0;
   delay(6);

   P2 = 0x0c; //display  on
   LEN = 1;
	delay(1);
   LEN = 0;
   delay(6);

}

void main(void)
{
		
	io_open();
	initlcd();
	clrlcd ();
	//dispstr("     ADVANCE    ",0,15);
	delay(2000);
	minute = 52;
	hour = 3;
	second = 1;
	date = 4;
	month = 5;
	year = 4;

	setrtc1();//
//	getrtc1();
	dispnum(date,1,2);
	dispnum(month,4,5);
	dispnum(year,7,8);
	
	dispstr("/",3,3);
	dispstr("/",6,6);

	dispstr(":",18,18);
	dispstr(":",21,21);
	while(1)
	{
		getrtc1();
		dispnum(hour,16,17);
		dispnum(minute,19,20);
		dispnum(second,22,23);
	}
}

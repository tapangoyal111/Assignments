#include <iostream>
#include <fstream>
#include <string>
#include <bits/stdc++.h> 
#include <boost/algorithm/string.hpp> 
using namespace std;
int main(){
    string line;
    fstream newfile;
    string tp;
  string array[]={"MemTotal:","MemFree:","MemAvailable:","SwapTotal:","SwapFree:"};
  int MemTotal,MemFree,MemAvailable,SwapTotal,SwapFree;
    newfile.open("/proc/stat",ios::in);
    int k=0;
        if (newfile.is_open()){   
      
      while(getline(newfile, tp)){ 
            if(tp.find("cpu")!=string::npos){
                vector<string> result;
                boost::split(result, tp, boost::is_any_of(" ")); 
               cout<<result[0]<<endl;
               cout<<result[1]<<endl;
               cout<<result[2]<<endl;
               cout<<result[4]<<endl;
               cout<<result[5]<<endl;
               cout<<result[6]<<endl;
                         
            }
        }
      }
      newfile.close();
      
   int num;
   string kb;
   freopen("/proc/meminfo","r",stdin);
   for(int i=0;i<20;i++){
        cin>>tp;
        cin>>num;
        cin>>kb;
        if(tp==array[0]){
            MemTotal=num;
            cout<<"MemTotal:"<<MemTotal<<endl;
        }
        else if(tp==array[1]){
            MemFree=num;
            cout<<"MemFree:"<<MemFree<<endl;
        }
        else if(tp==array[2]){
            MemAvailable=num;
            cout<<"MemAvailable:"<<MemAvailable<<endl;
        }
        else if(tp==array[3]){
            SwapTotal=num;
            cout<<"SwapTotal:"<<SwapTotal<<endl;
        }
        else if(tp==array[4]){
            SwapFree=num;
            cout<<"SwapFree:"<<SwapFree<<endl;
        }
   }
   int SwapUsed=SwapTotal-SwapFree;
   cout<<"SwapUsed:"<<SwapUsed<<endl;
   
   float pm,ps;
   pm=((float)MemFree/MemTotal)*100;
   ps=((float)SwapFree/SwapTotal)*100;
   
   cout<<"Type    "<<"      "<<"%"<<endl;
   cout<<"MemoryFree"<<"    "<<pm<<"%"<<endl;
   cout<<"SwapFREE  "<<"    "<<ps<<"%"<<endl;
   
   fclose(stdin);
   
   newfile.open("/proc/swaps",ios::in);
        if (newfile.is_open()){   
      
      while(getline(newfile, tp)){ 
            if(tp.find("/swap")!=string::npos){
                vector<string> result;
                boost::split(result, tp, boost::is_any_of("\t")); 
              
               cout<<result[0].<<endl;
               cout<<result[2]<<endl;
            }
        }
      }
      newfile.close();
   
     
     

return 0;
}

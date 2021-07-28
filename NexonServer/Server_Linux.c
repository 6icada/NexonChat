//Code by 6icada
//Please do not copy code

//Adding libraries
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <zconf.h>

//PortOpen function
void PortOpen(){
  //Adding vars
  char cmd[150];
  const int MainPort = 4444;

  //Opening MainPort
  sprintf(cmd, "ncat --broker --listen -p %d -v < Banner.md", MainPort);
  system(cmd);
}

//Main function
int main(){
  //Adding vars
  char cmd1[150];
  char cmd[150];
  const int MainPort = 4444;
  int x = getuid();

  //Checking root access
  if(x == 0){
    
    //Opening MainPort
    PortOpen(cmd, MainPort);
  }
  else{
    //Warning
    printf("\n\nI do not have root access!!!\n\n");
  }
}

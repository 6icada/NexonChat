//Code by 6icada
//Please do not copy code

//Adding libraries
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//Main function
int main(){
  //Warning
  printf("This program needs \"nc\" Please install it!");

  //Link for netcat(nc)
  printf("Download netcat(nc) - https://joncraton.org/blog/46/netcat-for-windows/\n");

  //Adding vars
  char cmd[150];
  const int MainPort = 4444;
  //char IPv4[15] = "255.255.255.255";
  int x;
  int y;
  char YesOrNo;

  if(YesOrNo == 'Y'){
    //Starting Action
    printf("Enter number(192.168.x.1): ");
    scanf("%d", x);

    for(y = 1; y < 256; y++){
      sprintf(cmd, "nc -w 1 -v 192.168.%d.%d %d", x, y, MainPort);
      system(cmd);
    }
  }
  else{
    //Starting Action
    for(x = 1; x < 256; x++){
      for(y = 1; y < 256; y++){
        //sprintf(cmd, "nmap -p %d 192.168.%d.%d", MainPort, x, y);
        sprintf(cmd, "nc -w 1 -v 192.168.%d.%d %d", x, y, MainPort);
        system(cmd);
      }
    }
  }
}

//Code by DisMe ^-^
//Please do not copy code

//Adding libraries
#include <stdio.h>
#include <stdlib.h>
#include <zconf.h>
#include <string.h>
#include <stdbool.h>

//Main function
int main(){
  //Adding vars
  char cmd[150];
  char IPv4[15] = "255.255.255.255";
  const int MainPortForChatting = 4444;
  const int MainPortForShell = 1111;
  const int MainPortForLogIn = 2222;
  int x = getuid();

  //Checking root access ^-^
  if(x == 0){
    //Installing tools
    {
      //Fixing broken packages ^-^
      system("apt --fix-broken install -y > /dev/null");

      //Installing ufw(Firewall)
      system("apt install ufw -y > /dev/null");
    }
    //Choosing IPv4 :)
    printf("Enter IPv4: ");
    scanf("%s", &IPv4);

    //Starting Action
    sprintf(cmd, "ufw deny %s to any port %d", IPv4, MainPortForChatting);
    system(cmd);
    sprintf(cmd, "ufw deny %s to any port %d", IPv4, MainPortForLogIn);
    system(cmd);
    sprintf(cmd, "ufw deny %s to any port %d", IPv4, MainPortForShell);
    system(cmd);
  }
  else{
    //Warning
    printf("\n\nI do not have root access!!!\n\n");
  }
}

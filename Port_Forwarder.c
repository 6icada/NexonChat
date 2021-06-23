//Code by 6icada
//Please do not copy code

//Adding libraries
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//Main function
int main(){
  //Adding vars
  const int MainPort = 4444;
  int port;
  char cmd[150];
  char YesOrNo;

  //Starting Action
  printf("Default port is 4444 do you want to change it? :  ");
  scanf("%c", &YesOrNo);

  if(YesOrNo == 'Y'){
    //Adding port
    printf("Enter port: ");
    scanf("%d", &port);

    //Forwarding Port
    sprintf(cmd, "./ngrok tcp %d", port);
    system(cmd);
  }
  else if(YesOrNo == 'N'){
    //Forwarding Port
    sprintf(cmd, "./ngrok tcp %d", MainPort);
    system(cmd);
  }
}

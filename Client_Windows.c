//Code by 6icada
//Please do not copy code

//Adding libraries
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//Main function
int main(){
  //Warning
  printf("This program needs \"nc\" Please install it!\n");
  printf("This program needs \"mawk\" Please install it!\n\n");

  //Links for mawk and netcat(nc)
  printf("Download MAWK - http://gnuwin32.sourceforge.net/packages/mawk.htm\n");
  printf("Download netcat(nc) - https://joncraton.org/blog/46/netcat-for-windows/");

  //Adding vars
  char IPv4_2[30] = "ngrok.io";
  char cmd[150];
  char NickName[20] = "NickName";
  char IPv4[15] = "255.255.255.255";
  int port;
  char YesOrNo;
  int TimeOut;

  //Starting Action

  //Port forwarded server or not
  printf("Is server port forwarded? :  ");
  scanf("%c", &YesOrNo);

  //Port forwarded server or not
  if(YesOrNo == 'Y'){
    //Choosing IPv4
    printf("Enter IPv4: ");
    scanf("%s", &IPv4_2);

    //Choosing port
    //printf("Enter port: ");
    //scanf("%d", port);

    printf("Enter Forwarded port: ");
    scanf("%d", &port);

    //Enter NickName
    printf("Enter NickName(MAX 20): ");
    scanf("%s", &NickName);

    //TimeOut
    printf("Enter TimeOut(Seconds): ");
    scanf("%d", &TimeOut);

    //Choosing TimeOut
    //printf("Enter TimeOut(Seconds): ");
    //scanf("%d", &TimeOut);

    if(TimeOut == 0){
      //Connecting to server
      sprintf(cmd, "mawk -W interactive '$0=\"\e[0;37m[Client]@%s\e[0m: \"$0' | nc -v %s %d", NickName, IPv4_2, port);
      system(cmd);
    }
    else{
      //Connecting to server
      sprintf(cmd, "mawk -W interactive '$0=\"\e[0;37m[Client]@%s\e[0m: \"$0' | nc -w %d -v %s %d", NickName, TimeOut, IPv4_2, port);
      system(cmd);
    }
  }
  else if(YesOrNo == 'N'){
    //Choosing IPv4
    printf("Enter IPv4: ");
    scanf("%s", &IPv4);

    //Choosing port
    printf("Enter port: ");
    scanf("%d", &port);

    //Enter NickName
    printf("Enter NickName(MAX 12): ");
    scanf("%s", &NickName);

    //TimeOut
    printf("Enter TimeOut(Seconds): ");
    scanf("%d", &TimeOut);

    //Choosing TimeOut
    //printf("Enter TimeOut(Seconds): ");
    //scanf("%d", &TimeOut);

    if(TimeOut == 0){
      //Connecting to server
      sprintf(cmd, "mawk -W interactive '$0=\"\e[0;37m[Client]@%s\e[0m: \"$0' | nc -v %s %d", NickName, IPv4, port);
      system(cmd);
    }
    else{
      //Connecting to server
      sprintf(cmd, "mawk -W interactive '$0=\"\e[0;37m[Client]@%s\e[0m: \"$0' | nc -w %d -v %s %d", NickName, TimeOut, IPv4, port);
      system(cmd);
    }
  }
}

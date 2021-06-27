//Code by 6icada
//Please do not copy code

//Adding libraries
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//Main function
int main(){
  //Warning
  printf("This program needs \"ncat\" Please install it!\n");
  printf("This program needs \"mawk\" Please install it!\n\n");

  //Links for mawk and ncat
  printf("Download MAWK - http://gnuwin32.sourceforge.net/packages/mawk.htm\n");
  printf("Download Ncat - https://nmap.org/ncat/");

  //Adding vars
  char NickName[20] = "NickName";
  char cmd[150];
  const int MainPort = 4444;
  int port;
  char YesOrNo;
  char YesOrNo2;
  char TimeOut;

  //Starting Action
  printf("If you want to port forward use ngrok in new tab like this \"ngrok tcp <and your port>\"\n");
  printf("Default port is 4444 do you want to change it? :  ");
  scanf("%c", &YesOrNo);

  if(YesOrNo == 'Y'){
    //Choosing port
    printf("Enter port: ");
    scanf("%d", &port);

    //Enter NickName
    //printf("Enter NickName(MAX 20): ");
    //scanf("%s", &NickName);


    //Enter NickName
    //printf("Enter NickName(MAX 20): ");
    //scanf("%s", &NickName);

    //TimeOut
    printf("Enter TimeOut(Enter 0 for nonending chat): ");
    scanf("%d", &TimeOut);

    if(TimeOut == 0){
      //Opening MainPort
      sprintf(cmd, "mawk -W interactive '$0=\"\e[0;31m[Server]@MainServer\e[0m: \"$0' | ncat --broker --listen -p %d -v", MainPort);
      system(cmd);
    }
    else{
      //Opening MainPort
      sprintf(cmd, "mawk -W interactive '$0=\"\e[0;31m[Server]@%s\e[0m: \"$0' | ncat -w %d --broker --listen -p %d -v", NickName, TimeOut, MainPort);
      system(cmd);
    }
    
    /*
    if(TimeOut == 0){
      //Opening port
      sprintf(cmd, "mawk -W interactive '$0=\"\e[0;31m[Server]@%s\e[0m: \"$0' | ncat --broker --listen -p %d -v", NickName, port);
      system(cmd);
    }
    else{
      //Opening port
      sprintf(cmd, "mawk -W interactive '$0=\"\e[0;31m[Server]@%s\e[0m: \"$0' | ncat -w %d --broker --listen -p %d -v", NickName, TimeOut, port);
      system(cmd);
    }
  }
  else if(YesOrNo == 'N'){
    //Enter NickName
    //printf("Enter NickName(MAX 20): ");
    //scanf("%s", &NickName);

    //TimeOut
    printf("Enter TimeOut(Enter 0 for nonending chat): ");
    scanf("%d", &TimeOut);

    if(TimeOut == 0){
      //Opening MainPort
      sprintf(cmd, "mawk -W interactive '$0=\"\e[0;31m[Server]@MainServer\e[0m: \"$0' | ncat --broker --listen -p %d -v", MainPort);
      system(cmd);
    }
    else{
      //Opening MainPort
      sprintf(cmd, "mawk -W interactive '$0=\"\e[0;31m[Server]@%s\e[0m: \"$0' | ncat -w %d --broker --listen -p %d -v", NickName, TimeOut, MainPort);
      system(cmd);
    }
  }
  */
}

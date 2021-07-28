//Code by 6icada
//Please do not copy code

//Adding libraries
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <zconf.h>

//ToolInstaller function
void ToolInstaller(){
  //Installing tools
  {
    //Fixing broken pkg
    system("apt --fix-broken install -y > /dev/null");

    //Installing netcat(nc)
    system("apt install netcat -y > /dev/null");

    //Installing ncat
    system("apt install ncat -y > /dev/null");

    //Installing mawk
    system("apt install mawk -y > /dev/null");
  }
}

//Main function
int main(int argc, char *argv[]){
  //Adding vars
  char cmd[150];
  char IPv4[15] = "255.255.255.255";
  const int MainPort = 4444;
  int x = getuid();
  int y;
  char NickName[20];

  //Checking root access
  if(x == 0){
    //Checking argc and argv
    if(argc == 1){
      //MSG
      printf("Type \"NexonChat -h\" for help\n");
    }
    else if(strcmp(argv[1], "-h") == 0 || strcmp(argv[1], "--help") == 0){
      //MSG
      printf("Usage:\n");
      printf("-S            - Server\n");
      printf("-cS           - Controller Server\n");
      printf("-C            - Client\n");
      printf("-h            - This MSG\n");
      printf("--Scan-Server - Scan Server\n");
    }
    else if(strcmp(argv[1], "-S") == 0){
      //Choosing NickName
      printf("Enter NickName(MAX 20): ");
      scanf("%s", &NickName);

      //Installing tools
      ToolInstaller();

      //Starting Action
      sprintf(cmd, "mawk -W interactive '$0=\"\e[0;31m[Server]@%s\e[0m: \"$0' | nc -lnvp %d", NickName, MainPort);
      system(cmd);
    }
    else if(strcmp(argv[1], "-cS") == 0){
      //Choosing NickName
      printf("Enter NickName(MAX 20): ");
      scanf("%s", &NickName);

      //Installing tools
      ToolInstaller();

      //Starting Action
      sprintf(cmd, "mawk -W interactive '$0=\"\e[0;31m[Server]@%s\e[0m: \"$0' | ncat --broker --listen -p %d -v", NickName, MainPort);
      system(cmd);
    }
    else if(strcmp(argv[1], "-C") == 0){
      //Choosing NickName
      printf("Enter NickName(MAX 20): ");
      scanf("%s", &NickName);

      //Installing tools
      ToolInstaller();

      //Choosing IPv4
      printf("Enter IPv4: ");
      scanf("%s", &IPv4);

      //Starting Action
      sprintf(cmd, "mawk -W interactive '$0=\"\e[0;37m[Client]@%s\e[0m: \"$0' | nc -v %s %d", NickName, IPv4, MainPort);
      system(cmd);
    }
    else if(strcmp(argv[1], "--Scan-Server") == 0){
      //Installing tools
      ToolInstaller();

      //Enter y
      printf("Enter y(192.168.y.1): ");
      scanf("%d", &y);

      //Starting Action
      for(int i = 1; i < 256; i++){
        sprintf(cmd, "nc -w 1 -v 192.168.%d.%d %d> /dev/null", y, i, MainPort);
        system(cmd);
      }
    }
  }
  else{
    //Warning
    printf("\n\nI do not have root access!!!\n\n");
  }
}

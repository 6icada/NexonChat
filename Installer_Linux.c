//Code by 6icada
//Please do not copy code

//Adding libraries
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <zconf.h>

//Main function
int main(){
  //Adding vars
  int ToChoose;
  int x = getuid();

  //Checking root access
  if(x == 0){
    printf("1)Install tools\n");
    printf("2)Compile codes\n");
    printf("3)Both\n\n");
    printf("Choose what to do: ");
    scanf("%d", &ToChoose);

    if(ToChoose == 1){
      //Installing tools
      {
        //Fixing broken pkg
        system("apt --fix-broken install -y > /dev/null");

        //Installing ncat and netcat(nc)
        system("apt install ncat -y > /dev/null");
        system("apt install netcat -y > /dev/null");

        //Installing git
        system("apt install git -y > /dev/null");

        //Installing gcc
        system("apt install gcc -y > dev/null");

        //Installing mawk
        system("apt install mawk -y > /dev/null");
      }
    }
    else if(ToChoose == 2){
      //Compiling codes
      {
        //Compiling Server_Linux.c
        system("gcc Server_Linux.c -o Server_Linux");

        //Compiling Client_Linux.c
        system("gcc Client_Linux.c -o Client_Linux");

        //Compiling ControlerServer_Linux
        system("gcc ControlerServer_Linux.c -o ControlerServer_Linux");

        //Compiling NexonChat
        system("gcc NexonChat.c -o NexonChat");
        //Coping compiled code to /bin file
        system("cp NexonChat /bin/");

        //Compiling Port_Forwarder
        system("gcc Port_Forwarder.c -o Port_Forwarder");

        //Compiling ServerScanner_Linux
        system("gcc ServerScanner_Linux.c -o ServerScanner_Linux");
      }
    }
    else if(ToChoose == 3){
      //Installing tools
      {
        //Fixing broken pkg
        system("apt --fix-broken install -y > /dev/null");

        //Installing ncat and netcat(nc)
        system("apt install ncat -y > /dev/null");
        system("apt install netcat -y > /dev/null");

        //Installing git
        system("apt install git -y > /dev/null");

        //Installing gcc
        system("apt install gcc -y > dev/null");

        //Installing mawk
        system("apt install mawk -y > /dev/null");
      }

      //Compiling codes
      {
        //Compiling Server_Linux.c
        system("gcc Server_Linux.c -o Server_Linux");

        //Compiling Client_Linux.c
        system("gcc Client_Linux.c -o Client_Linux");

        //Compiling ControlerServer_Linux
        system("gcc ControlerServer_Linux.c -o ControlerServer_Linux");

        //Compiling NexonChat
        system("gcc NexonChat.c -o NexonChat");
        //Coping compiled code to /bin file
        system("cp NexonChat /bin/");

        //Compiling Port_Forwarder
        system("gcc Port_Forwarder.c -o Port_Forwarder");

        //Compiling ServerScanner_Linux
        system("gcc ServerScanner_Linux.c -o ServerScanner_Linux");
      }
    }
    else{
      //Warning
      printf("\n\nInvalid input!!!\n\n");
    }
  }
  else{
    //Warning
    printf("\n\nI do not have root access!!!\n\n");
  }
}

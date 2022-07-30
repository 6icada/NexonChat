# Code by 6icada
# Project NexonChat

# Tring to import libraries
try:
    import socket
    import threading
    import os
    from time import sleep as slp
except:
    # ERROR MSG
    print(f'[ERROR]: Can\'t import libraries...')
    exit()

# Adding SysINFO Texts
exitINFO = '//EXIT//'
pyFileINFO = '//.py//'
cFileINFO = '//.c//'
txtFileINFO = '//.txt//'

# Adding vars
HOST = '0.0.0.0' # Change this if you want specific IPv4 address
PORT = 4444
Server_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
counter1 = 1
MAX_USERS = 5

# Adding lists
clients = []
threads = []
nicknames = []

# Tring to listen
try:
    # Binding Server_Socket
    Server_Socket.bind((HOST, PORT))
    Server_Socket.listen()
except:
    # ERROR MSG
    print('[ERROR]: Can\'t start server...')
    exit()

# MSG when server starts
print(f'[START]: Server listening on {HOST}:{PORT}')

# Handle function (This function will handle one client at the time)
def Handle():
    while True:
        while True:
            # Receiving INFO about client
            client, address = Server_Socket.accept()

            # BroadcastMSG function (This will send MSGs to other clients)
            def BroadcastMSG(msg):
                for Client in clients:
                    if Client == client:
                        pass
                    else:
                        Client.send(msg.encode('utf-8'))

            # Receiving Nickname
            receivedNickname = client.recv(16)
            decodedReceivedNickname = receivedNickname.decode('utf-8')

            # Checking decodedReceivedNickname
            if decodedReceivedNickname in nicknames:
                # Sending ERROR MSG To the client
                client.send(f'[ERROR]: Nickname is already used...'.encode('utf-8'))
                break
            else:
                # Adding decodedReceivedNickname in nicknames list
                nicknames.append(decodedReceivedNickname)

            # Adding clinet in clients list
            clients.append(client)

            # Sending INFO MSG to the client
            client.send(f'[INFO]: You joined the server!'.encode('utf-8'))

            # Printing INFO
            print(f'[INFO]: {decodedReceivedNickname} joined!')

            slp(0.2)

            # Sending USERS to the client
            if len(clients) == 5:
                client.send(f'[USERS]: {nicknames[0]}, {nicknames[1]}, {nicknames[2]}, {nicknames[3]}, {nicknames[4]}'.encode('utf-8'))
            elif len(clients) == 4:
                client.send(f'[USERS]: {nicknames[0]}, {nicknames[1]}, {nicknames[2]}, {nicknames[3]}'.encode('utf-8'))
            elif len(clients) == 3:
                client.send(f'[USERS]: {nicknames[0]}, {nicknames[1]}, {nicknames[2]}'.encode('utf-8'))
            elif len(clients) == 2:
                client.send(f'[USERS]: {nicknames[0]}, {nicknames[1]}'.encode('utf-8'))
            elif len(clients) == 1:
                client.send(f'[USERS]: {nicknames[0]}'.encode('utf-8'))
            else:
                pass

            # Sending MSG to other clients
            BroadcastMSG(f'{decodedReceivedNickname} joined!')

            # Main loop
            while True:
                # Receiving MSG from client
                receivedMSG = client.recv(10000)
                decodedReceivedMSG = receivedMSG.decode('utf-8')

                # Checking decodedReceivedMSG
                if decodedReceivedMSG[0] == '/':
                    if decodedReceivedMSG == exitINFO:
                        # Sending WARNING INFO to the client
                        client.send(f'[WARNING]: You can not do that!'.encode('utf-8'))

                        # Printing WARNING MSG
                        print(f'[WARNING]: {decodedReceivedNickname} tried to leak EXIT_INFO!')
                    elif decodedReceivedMSG == '/exit':
                        # Sending EXIT_INFO to the client (This MSG will turn off 'Receive' function on client side)
                        client.send(exitINFO.encode('utf-8'))

                        # Removing client's INFO from lists
                        nicknames.remove(decodedReceivedNickname)
                        clients.remove(client)

                        # Printing INFO
                        print(f'[INFO]: {decodedReceivedNickname} left!')

                        # Sending MSG to other clients
                        BroadcastMSG(f'{decodedReceivedNickname} left!')
                        break
                    elif decodedReceivedMSG == '/upload':
                        # Receiving SysINFO about file
                        dataAboutFile = client.recv(100)
                        decodedDataAboutFile = dataAboutFile.decode('utf-8')

                        # Checking decodedDataAboutFile
                        if decodedDataAboutFile == pyFileINFO:
                            # Receiving file
                            receivedDataForFile = client.recv(10000000)
                            decodedReceivedDataForFile = receivedDataForFile.decode('utf-8')

                            # Storing decodedReceivedDataForFile in File
                            uploadedFile = open('uploadedFile.py', 'w')
                            uploadedFile.write(decodedReceivedDataForFile)
                            uploadedFile.close()

                            # Printing INFO
                            print(f'[INFO]: {decodedReceivedNickname} uploaded file!')

                            # Sending INFO to other clients
                            BroadcastMSG(f'[INFO]: {decodedReceivedNickname} uploaded file!')
                        elif decodedDataAboutFile == cFileINFO:
                            # Receiving file
                            receivedDataForFile = client.recv(10000000)
                            decodedReceivedDataForFile = receivedDataForFile.decode('utf-8')

                            # Storing decodedReceivedDataForFile in File
                            uploadedFile = open('uploadedFile.py', 'w')
                            uploadedFile.write(decodedReceivedDataForFile)
                            uploadedFile.close()

                            # Printing INFO
                            print(f'[INFO]: {decodedReceivedNickname} uploaded file!')

                            # Sending INFO to other clients
                            BroadcastMSG(f'[INFO]: {decodedReceivedNickname} uploaded file!')
                        elif decodedDataAboutFile == txtFileINFO:
                            # Receiving file
                            receivedDataForFile = client.recv(10000000)
                            decodedReceivedDataForFile = receivedDataForFile.decode('utf-8')

                            # Storing decodedReceivedDataForFile in File
                            uploadedFile = open('uploadedFile.py', 'w')
                            uploadedFile.write(decodedReceivedDataForFile)
                            uploadedFile.close()

                            # Printing INFO
                            print(f'[INFO]: {decodedReceivedNickname} uploaded file!')

                            # Sending INFO to other clients
                            BroadcastMSG(f'[INFO]: {decodedReceivedNickname} uploaded file!')
                        else:
                            # ERROR MSG
                            print(f'[ERROR]: Did not recognize file...')
                    elif decodedReceivedMSG == '/download':
                        # Checking file
                        if 'uploadedFile.py' in os.listdir():
                            # Sending SysINFO to the client
                            client.send(pyFileINFO.encode('utf-8'))

                            # Reading File
                            toDownloadFile = open('uploadedFile.py', 'r')
                            dataToSend = toDownloadFile.read()
                            toDownloadFile.close()

                            # Sending dataToSend to the client
                            client.send(dataToSend.encode('utf-8'))

                            # Printing INFO
                            print(f'[INFO]: {decodedReceivedNickname} downloaded file!')

                            # Sending INFO to other clients
                            BroadcastMSG(f'[INFO]: {decodedReceivedNickname} downloaded file!')
                        elif 'uploadedFile.c' in os.listdir():
                            # Sending SysINFO to the client
                            client.send(cFileINFO.encode('utf-8'))

                            # Reading File
                            toDownloadFile = open('uploadedFile.c', 'r')
                            dataToSend = toDownloadFile.read()
                            toDownloadFile.close()

                            # Sending dataToSend to the client
                            client.send(dataToSend.encode('utf-8'))

                            # Printing INFO
                            print(f'[INFO]: {decodedReceivedNickname} downloaded file!')

                            # Sending INFO to other clients
                            BroadcastMSG(f'[INFO]: {decodedReceivedNickname} downloaded file!')
                        elif 'uploadedFile.txt' in os.listdir():
                            # Sending SysINFO to the client
                            client.send(txtFileINFO.encode('utf-8'))

                            # Reading File
                            toDownloadFile = open('uploadedFile.txt', 'r')
                            dataToSend = toDownloadFile.read()
                            toDownloadFile.close()

                            # Sending dataToSend to the client
                            client.send(dataToSend.encode('utf-8'))

                            # Printing INFO
                            print(f'[INFO]: {decodedReceivedNickname} downloaded file!')

                            # Sending INFO to other clients
                            BroadcastMSG(f'[INFO]: {decodedReceivedNickname} downloaded file!')
                        else:
                            # ERROR MSG
                            print(f'[ERROR]: Can\'t find file...')

                            # Sending ERROR MSG to the client
                            client.send(f'[ERROR]: Can\'t find file...'.encode('utf-8'))
                else:
                    # Sending MSG to other clients
                    BroadcastMSG(f'{decodedReceivedNickname}: {decodedReceivedMSG}')

# Making threads
while counter1 <= MAX_USERS:
    handleThread = threading.Thread(target=Handle)

    threads.append(handleThread)

    counter1 = counter1 + 1

# Starting threads
for thread in threads:
    thread.start()
